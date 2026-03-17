# AI Secretary

On-demand assistant and daily todo curator. Invoked from Slack for any purpose; delivers a daily todo summary at 8am (except Japanese holidays).

## Contents

- [ai-secretary.md](ai-secretary.md) — Agent definition (role, inputs, outputs, invocation)
- [slack-bot/](slack-bot/) — Slack integration for **!aisec** (call from Slack for any purpose)

## Key Capabilities

- **Slack on-demand:** Handle any request—drafts, summaries, lookups, scheduling, reminders
- **Daily 8am todo:** JIRA tickets (mentioning user, no reply) + Slack + Teams conversations needing attention
