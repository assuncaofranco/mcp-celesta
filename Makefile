# Variables
VENV = venv
PYTHON = $(VENV)/bin/python3
PIP = $(VENV)/bin/pip
CLI_SCRIPT = cli/celesta_run.py
SERVER_SCRIPT = server/server.py
PORT_PROXY = 6277
PORT_INSPECTOR = 6274

# Default Project (can be overridden via command line: make task p=another-project)
p = mcp-celesta

.PHONY: install clean run-inspector list run-cli task test

# 0. Setup
install:
	@echo "[*] Creating virtual environment..."
	python3 -m venv $(VENV)
	$(PIP) install --upgrade pip
	@if [ -f requirements.txt ]; then $(PIP) install -r requirements.txt; fi
	@echo "✅ Installation completed."

# 1. Cleanup
clean:
	@echo "[*] Freeing MCP ports..."
	-fuser -k $(PORT_PROXY)/tcp 2>/dev/null || true
	-fuser -k $(PORT_INSPECTOR)/tcp 2>/dev/null || true
	@find . -type d -name "__pycache__" -exec rm -rf {} +
	@echo "✅ Clean sweep done."

# 2. Development & Debug
run-inspector: clean
	@echo "[*] Launching MCP Inspector..."
	npx @modelcontextprotocol/inspector $(PYTHON) $(SERVER_SCRIPT)

# 3. Testing (Item 1.1 Validation)
test:
	@echo "[*] Running Integration Suite..."
	@$(PYTHON) tests/test_flow.py

# 4. CLI Entry Points
# Usage: make run-cli
run-cli:
	@$(PYTHON) $(CLI_SCRIPT) $(p)

# Usage: make task t="Analyze this folder"
# Usage for other projects: make task p=my-symfony-app t="List routes"
task:
	@$(PYTHON) $(CLI_SCRIPT) $(p) "$(t)"

list:
	@echo "[*] Checking MCP processes..."
	lsof -i :$(PORT_PROXY) || echo "Port $(PORT_PROXY) is free."