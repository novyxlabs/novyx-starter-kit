"""Research Knowledge Agent — knowledge graph + memory linking."""

import os
from novyx import Novyx

api_key = os.environ.get("NOVYX_API_KEY", "")
if not api_key:
    raise SystemExit("Set NOVYX_API_KEY in your environment or .env file")

nx = Novyx(api_key=api_key)

print("Research Knowledge Agent")
print("Commands: remember, recall, triple, entity, quit\n")

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
            print(f"  Stored: {result.memory_id}\n")

    elif cmd == "recall":
        query = input("  Query: ").strip()
        if query:
            results = nx.recall(query, top_k=5)
            for mem in results.memories:
                print(f"  [{mem.relevance:.2f}] {mem.observation}")
            print()

    elif cmd == "triple":
        subject = input("  Subject: ").strip()
        predicate = input("  Predicate: ").strip()
        obj = input("  Object: ").strip()
        if subject and predicate and obj:
            nx.knowledge_triples(
                triples=[{"subject": subject, "predicate": predicate, "object": obj}]
            )
            print(f"  Stored: {subject} —{predicate}→ {obj}\n")

    elif cmd == "entity":
        name = input("  Entity name: ").strip()
        if name:
            result = nx.entity(name)
            for triple in result.triples:
                print(f"  {triple.subject} —{triple.predicate}→ {triple.object}")
            print()

    else:
        print("  Unknown command. Try: remember, recall, triple, entity, quit\n")

print("Session ended. All memories and graph data are persisted.")
