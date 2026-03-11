"""Trading Audit Agent — decision logging with audit trails and rollback."""

import os
from dotenv import load_dotenv
from novyx import Novyx

load_dotenv()

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
        importance = input("  Importance (1-10, default 5): ").strip()

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
            importance=int(importance) if importance else 5,
        )
        print(f"  Logged: {result['uuid']}\n")

    elif cmd == "recall":
        query = input("  Query: ").strip()
        if query:
            results = nx.recall(query, limit=5)
            for mem in results:
                print(f"  [{mem.score:.2f}] {mem.observation}")
            print()

    elif cmd == "audit":
        print("  Fetching audit trail...")
        entries = nx.audit()
        for entry in entries[:10]:
            print(f"  {entry['timestamp']} | {entry['operation']} | {entry.get('artifact_id', 'N/A')}")
        print()

    elif cmd == "rollback-preview":
        steps = input("  Steps to rollback (default 1): ").strip()
        n = int(steps) if steps else 1
        preview = nx.rollback_preview(f"{n} steps ago")
        print(f"  Would affect {preview.get('artifacts_modified', 0)} memories:")
        for warning in preview.get("warnings", []):
            print(f"    ⚠ {warning}")
        if preview.get("safe_rollback"):
            print("  ✅ Safe to rollback")
        else:
            print("  ⚠ Review warnings before proceeding")
        print()

    else:
        print("  Unknown command. Try: log, recall, audit, rollback-preview, quit\n")

print("Session ended. All decisions and audit trail are persisted.")
