# Customer Support Agent

Session-scoped memory with semantic recall and agent handoff.

## What it does

- Creates a session-scoped memory for each support conversation
- Stores customer messages with semantic tags for later recall
- Hands off context between agents using Novyx memory spaces
- Free tier compatible

## Quick start

```bash
cp .env.example .env
# Add your Novyx API key to .env

pip install -r requirements.txt
python agent.py
```

## How it works

1. **Session memory** — each conversation gets its own session via `NovyxSession`, so memories are scoped and isolated
2. **Semantic recall** — when the customer asks a follow-up, the agent searches session memory for relevant context
3. **Agent handoff** — if the conversation is escalated, the full session memory is available to the next agent via memory spaces

## Requirements

- Python 3.10+
- Novyx API key (free tier works)
- `novyx>=2.7.0`

## Tags used

- `support` — all memories in this template
- `session:{session_id}` — scoped to the conversation
