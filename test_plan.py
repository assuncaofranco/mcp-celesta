"""
Script de teste para demonstrar o uso da ferramenta get_architecture_plan
"""

import asyncio
from server import get_architecture_plan

async def test_plan():
    """Testa a ferramenta get_architecture_plan com a tarefa do ExternalLoggerNode"""
    
    task = "Adicione um novo nó de ação chamado ExternalLoggerNode que apenas loga uma mensagem recebida"
    
    print("=" * 80)
    print("TESTE DA FERRAMENTA get_architecture_plan")
    print("=" * 80)
    print(f"\nTarefa: {task}\n")
    print("-" * 80)
    
    plan = await get_architecture_plan(task)
    
    print(plan)
    print("=" * 80)

if __name__ == "__main__":
    asyncio.run(test_plan())



