# Integração com VS Code - Status Atual

## 📊 O que temos atualmente

### 1. **Servidor MCP Base** ✅
- Servidor FastMCP configurado em `server.py`
- Ferramenta `get_architecture_plan` implementada
- Comunicação via **stdio** (entrada/saída padrão) - método padrão do FastMCP

### 2. **Estrutura do Projeto**
- `server.py` - Servidor MCP principal
- `tools/` - Diretório para ferramentas (atualmente vazio)
  - `vscode_sync.py` - Arquivo existe mas está vazio
  - `file_manager.py` - Arquivo existe mas está vazio
  - `search_rag.py` - Arquivo existe mas está vazio

### 3. **Configuração VS Code**
- `.vscode/launch.json` - Apenas configuração de debug Python básica
- **Não há configuração específica para MCP**

## ❌ O que falta para comunicação completa

### 1. **Configuração do Servidor MCP no VS Code**

Para conectar o servidor MCP com extensões do VS Code (Cline, Roo Code, Claude Desktop), você precisa:

#### Opção A: Configuração via settings.json (Recomendado)

Criar/editar `.vscode/settings.json`:

```json
{
  "mcp.servers": {
    "SeniorArchitect": {
      "command": "python",
      "args": [
        "/home/lucas/Desktop/personal-projects/mcp-celesta/server.py"
      ],
      "env": {
        "PYTHONPATH": "/home/lucas/Desktop/personal-projects/mcp-celesta"
      }
    }
  }
}
```

#### Opção B: Configuração Global (para Cline/Roo Code)

Para extensões como **Cline** ou **Roo Code**, a configuração pode ser feita em:
- `~/.config/Code/User/settings.json` (Linux)
- `~/Library/Application Support/Code/User/settings.json` (Mac)
- `%APPDATA%\Code\User\settings.json` (Windows)

```json
{
  "cline.mcpServers": {
    "SeniorArchitect": {
      "command": "python",
      "args": [
        "/caminho/absoluto/para/server.py"
      ]
    }
  }
}
```

### 2. **Implementação das Ferramentas Vazias**

Os arquivos em `tools/` estão vazios e podem ser implementados:

- **`vscode_sync.py`**: Sincronização bidirecional com VS Code
  - Ler arquivos do workspace
  - Escrever arquivos no workspace
  - Notificar mudanças

- **`file_manager.py`**: Gerenciamento de arquivos
  - Criar arquivos
  - Editar arquivos
  - Deletar arquivos
  - Listar arquivos

- **`search_rag.py`**: Busca no RAG (já parcialmente implementado no server.py)

### 3. **Ferramentas Adicionais para o Servidor MCP**

Podem ser adicionadas mais ferramentas ao servidor:

```python
@mcp.tool()
async def read_file(file_path: str) -> str:
    """Lê o conteúdo de um arquivo"""
    pass

@mcp.tool()
async def write_file(file_path: str, content: str) -> bool:
    """Escreve conteúdo em um arquivo"""
    pass

@mcp.tool()
async def list_files(directory: str) -> list:
    """Lista arquivos em um diretório"""
    pass
```

## 🔧 Como testar a comunicação

### 1. Teste Local (stdio)

```bash
# No terminal
cd /home/lucas/Desktop/personal-projects/mcp-celesta
python server.py
```

O servidor deve iniciar e aguardar conexões via stdio.

### 2. Teste com Extensão VS Code

1. Instale uma extensão compatível:
   - **Cline** (https://marketplace.visualstudio.com/items?itemName=Codeium.codeium)
   - **Roo Code** (se disponível)
   - **Claude Desktop** (se disponível)

2. Configure o servidor MCP nas configurações da extensão

3. Teste chamando a ferramenta `get_architecture_plan` através da extensão

## 📝 Próximos Passos Recomendados

1. ✅ Criar `.vscode/settings.json` com configuração do servidor MCP
2. ✅ Implementar ferramentas básicas de gerenciamento de arquivos
3. ✅ Adicionar ferramenta para executar o plano retornado
4. ✅ Testar integração com extensão do VS Code
5. ✅ Documentar processo de configuração no README

## 🔗 Referências

- [Documentação FastMCP](https://github.com/jlowin/fastmcp)
- [Model Context Protocol Spec](https://modelcontextprotocol.io/)
- [Cursor MCP Tutorial](https://docs.cursor.com/pt-BR/guides/tutorials/building-mcp-server)



