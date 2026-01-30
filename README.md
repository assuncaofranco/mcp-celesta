# Senior MCP Server - Architect Agent 🧠

Este projeto implementa um servidor **Model Context Protocol (MCP)** em Python que atua como um Arquiteto de Software Sênior. Ele utiliza **RAG** (Retrieval-Augmented Generation) para analisar seus projetos locais e fornecer planos de implementação precisos.

---

## 🚀 Estrutura do Ecossistema

* **Core:** Python com SDK FastMCP.
* **Memory (RAG):** ChromaDB (Banco de dados vetorial local).
* **Reasoning (Brain):** LLM Local via Ollama (**Qwen 2.5 7B Coder**).
* **Execution:** Claude 3.5 Sonnet (via Extensão do VS Code).

---

## 🛠️ Instalação e Configuração

### 1. Pré-requisitos
* **Python 3.10+** instalado.
* **Ollama** instalado (para rodar o modelo localmente).
* **VS Code** com extensão compatível (ex: Cline, Roo Code ou Claude Desktop).

### 2. Configuração do Ambiente
No terminal, dentro da pasta raiz do projeto:

```bash
# Criar o ambiente virtual (venv)
python -m venv venv

# Ativar o ambiente virtual
# No Linux/Mac/Git Bash:
source venv/bin/activate
# No Windows (PowerShell):
.\venv\Scripts\Activate

# Instalar as dependências (Equivalente ao composer install)
pip install -r requirements.txt
