# Research Knowledge Agent

Knowledge graph construction, memory linking, and cross-session continuity.

## What it does

- Stores research findings as linked memories with auto-linking
- Builds a knowledge graph of entities and relationships
- Supports cross-session continuity — pick up where you left off
- Requires Pro tier for knowledge graph features

## Quick start

```bash
cp .env.example .env
# Add your Novyx API key to .env

pip install -r requirements.txt
python agent.py
```

## How it works

1. **Memory with auto-linking** — each research finding is stored with `auto_link=True`, so Novyx automatically links related memories
2. **Knowledge graph** — entities and relationships are stored as subject-predicate-object triples via `nx.knowledge_triples()`
3. **Entity lookup** — query the graph for everything known about a specific entity with `nx.entity()`
4. **Cross-session recall** — no session scoping, so all memories persist and are searchable across sessions

## Requirements

- Python 3.10+
- Novyx API key (Pro tier for knowledge graph)
- `novyx>=2.7.0`

## Tags used

- `research` — all memories in this template
- `topic:{name}` — categorizes findings by research topic
