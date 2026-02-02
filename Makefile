# Variáveis
PORT_PROXY = 6277
PORT_INSPECTOR = 6274
PYTHON = venv/bin/python3
SERVER_SCRIPT = server.py

.PHONY: clean run-inspector list restart

# 1. Mata qualquer processo travando as portas do MCP
clean:
	@echo "🧹 Limpando processos nas portas $(PORT_PROXY) e $(PORT_INSPECTOR)..."
	-fuser -k $(PORT_PROXY)/tcp 2>/dev/null || true
	-fuser -k $(PORT_INSPECTOR)/tcp 2>/dev/null || true
	@echo "✅ Portas liberadas."

# 2. Inicia o Inspector do zero (limpa antes)
run-inspector: clean
	@echo "🚀 Iniciando MCP Inspector..."
	npx @modelcontextprotocol/inspector $(PYTHON) $(SERVER_SCRIPT)

# 3. Atalho para quando você só quer resetar e ver se o Claude reconecta
init: clean
	@echo "🔄 Servidor resetado. O Claude no VS Code deve reconectar automaticamente."

# 4. Verifica quem está rodando
list:
	@echo "🔍 Verificando processos MCP..."
	lsof -i :$(PORT_PROXY) || echo "Porta $(PORT_PROXY) está livre."