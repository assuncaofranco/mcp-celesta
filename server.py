from mcp.server.fastmcp import FastMCP
import chromadb
import os

mcp = FastMCP("SeniorArchitect")

db_path = os.path.join(os.getcwd(), "database", "chroma_db")
chroma_client = chromadb.PersistentClient(path=db_path)
collection = chroma_client.get_collection(name="project_code")

@mcp.tool()
async def get_architecture_plan(task_description: str) -> str:
    """
    Consulta o código local e gera um plano técnico estruturado para uma tarefa.
    Retorna um plano detalhado com Actions, Patterns e Modifications.
    """

    # Consulta o RAG para contexto
    results = collection.query(
        query_texts=[task_description],
        n_results=5
    )
    context = "\n".join(results['documents'][0]) if results['documents'] else ""

    # Mock: Retorna plano estruturado para a tarefa específica do ExternalLoggerNode
    # Em produção, isso seria gerado pelo Ollama/Qwen baseado no contexto
    if "ExternalLoggerNode" in task_description or "nó de ação" in task_description.lower():
        plan = {
            "task": task_description,
            "context_summary": context[:300] + "..." if len(context) > 300 else context,
            "actions": [
                {
                    "type": "Create file",
                    "file": "src/domain/nodes/ExternalLoggerNode.ts",
                    "description": "Criar novo nó de ação ExternalLoggerNode que loga mensagens recebidas"
                }
            ],
            "patterns": [
                {
                    "pattern": "Follow the ActionNode interface",
                    "description": "O novo nó deve implementar a interface ActionNode existente"
                }
            ],
            "modifications": [
                {
                    "file": "src/infra/mappers/NodeDataMapper.ts",
                    "description": "Registrar o novo nó no mapeador de nós"
                }
            ]
        }
        
        # Formata como string estruturada (simulando saída do Ollama)
        formatted_plan = f"""PLANO TÉCNICO ESTRUTURADO

Task: {plan['task']}

Context Summary:
{plan['context_summary']}

Action: Create file {plan['actions'][0]['file']}
Description: {plan['actions'][0]['description']}

Pattern: {plan['patterns'][0]['pattern']}
Description: {plan['patterns'][0]['description']}

Modification: Register the new node in {plan['modifications'][0]['file']}
Description: {plan['modifications'][0]['description']}

---
Plano gerado pelo Senior Architect MCP Server
"""
        return formatted_plan
    
    # Para outras tarefas, retorna plano genérico baseado no contexto
    plan = f"""PLANO TÉCNICO ESTRUTURADO

Task: {task_description}

Context Summary:
{context[:300]}...

Actions:
- Analisar código existente
- Implementar funcionalidade solicitada

Patterns:
- Seguir padrões arquiteturais existentes no projeto

Modifications:
- Atualizar arquivos conforme necessário

---
Plano gerado pelo Senior Architect MCP Server
"""
    return plan

if __name__ == "__main__":
    mcp.run()
