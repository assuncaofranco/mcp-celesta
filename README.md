# MCP Senior Architect - MVP

A minimal Model Context Protocol (MCP) server that acts as a Senior Software Architect.

## Setup

1. **Install dependencies:**
```bash
pip install -r requirements.txt
```

2. **Configure for VS Code:**

Add to your workspace `.vscode/settings.json`:

```json
{
  "mcp.servers": {
    "SeniorArchitect": {
      "command": "${command:python.interpreterPath}",
      "args": ["${workspaceFolder}/server.py"],
      "env": {
        "PYTHONPATH": "${workspaceFolder}"
      }
    }
  }
}
```

**OR for Claude Desktop:**

Edit `~/.config/Claude/claude_desktop_config.json`:

```json
{
  "mcpServers": {
    "SeniorArchitect": {
      "command": "/usr/bin/python3",
      "args": ["/full/path/to/server.py"],
      "env": {
        "PYTHONPATH": "/full/path/to/project"
      }
    }
  }
}
```

3. **Restart VS Code or Claude Desktop completely**

## Available Tools

- `orchestrate_task` - Receives a task and returns an architect-approved plan (MVP test)

## Usage

Once configured and connected, Claude will automatically have access to this tool.

**Test the connection:**
- "Use orchestrate_task to test: add a new feature"

## Testing

The server runs via stdio. To verify it's working:

1. Check that the MCP server appears in your AI extension's tool list
2. Try calling `orchestrate_task` with a test description
3. You should receive: `[Senior-Architect] MVP Connection Success! Task received: <your description>`
