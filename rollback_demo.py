#!/usr/bin/env python3
"""
Novyx Starter Kit - Rollback Demo
===================================
See Magic Rollback in action (Pro tier required).
"""

import os
from dotenv import load_dotenv
from novyx import Novyx

# Load API key from .env file
load_dotenv()

# Initialize Novyx client
nx = Novyx(api_key=os.getenv("NOVYX_API_KEY"))

print("=== Novyx Rollback Demo ===\n")

# Store some good memories
print("1. Storing good memories...")
nx.remember("User is a premium customer")
nx.remember("User prefers email communication")
print("   ✅ Stored 2 good memories\n")

# Simulate agent going rogue
print("2. ⚠️  Agent stores bad data...")
nx.remember("User wants to cancel their account")
nx.remember("User is unhappy with service")
print("   ❌ Stored 2 bad memories\n")

print("3. Checking current memories...")
results = nx.recall("user status")
print("   Current memories:")
for m in results.memories[:4]:
    print(f"     - {m.observation}")

# Rollback to before the bad data
print("\n4. 🔄 Rolling back to 1 hour ago...")
try:
    rollback_result = nx.rollback(target="1 hour ago")
    print(f"   ✅ Rolled back to: {rollback_result.get('rolled_back_to')}")
    print(f"   Operations undone: {rollback_result.get('operations_undone', 0)}")

    print("\n5. Memories after rollback:")
    results = nx.recall("user status")
    print("   Restored memories:")
    for m in results.memories[:4]:
        print(f"     - {m.observation}")

    print("\n✅ Bad data removed. Agent memory restored.")

except Exception as e:
    error_msg = str(e)
    if "403" in error_msg or "Forbidden" in error_msg:
        print(f"   ⚠️  Rollback requires a paid tier")
        print(f"   Upgrade at: https://novyxlabs.com/pricing")
        print(f"\n   Free tier: 10 rollbacks/month")
        print(f"   Pro tier: Unlimited rollbacks")
    else:
        print(f"   ❌ Error: {error_msg}")

print("\n📚 Learn more about Magic Rollback:")
print("   https://novyxlabs.com/docs")
