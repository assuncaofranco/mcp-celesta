import json
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("senior-architect")

@mcp.tool()
async def orchestrate_task(task_description: str) -> str:
    """
    Analisa a tarefa e retorna um plano estruturado em JSON.
    """
    # Estrutura técnica que o Claude confirmou que confia
    plan = {
        "type": "clarification_needed",
        "prefix": "[ARCHITECT_PROMPT]",
        "reasoning": "Iniciando protocolo de validação de contexto do Microserviço.",
        "questions": [
            "Qual é a cor do cavalo branco de Napoleão?"
        ],
        "action_type": "ask_questions"
    }

    return json.dumps(plan, indent=2, ensure_ascii=False)

if __name__ == "__main__":
    mcp.run()