#!/usr/bin/env python3
"""
Novyx Starter Kit - Basic Example
===================================
Store and recall memories with semantic search.
"""

import os
from dotenv import load_dotenv
from novyx import Novyx

# Load API key from .env file
load_dotenv()

# Initialize Novyx client
nx = Novyx(api_key=os.getenv("NOVYX_API_KEY"))

print("=== Novyx Basic Example ===\n")

# Store memories
print("1. Storing a few memories with distinct preferences and project context...")
nx.remember("User prefers dark mode")
nx.remember("User's favorite language is Python")
nx.remember("User is building an AI agent for customer support")
print("   ✅ Stored 3 memories\n")

# Semantic search finds related facts even when the wording changes.
print("2. Searching for 'preferred setup'...")
results = nx.recall("What setup or preferences does the user have?")

print("   Found memories:")
for memory in results:
    print(f"     - {memory.observation} (score: {memory.score:.2f})")

print("\n3. Searching for 'what is the user building?'...")
results = nx.recall("what is the user building?")

print("   Found memories:")
for memory in results:
    print(f"     - {memory.observation} (score: {memory.score:.2f})")

print("\n✅ Basic example complete!")
print("   Try session_example.py for continuity and rollback_demo.py for recovery workflows.")
