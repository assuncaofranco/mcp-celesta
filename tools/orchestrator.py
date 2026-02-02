# tools/orchestrator.py
import json
from tools.file_manager import FileManager

class Orchestrator:
    def __init__(self):
        self.file_manager = FileManager()

    async def run_full_cycle(self, user_query: str):
        """
        Assemble data for the Local LLM to review.
        """
        # 1. First Pass: Create the "Context Package" for the Local LLM
        # We don't send files yet, just the project intent
        local_input = self._prepare_7b_intelligence_package(user_query)
        
        # 2. Breakpoint here! 
        # Inspect 'local_input' to see what we are sending to the 7B
        print("[*] Intelligence package assembled.")
        
        # 3. Simulate 7B requesting specific architecture files
        # (In the future, this will be an actual call to your 7B)
        mock_7b_requirements = [
            {"target": "Makefile"},
            {"target": "tools/orchestrator.py"}
        ]
        
        # 4. Final Assembly
        final_payload = self._assemble_final_payload(user_query, mock_7b_requirements)
        
        return {
            "status": "success",
            "content": f"Payload assembled with {len(mock_7b_requirements)} files. Ready for Claude CLI."
        }

    def _prepare_7b_intelligence_package(self, query):
        return {
            "role": "Project Scout",
            "task": query,
            "project_name": "Celesta-MCP"
        }

    def _assemble_final_payload(self, query, requirements):
        context = []
        for req in requirements:
            content = self.file_manager.read_file(req["target"])
            context.append({"file": req["target"], "content": content})
        
        return {"original_query": query, "context": context}
