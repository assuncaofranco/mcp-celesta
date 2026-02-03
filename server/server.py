import os
from mcp.server.fastmcp import FastMCP
from core.config_loader import ConfigLoader
from core.orchestrator import Orchestrator

# --- Xdebug-like Debugging Setup ---
# This opens a port for your IDE to connect to.
# Use the environment variable to toggle this so it doesn't hang in production.
if os.getenv("CELESTA_DEBUG") == "1":
    try:
        import debugpy
        # 5678 is the standard Python debug port
        debugpy.listen(("127.0.0.1", 5678))
        
        # Optional: Uncomment the line below if you want the server to PAUSE 
        # until you click 'Attach' in your IDE.
        # debugpy.wait_for_client()
    except ImportError:
        print("[!] debugpy not installed. Debug mode disabled.") 

# --- MCP Server Initialization ---
mcp = FastMCP("Celesta-MCP")
# Initialize ConfigLoader and Orchestrator with context
loader = ConfigLoader()
context = loader.get_full_context()
orchestrator = Orchestrator(context)

@mcp.tool()
async def handle_request(query: str) -> str:
    """
    Main entry point for Celesta. 
    It leverages the Local LLM to analyze context before reaching out to Claude.
    """
    # We use the full cycle logic: Wrap -> Local 7B Analysis -> Fetch -> Claude
    result = await orchestrator.run_full_cycle(query)
    # Return the content as a string for MCP
    if isinstance(result, dict) and "content" in result:
        return result["content"]
    return str(result)

if __name__ == "__main__":
    # In FastMCP, run() handles the standard input/output communication with Claude Desktop
    mcp.run()

