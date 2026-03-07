"""
LLM Client — Multi-provider LLM wrapper.

Supports Anthropic (Claude), OpenAI (GPT), and OpenAI-compatible APIs
(DeepSeek, Qwen, etc.). Configured via config/models.json.

Each agent can use a different model, specified in agents-registry.json.
"""

import json
import logging
import os
from pathlib import Path
from typing import Optional

logger = logging.getLogger(__name__)

# Auto-detect package root
_PACKAGE_ROOT = Path(__file__).resolve().parent.parent


def load_models_config(config_path: str = None) -> dict:
    """Load models.json configuration."""
    if config_path is None:
        config_path = str(_PACKAGE_ROOT / "config" / "models.json")
    return json.loads(Path(config_path).read_text(encoding="utf-8"))


class LLMClient:
    """Unified LLM client supporting multiple providers."""

    def __init__(self, model_key: str = None, config_path: str = None):
        """Initialize LLM client from models.json.

        Args:
            model_key: Key in models.json (e.g., "claude-opus", "gpt-4o").
                       Uses default_model from config if not specified.
            config_path: Path to models.json. Auto-detected if not provided.
        """
        config = load_models_config(config_path)
        models = config["models"]

        if model_key is None:
            model_key = config.get("default_model", "claude-opus")

        if model_key not in models:
            raise ValueError(
                f"Model '{model_key}' not found in models.json. "
                f"Available: {', '.join(models.keys())}"
            )

        self.model_key = model_key
        self.model_config = models[model_key]
        self.provider = self.model_config["provider"]
        self.model_id = self.model_config["model_id"]
        self.default_max_tokens = self.model_config.get("max_tokens", 16384)
        self.default_temperature = self.model_config.get("temperature", 0.3)

        # Resolve API key from environment
        api_key_env = self.model_config.get("api_key_env", "")
        self.api_key = os.environ.get(api_key_env, "")

        if not self.api_key:
            logger.warning(
                f"API key env var '{api_key_env}' not set for model '{model_key}'. "
                f"Set it before making API calls."
            )

        # Initialize provider client
        self._client = None
        self._init_client()

        logger.info(f"LLM client initialized: {model_key} ({self.provider}/{self.model_id})")

    def _init_client(self):
        """Initialize the appropriate provider client."""
        if self.provider == "anthropic":
            import anthropic
            self._client = anthropic.Anthropic(api_key=self.api_key or None)

        elif self.provider in ("openai", "openai_compatible"):
            from openai import OpenAI
            kwargs = {"api_key": self.api_key}
            base_url = self.model_config.get("base_url")
            if base_url:
                kwargs["base_url"] = base_url
            self._client = OpenAI(**kwargs)

        else:
            raise ValueError(f"Unsupported provider: {self.provider}")

    def chat(
        self,
        system_prompt: str,
        messages: list,
        max_tokens: int = None,
        temperature: float = None,
    ) -> str:
        """Send a chat request and return the response text.

        Args:
            system_prompt: System-level instructions.
            messages: List of {"role": "user"|"assistant", "content": "..."}.
            max_tokens: Max response tokens (uses model default if not set).
            temperature: Sampling temperature (uses model default if not set).

        Returns:
            The assistant's response text.
        """
        max_tokens = max_tokens or self.default_max_tokens
        temperature = temperature if temperature is not None else self.default_temperature

        if self.provider == "anthropic":
            return self._chat_anthropic(system_prompt, messages, max_tokens, temperature)
        else:
            return self._chat_openai(system_prompt, messages, max_tokens, temperature)

    async def chat_streaming(
        self,
        system_prompt: str,
        messages: list,
        on_chunk: callable = None,
        max_tokens: int = None,
        temperature: float = None,
    ) -> str:
        """Chat with streaming output.

        Args:
            system_prompt: System instructions.
            messages: Conversation messages.
            on_chunk: Async callback(chunk_text) for each streamed piece.
            max_tokens: Max response tokens.
            temperature: Sampling temperature.

        Returns:
            Complete response text.
        """
        max_tokens = max_tokens or self.default_max_tokens
        temperature = temperature if temperature is not None else self.default_temperature

        if self.provider == "anthropic":
            return await self._stream_anthropic(system_prompt, messages, on_chunk, max_tokens, temperature)
        else:
            return await self._stream_openai(system_prompt, messages, on_chunk, max_tokens, temperature)

    # ── Anthropic Implementation ──

    def _chat_anthropic(self, system_prompt, messages, max_tokens, temperature):
        response = self._client.messages.create(
            model=self.model_id,
            max_tokens=max_tokens,
            system=system_prompt,
            messages=messages,
            temperature=temperature,
        )
        return response.content[0].text

    async def _stream_anthropic(self, system_prompt, messages, on_chunk, max_tokens, temperature):
        full_text = ""
        with self._client.messages.stream(
            model=self.model_id,
            max_tokens=max_tokens,
            system=system_prompt,
            messages=messages,
            temperature=temperature,
        ) as stream:
            for text in stream.text_stream:
                full_text += text
                if on_chunk:
                    await on_chunk(text)
        return full_text

    # ── OpenAI / OpenAI-Compatible Implementation ──

    def _chat_openai(self, system_prompt, messages, max_tokens, temperature):
        oai_messages = [{"role": "system", "content": system_prompt}]
        oai_messages.extend(messages)

        response = self._client.chat.completions.create(
            model=self.model_id,
            messages=oai_messages,
            max_tokens=max_tokens,
            temperature=temperature,
        )
        return response.choices[0].message.content

    async def _stream_openai(self, system_prompt, messages, on_chunk, max_tokens, temperature):
        oai_messages = [{"role": "system", "content": system_prompt}]
        oai_messages.extend(messages)

        full_text = ""
        response = self._client.chat.completions.create(
            model=self.model_id,
            messages=oai_messages,
            max_tokens=max_tokens,
            temperature=temperature,
            stream=True,
        )
        for chunk in response:
            if chunk.choices and chunk.choices[0].delta.content:
                text = chunk.choices[0].delta.content
                full_text += text
                if on_chunk:
                    await on_chunk(text)
        return full_text

    # ── Static Prompt Builders (provider-agnostic) ──

    @staticmethod
    def build_system_prompt(skill_dir: str, workspace_dir: str = None) -> str:
        """Build system prompt from SKILL.md + reference files."""
        skill_path = Path(skill_dir)
        parts = []

        skill_md = skill_path / "SKILL.md"
        if skill_md.exists():
            parts.append(f"# SKILL INSTRUCTIONS\n\n{skill_md.read_text(encoding='utf-8')}")

        refs_dir = skill_path / "references"
        if refs_dir.exists():
            for ref_file in sorted(refs_dir.iterdir()):
                if ref_file.is_file() and ref_file.suffix == ".md":
                    content = ref_file.read_text(encoding="utf-8")
                    parts.append(f"# REFERENCE: {ref_file.stem}\n\n{content}")

        if workspace_dir:
            ws_path = Path(workspace_dir)
            for bootstrap in ["AGENTS.md", "SOUL.md", "IDENTITY.md"]:
                bp = ws_path / bootstrap
                if bp.exists():
                    parts.append(f"# {bootstrap}\n\n{bp.read_text(encoding='utf-8')}")

        return "\n\n---\n\n".join(parts)

    @staticmethod
    def build_supervisor_prompt(supervisor_dir: str) -> str:
        """Build system prompt for supervisor execution."""
        sup_path = Path(supervisor_dir)
        parts = []

        skill_md = sup_path / "SKILL.md"
        if skill_md.exists():
            parts.append(f"# SUPERVISOR INSTRUCTIONS\n\n{skill_md.read_text(encoding='utf-8')}")

        criteria_file = sup_path / "references" / "inspection-criteria.md"
        if criteria_file.exists():
            parts.append(f"# INSPECTION CRITERIA\n\n{criteria_file.read_text(encoding='utf-8')}")

        return "\n\n---\n\n".join(parts)
