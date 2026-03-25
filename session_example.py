#!/usr/bin/env python3
"""
Novyx Starter Kit - Session Memory Example
============================================
Persistent conversation memory across sessions with semantic recall.
"""

import os
from dotenv import load_dotenv
from novyx import Novyx

# Load API key from .env file
load_dotenv()

# Initialize Novyx client
nx = Novyx(api_key=os.getenv("NOVYX_API_KEY"))

print("=== Novyx Session Memory Example ===\n")

# Simulate a conversation with persistent memory
conversation = [
    ("user", "My name is Blake"),
    ("assistant", "Nice to meet you, Blake!"),
    ("user", "I'm building an AI agent for my startup"),
    ("assistant", "That's exciting! What kind of agent?"),
    ("user", "A customer support agent that remembers context"),
    ("assistant", "Great choice! Novyx can help with persistent memory across sessions."),
]

print("1. Storing conversation history with user and assistant turns...")
# Store each exchange as a memory
for role, message in conversation:
    nx.remember(f"{role}: {message}")
print(f"   ✅ Stored {len(conversation)} conversation turns\n")

# Later (even in a different session), recall context
print("2. Recalling context: 'What is the user building?'")
context = nx.recall("What is the user building?")

print("   Context for AI:")
for memory in context:
    print(f"     {memory.observation}")

print("\n3. Recalling context: 'What is the user's name?'")
context = nx.recall("What is the user's name?")

print("   Context for AI:")
for memory in context:
    print(f"     {memory.observation}")

print("\n✅ Session memory example complete!")
print("   These memories persist across sessions, survive restarts, and stay searchable by meaning.")
