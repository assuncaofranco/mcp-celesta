# Variáveis
PORT_PROXY = 6277
PORT_INSPECTOR = 6274
VENV = venv
PYTHON = $(VENV)/bin/python3
PIP = $(VENV)/bin/pip
SERVER_SCRIPT = server/server.py
CLI_SCRIPT = cli/celesta_run.py

.PHONY: install clean run-inspector list init

# 0. Installation: Creates venv and installs dependencies
install:
	@echo "🛠️ Creating virtual environment and installing dependencies..."
	python3 -m venv $(VENV)
	$(PIP) install --upgrade pip
	$(PIP) install mcp fastmcp
	@if [ -f requirements.txt ]; then $(PIP) install -r requirements.txt; fi
	@echo "✅ Installation completed."

# 1. Kills any process blocking MCP ports
clean:
	@echo "🧹 Cleaning processes on ports $(PORT_PROXY) and $(PORT_INSPECTOR)..."
	-fuser -k $(PORT_PROXY)/tcp 2>/dev/null || true
	-fuser -k $(PORT_INSPECTOR)/tcp 2>/dev/null || true
	@echo "✅ Ports freed."

# 2. Starts the Inspector from scratch (cleans first)
run-inspector: clean
	@echo "🚀 Starting MCP Inspector..."
	npx @modelcontextprotocol/inspector $(PYTHON) $(SERVER_SCRIPT)

# 3. Shortcut to reset and reconnect
init: clean
	@echo "🔄 Server reset. Claude should reconnect automatically."

# 4. Checks what's running
list:
	@echo "🔍 Checking MCP processes..."
	lsof -i :$(PORT_PROXY) || echo "Port $(PORT_PROXY) is free."
## CLI Execution
run-cli:
	@echo "[Celesta] Starting Active Agent mode..."
	@./venv/bin/python3 $(CLI_SCRIPT)

## CLI with argument (e.g.: make task t="your task here")
task:
	@./venv/bin/python3 $(CLI_SCRIPT) "$(t)"