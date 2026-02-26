"""Customer Support Agent — session-scoped memory with semantic recall."""

import os
import uuid
from novyx import Novyx

api_key = os.environ.get("NOVYX_API_KEY", "")
if not api_key:
    raise SystemExit("Set NOVYX_API_KEY in your environment or .env file")

nx = Novyx(api_key=api_key)
session_id = str(uuid.uuid4())[:8]
session = nx.session(session_id)

print(f"Support session started: {session_id}")
print("Type 'quit' to end the session.\n")

while True:
    user_input = input("Customer: ").strip()
    if not user_input or user_input.lower() == "quit":
        break

    # Store the customer message in session memory
    session.remember(
        observation=user_input,
        tags=["support", f"session:{session_id}"],
    )

    # Recall relevant context from this session
    results = session.recall(user_input, top_k=3)

    print("\n--- Agent context (from memory) ---")
    for mem in results.memories:
        print(f"  [{mem.relevance:.2f}] {mem.observation}")
    print("---\n")

    # In a real agent, you'd pass the recalled context to an LLM here.
    # For this demo, we just show what the agent would have access to.

print(f"\nSession {session_id} ended. Memories are persisted for handoff.")
