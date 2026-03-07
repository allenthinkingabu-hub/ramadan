#!/bin/bash
# Start a single OpenClaw Agent
#
# Usage:
#   ./scripts/start_agent.sh pm
#   ./scripts/start_agent.sh ipm
#   ./scripts/start_agent.sh sa

set -e

ROLE="${1:?Usage: $0 <pm|ipm|sa>}"
SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
PACKAGE_ROOT="$(dirname "$SCRIPT_DIR")"

# Validate role
case "$ROLE" in
    pm|ipm|sa) ;;
    *) echo "Error: Role must be pm, ipm, or sa"; exit 1 ;;
esac

cd "$PACKAGE_ROOT"

echo "Starting ${ROLE^^} Agent..."
echo "Package root: $PACKAGE_ROOT"
echo ""

python3 -m runtime.agent --role "$ROLE" --package-root "$PACKAGE_ROOT"
