"""Trading Audit Agent — decision logging with audit trails and rollback."""

import os
from novyx import Novyx

api_key = os.environ.get("NOVYX_API_KEY", "")
if not api_key:
    raise SystemExit("Set NOVYX_API_KEY in your environment or .env file")

nx = Novyx(api_key=api_key)

print("Trading Audit Agent")
print("Commands: log, recall, audit, rollback-preview, quit\n")

while True:
    cmd = input("> ").strip().lower()

    if cmd == "quit":
        break

    elif cmd == "log":
        decision = input("  Decision (e.g., 'Buy 0.5 BTC at 42000'): ").strip()
        asset = input("  Asset (e.g., BTC): ").strip()
        strategy = input("  Strategy (e.g., momentum): ").strip()
        decision_type = input("  Type (buy/sell/hold): ").strip()
        importance = input("  Importance (0.0-1.0, default 0.5): ").strip()

        tags = ["trade"]
        if asset:
            tags.append(f"asset:{asset}")
        if strategy:
            tags.append(f"strategy:{strategy}")
        if decision_type:
            tags.append(f"decision:{decision_type}")

        result = nx.remember(
            observation=decision,
            tags=tags,
            importance=float(importance) if importance else 0.5,
        )
        print(f"  Logged: {result.memory_id}\n")

    elif cmd == "recall":
        query = input("  Query: ").strip()
        if query:
            results = nx.recall(query, top_k=5)
            for mem in results.memories:
                print(f"  [{mem.relevance:.2f}] {mem.observation}")
            print()

    elif cmd == "audit":
        print("  Fetching audit trail...")
        trail = nx.audit()
        for entry in trail.entries[:10]:
            print(f"  {entry.timestamp} | {entry.action} | {entry.memory_id}")
        print()

    elif cmd == "rollback-preview":
        steps = input("  Steps to rollback (default 1): ").strip()
        preview = nx.rollback_preview(steps=int(steps) if steps else 1)
        print(f"  Would revert {preview.affected_count} memories:")
        for change in preview.changes:
            print(f"    {change.action}: {change.observation}")
        print()

    else:
        print("  Unknown command. Try: log, recall, audit, rollback-preview, quit\n")

print("Session ended. All decisions and audit trail are persisted.")
