# Novyx Starter Kit

Get started with Novyx Core in 5 minutes.

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
- **langchain_example.py** — Drop-in replacement for LangChain ConversationBufferMemory
- **rollback_demo.py** — See Magic Rollback in action

## What is Novyx Core?

Novyx Core provides Constitutional AI Infrastructure for production AI agents:

- **RAM (Persistent Memory)** — Sub-100ms semantic search across all memories
- **Sentinel (Security Layer)** — Circuit breaker for unauthorized actions
- **Magic Rollback** — Point-in-time recovery to any verified state

## Pricing

| Tier | Price | Memories | API Calls | Rollbacks |
|------|-------|----------|-----------|-----------|
| Free | $0 | 5,000 | 5,000/mo | 3/mo |
| Pro | $49/mo | Unlimited | 100,000/mo | Unlimited |
| Enterprise | $299/mo | Unlimited | Unlimited | Unlimited |

## Links

- **Website:** https://novyxlabs.com
- **Docs:** https://novyxlabs.com/docs
- **Discord:** https://discord.gg/PCxZ3tMj
- **API Status:** https://novyxlabs.com/status

## License

MIT
