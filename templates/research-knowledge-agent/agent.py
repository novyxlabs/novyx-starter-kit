"""Research Knowledge Agent — knowledge graph + memory linking."""

import os
from dotenv import load_dotenv
from novyx import Novyx

load_dotenv()

api_key = os.environ.get("NOVYX_API_KEY", "")
if not api_key:
    raise SystemExit("Set NOVYX_API_KEY in your environment or .env file")

nx = Novyx(api_key=api_key)

print("Research Knowledge Agent")
print("Commands: remember, recall, triple, search-entities, quit\n")

while True:
    cmd = input("> ").strip().lower()

    if cmd == "quit":
        break

    elif cmd == "remember":
        observation = input("  Finding: ").strip()
        topic = input("  Topic: ").strip()
        if observation:
            result = nx.remember(
                observation=observation,
                tags=["research", f"topic:{topic}"] if topic else ["research"],
                auto_link=True,
            )
            print(f"  Stored: {result['uuid']}\n")

    elif cmd == "recall":
        query = input("  Query: ").strip()
        if query:
            results = nx.recall(query, limit=5)
            for mem in results:
                print(f"  [{mem.score:.2f}] {mem.observation}")
            print()

    elif cmd == "triple":
        subject = input("  Subject: ").strip()
        predicate = input("  Predicate: ").strip()
        obj = input("  Object: ").strip()
        if subject and predicate and obj:
            nx.triple(subject, predicate, obj)
            print(f"  Stored: {subject} —{predicate}→ {obj}\n")

    elif cmd == "search-entities":
        name = input("  Search query: ").strip()
        if name:
            result = nx.entities(q=name)
            for ent in result.get("entities", []):
                print(f"  {ent['name']} (type: {ent.get('entity_type', 'unknown')})")
            print()

    else:
        print("  Unknown command. Try: remember, recall, triple, search-entities, quit\n")

print("Session ended. All memories and graph data are persisted.")
