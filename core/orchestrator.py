import os
import json
import asyncio
from typing import Dict, Any
from tools.file_manager import FileManager

class Orchestrator:
    def __init__(self, context: Dict[str, Any]):
        # ConfigLoader data is injected here
        self.context = context
        self.project_path = context.get("project_path")

        # Initialize tools
        self.file_manager = FileManager()
        self.domain_keywords = ["game", "wallet", "promotion", "notification", "contact"]

    def run(self, task: str):
        """
        Breakpoint entry point for the Debugger.
        """
        print(f"[*] Orchestrator initialized with path: {self.project_path}")
        print(f"[*] Task received: '{task}'")

        return asyncio.run(self.run_full_cycle(task))

    async def run_full_cycle(self, user_query: str):
        # Scout Phase
        intelligence = self._prepare_intelligence(user_query)
        # Assemble Phase - NOW IT WILL FIND THE METHOD
        payload = self._assemble_payload(user_query, intelligence)

        return {
            "status": "success",
            "project": intelligence["project_name"],
            "content": payload
        }

    def _prepare_intelligence(self, query: str):
        root = self.project_path or "."
        return {
            "project_name": os.path.basename(os.path.abspath(root)),
            "task": query
        }

    # FIX: Indented to be inside the Orchestrator class
    def _assemble_payload(self, query: str, intelligence: dict):
        """
        Transforms the raw context into a structured prompt for Claude.
        """
        # 1. Retrieve the project type from the Loader's context
        project_type = self.context.get("project_config", {}).get("project_type", "generic")

        # 2. Build the dynamic header
        header = f"# CELESTA ARCHITECT DOSSIER | MODE: {project_type.upper()}\n"
        header += f"**User Query:** {query}\n\n"

        # 3. Add specific instructions based on project type
        instructions = "## SYSTEM INSTRUCTIONS\n"
        if project_type == "symfony":
            instructions += "- Follow Symfony 6/7 and Twig best practices.\n"
            instructions += "- Consider the standard directory structure: src/Controller and src/Entity.\n"
        else:
            instructions += "- Provide a clean, modular solution following general best practices.\n"

        # 4. Gather file content
        content = self.file_manager.read_file("Makefile")

        files_section = "\n## ATTACHED FILES\n"
        files_section += "### File: Makefile\n"
        files_section += f"```\n{content or 'File not found.'}\n```\n"

        return header + instructions + files_section