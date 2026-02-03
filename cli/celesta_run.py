import asyncio
import sys
import os

# Ensure local imports work
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from core.orchestrator import Orchestrator

# --- Xdebug-like Listener ---
# Start this script, then "Attach" from VS Code/PHPStorm on port 5678
try:
    import debugpy
    debugpy.listen(("127.0.0.1", 5678))
    print("[*] Debugger listening on port 5678. You can attach now.")
except ImportError:
    print("[!] debugpy not installed. Running without debugger.")

async def main():
    orchestrator = Orchestrator()
    print("--- Celesta Architect CLI (Debug Mode) ---")

    while True:
        user_query = input("\n[Mission Control] > ")

        if user_query.lower() in ['exit', 'quit', 'q']:
            break

        print(f"[*] Processing data assembly for: {user_query}")

        # This will trigger your breakpoints in orchestrator.py
        result = await orchestrator.run_full_cycle(user_query)

        print("\n[Result Summary]:")
        print(result.get("content", "No response content."))

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("\n[!] Shutting down.")

