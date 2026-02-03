import sys
from core.config_loader import ConfigLoader
from core.orchestrator import Orchestrator

def main():
    # Get project name from args or use default
    p_name = sys.argv[1] if len(sys.argv) > 1 else "mcp-celesta"

    print(f"--- Celesta Engine Active | Project: {p_name} ---")

    # Prepare context once
    loader = ConfigLoader(project_name_arg=p_name)
    context = loader.get_full_context()

    while True:
        try:
            task = input("(celesta) > ").strip()
            if task.lower() in ['exit', 'q']: break
            if not task: continue

            # Execute Orchestrator
            orch = Orchestrator(context)
            orch.run(task)

        except (KeyboardInterrupt, EOFError):
            break

if __name__ == "__main__":
    main()
