#!/bin/bash
# Start all 3 OpenClaw Agents in separate terminal windows (macOS)
#
# Usage:
#   ./scripts/start_team.sh

set -e

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
PACKAGE_ROOT="$(dirname "$SCRIPT_DIR")"

echo "Starting OpenClaw AI Agent Team..."
echo "Package root: $PACKAGE_ROOT"
echo ""

# Check if telegram.json is configured
if grep -q '<TELEGRAM_GROUP_ID>' "$PACKAGE_ROOT/config/telegram.json" 2>/dev/null; then
    echo "ERROR: config/telegram.json has placeholder values."
    echo "Please configure your Telegram bot tokens and group chat ID first."
    echo ""
    echo "Steps:"
    echo "  1. Create 3 bots via @BotFather on Telegram"
    echo "  2. Create a Telegram group and add all 3 bots + yourself"
    echo "  3. Get the group chat ID (send a message, then check via Telegram API)"
    echo "  4. Edit config/telegram.json with the real values"
    exit 1
fi

# macOS: open each agent in a new Terminal window
if [[ "$(uname)" == "Darwin" ]]; then
    for role in pm ipm sa; do
        osascript -e "
            tell application \"Terminal\"
                do script \"cd '$PACKAGE_ROOT' && python3 -m runtime.agent --role $role --package-root '$PACKAGE_ROOT'\"
                activate
            end tell
        "
        echo "  Started ${role^^} Agent in new Terminal window"
    done
# Linux: try gnome-terminal, then fall back to xterm
elif command -v gnome-terminal &>/dev/null; then
    for role in pm ipm sa; do
        gnome-terminal --title="${role^^} Agent" -- \
            bash -c "cd '$PACKAGE_ROOT' && python3 -m runtime.agent --role $role --package-root '$PACKAGE_ROOT'; exec bash"
        echo "  Started ${role^^} Agent in new terminal"
    done
elif command -v xterm &>/dev/null; then
    for role in pm ipm sa; do
        xterm -title "${role^^} Agent" -e \
            "cd '$PACKAGE_ROOT' && python3 -m runtime.agent --role $role --package-root '$PACKAGE_ROOT'; bash" &
        echo "  Started ${role^^} Agent in xterm"
    done
else
    echo "No supported terminal emulator found."
    echo "Please start each agent manually in separate terminals:"
    echo ""
    for role in pm ipm sa; do
        echo "  python3 -m runtime.agent --role $role --package-root '$PACKAGE_ROOT'"
    done
fi

echo ""
echo "All agents started. Check the Telegram group for status messages."
