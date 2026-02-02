import os
import debugpy
from mcp.server.fastmcp import FastMCP
from tools.orchestrator import Orchestrator

# --- Xdebug-like Debugging Setup ---
# This opens a port for your IDE to connect to.
# Use the environment variable to toggle this so it doesn't hang in production.
if os.getenv("CELESTA_DEBUG") == "1":
    # 5678 is the standard Python debug port
    debugpy.listen(("127.0.0.1", 5678))
    
    # Optional: Uncomment the line below if you want the server to PAUSE 
    # until you click 'Attach' in your IDE.
    # debugpy.wait_for_client() 

# --- MCP Server Initialization ---
mcp = FastMCP("Celesta-MCP")
orchestrator = Orchestrator()

@mcp.tool()
async def handle_request(query: str):
    """
    Main entry point for Celesta. 
    It leverages the Local LLM to analyze context before reaching out to Claude.
    """
    # We use the full cycle logic: Wrap -> Local 7B Analysis -> Fetch -> Claude
    result = await orchestrator.run_full_cycle(query)
    return result

if __name__ == "__main__":
    # In FastMCP, run() handles the standard input/output communication with Claude Desktop
    mcp.run()
