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
print("1. Storing memories...")
nx.remember("User prefers dark mode")
nx.remember("User's favorite language is Python")
nx.remember("User is building an AI agent for customer support")
print("   ✅ Stored 3 memories\n")

# Semantic search (finds by meaning, not keywords)
print("2. Searching for 'user preferences'...")
results = nx.recall("What are the user's preferences?")

print("   Found memories:")
for memory in results.get("memories", []):
    print(f"     - {memory['observation']} (score: {memory['score']:.2f})")

print("\n3. Searching for 'what is the user building?'...")
results = nx.recall("what is the user building?")

print("   Found memories:")
for memory in results.get("memories", []):
    print(f"     - {memory['observation']} (score: {memory['score']:.2f})")

print("\n✅ Basic example complete!")
print("   Try the other examples: langchain_example.py, rollback_demo.py")
