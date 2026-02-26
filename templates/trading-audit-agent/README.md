# Trading Audit Agent

Decision logging, structured tagging, audit trails, and rollback preview.

## What it does

- Logs every trading decision with importance scoring and structured tags
- Generates cryptographic audit trails for compliance
- Previews rollback before reverting agent state
- Free tier for basic audit, Pro tier for rollback features

## Quick start

```bash
cp .env.example .env
# Add your Novyx API key to .env

pip install -r requirements.txt
python agent.py
```

## How it works

1. **Decision logging** — each trade decision is stored with an importance score (0.0–1.0) and structured tags for filtering
2. **Audit trail** — `nx.audit()` returns a cryptographic log of every memory operation, suitable for compliance review
3. **Rollback preview** — before reverting to a previous state, `nx.rollback_preview()` shows exactly what would change
4. **Tag-based recall** — filter memories by asset, strategy, or decision type

## Requirements

- Python 3.10+
- Novyx API key (free for basic audit, Pro for rollback)
- `novyx>=2.7.0`

## Tags used

- `trade` — all memories in this template
- `asset:{symbol}` — the traded asset (e.g., `asset:BTC`)
- `strategy:{name}` — the strategy that triggered the decision
- `decision:{type}` — buy, sell, hold, etc.
