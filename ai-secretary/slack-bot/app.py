"""
AI Secretary !aisec - Slack bot
Responds to !aisec triggers, @mentions, and DMs. Uses Socket Mode for local development.
"""
import os

from dotenv import load_dotenv

load_dotenv()
from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler

app = App(token=os.environ.get("SLACK_BOT_TOKEN"))


def should_respond(event: dict) -> bool:
    """Ignore bot messages and message edits/changes."""
    if event.get("subtype") in ("bot_message", "message_changed", "message_deleted"):
        return False
    return True


def get_user_message(text: str) -> str:
    """Get the user's message, stripping !aisec prefix if present."""
    if text.lower().strip().startswith("!aisec"):
        return text.strip()[6:].strip() or "(no message)"
    return text.strip() or "(no message)"


@app.event("app_mention")
def handle_mention(body, say, logger):
    """Respond when someone mentions @aisec in a channel."""
    event = body.get("event", {})
    if not should_respond(event):
        return

    text = get_user_message(event.get("text", ""))
    user = event.get("user", "unknown")
    channel = event.get("channel")

    logger.info(f"Mention from {user}: {text[:50]}...")

    say(
        channel=channel,
        text=f"Hi <@{user}>! I'm aisec, your AI secretary. You said: _{text}_\n\nI'm connected and ready. More features coming soon.",
    )


@app.event("message")
def handle_message(body, say, logger):
    """Respond to DMs and !aisec triggers in channels."""
    event = body.get("event", {})
    if not should_respond(event):
        return

    raw_text = event.get("text", "").strip()
    channel_type = event.get("channel_type")
    user = event.get("user", "unknown")
    channel = event.get("channel")

    if channel_type == "im":
        text = raw_text or "(no message)"
        logger.info(f"DM from {user}: {text[:50]}...")
    elif raw_text.lower().startswith("!aisec"):
        text = get_user_message(raw_text)
        logger.info(f"!aisec from {user}: {text[:50]}...")
    else:
        return

    say(
        channel=channel,
        text=f"Hi <@{user}>! I'm aisec, your AI secretary. You said: _{text}_\n\nI'm connected and ready. More features coming soon.",
    )


if __name__ == "__main__":
    app_token = os.environ.get("SLACK_APP_TOKEN")
    if not app_token:
        print("Error: SLACK_APP_TOKEN is required. Create an App-Level Token at api.slack.com")
        exit(1)
    if not os.environ.get("SLACK_BOT_TOKEN"):
        print("Error: SLACK_BOT_TOKEN is required. Get it from OAuth & Permissions")
        exit(1)

    print("Starting !aisec... Use Ctrl+C to stop.")
    handler = SocketModeHandler(app, app_token)
    handler.start()
