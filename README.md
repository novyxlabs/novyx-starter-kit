# Novyx Starter Kit

Get started with Novyx Core in 5 minutes.

> Status: this starter kit is legacy onboarding collateral for the memory,
> audit, and rollback APIs. It is still useful for SDK smoke tests and simple
> examples, but the current Novyx Core product direction is change control for
> AI agents touching production: blast-radius gates, approval evidence,
> compensation, and exactly-once execution for risky side effects.

## Quick Start

1. **Clone this repo:**
   ```bash
   git clone https://github.com/novyxlabs/novyx-starter-kit
   cd novyx-starter-kit
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Get your free API key** at [novyxlabs.com](https://novyxlabs.com)

4. **Create .env file:**
   ```bash
   cp .env.example .env
   # Edit .env and add your API key
   ```

5. **Run the basic example:**
   ```bash
   python basic_example.py
   ```

## Examples

- **basic_example.py** — Store and recall memories with semantic search
- **session_example.py** — Persistent conversation memory across sessions
- **rollback_demo.py** — See Magic Rollback in action

## What is Novyx?

Persistent memory for AI agents — sub-100ms semantic search, time-travel rollback, and tamper-proof audit trails.

- **Persistent Memory** — Store and recall with semantic search across all memories
- **Time-Travel Rollback** — Point-in-time recovery to any verified state
- **Audit Trails** — Cryptographic proof of every memory operation

## How to Use This Repo Now

- Use it to smoke-test the public Python SDK.
- Use the examples as small snippets for docs or demos.
- Do not treat this repo as the flagship Novyx positioning.
- Prefer newer product demos that show change control, blast-radius review, and action approval.

## Pricing

Pricing changes over time. Check the Novyx website for the current plan limits.

## Links

- **Website:** https://novyxlabs.com
- **Docs:** https://docs.novyxlabs.com
- **Discord:** https://discord.gg/PCxZ3tMj
- **API Status:** https://novyxlabs.com/status

## License

MIT
