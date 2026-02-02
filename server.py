from mcp.server.fastmcp import FastMCP

mcp = FastMCP("SeniorArchitect")


@mcp.tool()
async def orchestrate_task(task_description: str) -> str:
    """Receives a task and returns an architect-approved plan."""
    return f"[Senior-Architect] MVP Connection Success! Task received: {task_description}"


if __name__ == "__main__":
    mcp.run()
