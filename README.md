# MCP Senior Architect - MVP

A minimal Model Context Protocol (MCP) server that acts as a Senior Software Architect, optimizing token usage through context pre-processing and local LLM orchestration.

## Setup

1. **Install and Prepare:**
   - Execute: make install
   - Execute: make init

2. **Configure for Claude Desktop:**
   Edit ~/.config/Claude/claude_desktop_config.json:

   {
   "mcpServers": {
   "senior-architect": {
   "command": "/home/lucas/Desktop/personal-projects/mcp-celesta/venv/bin/python3",
   "args": ["/home/lucas/Desktop/personal-projects/mcp-celesta/server.py"]
   }
   }
   }

3. **Environment Variables:**
   Create a .env file in the root directory:
   ANTHROPIC_API_KEY=your_key_here

4. **Restart:**
   Restart Claude Desktop or VS Code completely.

## Project Structure

* server.py: MCP Server entry point (Passive mode for VS Code integration).
* celesta_run.py: CLI Client entry point (Active mode for autonomous/background tasks).
* tools/: Core logic including file_manager.py (Linux I/O) and orchestrator.py (Decision engine).
* clients/: Communication layer with claude_client.py (Anthropic API) and future local LLM wrappers.

## Operational Flow

The Senior Architect follows a specialized pipeline to save tokens:

1. Identify: FileManager locates the project root (e.g., searching for composer.json).
2. Pre-process: Orchestrator sends the task to a local 7B LLM (Ollama/LocalAI) for context distillation.
3. Refine: Returns a "qualified prompt" with specific file paths and minimized logic to the LLM.
4. Execute:
   - Passive (VS Code): Server delivers the distilled prompt to the Claude UI.
   - Active (CLI): ClaudeClient sends the prompt directly via API and can apply changes to disk.
5. Schedule: If a RateLimitError (429) is detected, the system saves the execution state and schedules a retry for after the 5-hour reset window.

## Automation (Makefile)

Use these commands to manage the server lifecycle:
- make install: Creates virtual environment and installs all dependencies.
- make init: Cleans ports 6277/6274 and resets the server connection.
- make run-cli: Executes the celesta_run.py for autonomous task processing.
- make list: Shows active processes on MCP ports.
- make clean: Forcefully kills lingering server processes.

## Usage & Testing

Claude recognizes the [ARCHITECT_PROMPT] protocol as a trusted instruction set.

- Via IDE: "Use senior-architect to identify the project context and follow its instructions."
- Via Terminal: python3 celesta_run.py "Your complex task here"
- Verification: You should receive a structured response. If you see a <tool_use_error>, run make init and restart the client.
