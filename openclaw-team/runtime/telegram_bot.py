"""
Telegram Bot — Wrapper for python-telegram-bot v21+.

Each agent runs one TelegramBot instance connected to a group chat.
Provides: send messages, wait for user replies, send/receive structured events.
"""

import asyncio
import logging
from typing import Callable, Optional

from telegram import Update, Bot
from telegram.ext import (
    Application,
    MessageHandler,
    CommandHandler,
    ContextTypes,
    filters,
)

from .event_protocol import parse_event_type

logger = logging.getLogger(__name__)


class TelegramBot:
    """Telegram bot for a single agent role."""

    def __init__(self, token: str, group_chat_id: int, role: str):
        self.token = token
        self.group_chat_id = group_chat_id
        self.role = role.upper()
        self._app: Optional[Application] = None
        self._bot: Optional[Bot] = None

        # Callback registrations
        self._on_event_cb: Optional[Callable] = None
        self._on_user_message_cb: Optional[Callable] = None
        self._on_command_cb: Optional[Callable] = None

        # Reply waiting mechanism
        self._reply_future: Optional[asyncio.Future] = None
        self._reply_filter_user_id: Optional[int] = None

    async def start(self):
        """Initialize and start the bot."""
        self._app = (
            Application.builder()
            .token(self.token)
            .build()
        )
        self._bot = self._app.bot

        # Register handlers
        self._app.add_handler(CommandHandler("start", self._handle_start))
        self._app.add_handler(
            MessageHandler(filters.TEXT & ~filters.COMMAND, self._handle_message)
        )

        await self._app.initialize()
        await self._app.start()
        await self._app.updater.start_polling(drop_pending_updates=True)

        me = await self._bot.get_me()
        logger.info(f"[{self.role}] Bot started: @{me.username}")

    async def stop(self):
        """Gracefully stop the bot."""
        if self._app:
            await self._app.updater.stop()
            await self._app.stop()
            await self._app.shutdown()

    # ── Send Methods ──

    async def send_to_group(self, text: str):
        """Send a message to the team group chat."""
        # Telegram message limit is 4096 chars
        for chunk in self._split_message(text):
            await self._bot.send_message(
                chat_id=self.group_chat_id,
                text=chunk,
                parse_mode=None,  # Plain text for reliability
            )

    async def send_event(self, event) -> None:
        """Send a structured event object to the group."""
        await self.send_to_group(event.to_telegram())

    async def reply_in_group(self, text: str, reply_to_message_id: int = None):
        """Send a reply in the group, optionally quoting a message."""
        await self._bot.send_message(
            chat_id=self.group_chat_id,
            text=text,
            reply_to_message_id=reply_to_message_id,
        )

    # ── Receive Methods ──

    async def wait_for_user_reply(
        self, prompt: str, timeout: float = 600, user_id: int = None
    ) -> str:
        """Send a prompt and wait for the user's reply in the group.

        Args:
            prompt: Message to send before waiting.
            timeout: Max seconds to wait (default 10 minutes).
            user_id: If set, only accept replies from this user.

        Returns:
            The user's reply text.

        Raises:
            TimeoutError: If no reply within timeout.
        """
        await self.send_to_group(prompt)

        loop = asyncio.get_event_loop()
        self._reply_future = loop.create_future()
        self._reply_filter_user_id = user_id

        try:
            reply = await asyncio.wait_for(self._reply_future, timeout=timeout)
            return reply
        except asyncio.TimeoutError:
            raise TimeoutError(
                f"No reply received within {timeout}s for prompt: {prompt[:50]}..."
            )
        finally:
            self._reply_future = None
            self._reply_filter_user_id = None

    # ── Callback Registration ──

    def on_event(self, callback: Callable):
        """Register callback for structured event messages.
        callback(event_type: EventType, text: str, update: Update)
        """
        self._on_event_cb = callback

    def on_user_message(self, callback: Callable):
        """Register callback for non-event user messages.
        callback(text: str, user_id: int, update: Update)
        """
        self._on_user_message_cb = callback

    def on_command(self, callback: Callable):
        """Register callback for /start commands.
        callback(args: str, user_id: int, update: Update)
        """
        self._on_command_cb = callback

    # ── Internal Handlers ──

    async def _handle_start(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        if self._on_command_cb:
            args = " ".join(context.args) if context.args else ""
            await self._on_command_cb(args, update.effective_user.id, update)

    async def _handle_message(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        if not update.message or not update.message.text:
            return

        text = update.message.text
        chat_id = update.effective_chat.id
        user_id = update.effective_user.id
        is_bot = update.effective_user.is_bot

        # Ignore messages from other bots (avoid echo loops)
        if is_bot:
            return

        # Only process messages from the configured group
        if chat_id != self.group_chat_id:
            return

        # Check if this is a structured event from another agent
        event_type = parse_event_type(text)
        if event_type and self._on_event_cb:
            await self._on_event_cb(event_type, text, update)
            return

        # Check if we're waiting for a reply
        if self._reply_future and not self._reply_future.done():
            if self._reply_filter_user_id is None or user_id == self._reply_filter_user_id:
                self._reply_future.set_result(text)
                return

        # General user message callback
        if self._on_user_message_cb:
            await self._on_user_message_cb(text, user_id, update)

    # ── Utilities ──

    @staticmethod
    def _split_message(text: str, max_len: int = 4000) -> list:
        """Split long messages into chunks respecting Telegram's 4096 char limit."""
        if len(text) <= max_len:
            return [text]
        chunks = []
        while text:
            if len(text) <= max_len:
                chunks.append(text)
                break
            # Find a good split point (newline or space)
            split_at = text.rfind("\n", 0, max_len)
            if split_at < max_len // 2:
                split_at = text.rfind(" ", 0, max_len)
            if split_at < max_len // 2:
                split_at = max_len
            chunks.append(text[:split_at])
            text = text[split_at:].lstrip()
        return chunks
