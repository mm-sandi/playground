# !aisec Slack Bot

Slack integration for the AI Secretary. Call **!aisec** (or @aisec) for any purpose.

## Prerequisites

- Python 3.9+
- A Slack workspace where you can create apps

## Setup

### 1. Create a Slack App

1. Go to [api.slack.com/apps](https://api.slack.com/apps) → **Create New App** → **From scratch**
2. **App Name:** `aisec` (display name becomes @aisec when mentioned)
3. Select your workspace

### 2. Configure the Bot

**Bot Token Scopes** (OAuth & Permissions → Scopes):

- `app_mentions:read` — Detect @mentions
- `chat:write` — Send messages
- `channels:history` — Read channel messages (for !aisec trigger)
- `im:history` — Read DMs
- `im:read` — List DMs
- `users:read` — User info

**Event Subscriptions** → **Enable Events** → **Subscribe to bot events**:

- `app_mention` — When someone @mentions the bot
- `message.im` — When someone DMs the bot
- `message.channels` — When someone types `!aisec` in a channel (required for !aisec trigger)

**Socket Mode** (Basic Information → App-Level Tokens):

1. Enable Socket Mode
2. Create an App-Level Token with scope `connections:write`
3. Copy the token (starts with `xapp-`)

### 3. Install the App

- **OAuth & Permissions** → **Install to Workspace** → Authorize
- Copy the **Bot User OAuth Token** (starts with `xoxb-`)

### 4. Configure Locally

```bash
cd ai-secretary/slack-bot
cp .env.example .env
# Edit .env and add your SLACK_BOT_TOKEN and SLACK_APP_TOKEN
pip install -r requirements.txt
python app.py
```

### 5. Test

- **DM:** Open a DM with @aisec and send a message
- **Channel:** `/invite @aisec` in a channel, then type `!aisec hello` or `@aisec hello`

## Usage

- **DM @aisec** — Ask anything; aisec responds in the DM
- **!aisec** in a channel — Type `!aisec` or `!aisec your message` to invoke
- **@aisec** in a channel — Mention @aisec for on-demand help

## Troubleshooting

- **"missing_scope"** — Add the required scopes and reinstall the app
- **No response** — Ensure `app_mention` and `message.im` are subscribed
- **Socket Mode** — Must be enabled for local dev without ngrok
