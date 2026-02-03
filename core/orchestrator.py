import os
import json
from tools.file_manager import FileManager

class Orchestrator:
    """
    Coordinates the data assembly process, identifying project context 
    before preparing payloads for the Local LLM and Claude.
    """
    def __init__(self):
        self.file_manager = FileManager()
        # Specific strings to identify the project's domain
        self.domain_keywords = ["game", "wallet", "promotion", "notification", "contact"]

    async def run_full_cycle(self, user_query: str):
        """
        Main lifecycle: Scout -> Assemble -> Respond.
        """
        # 1. Prepare the Intelligence Package (Scout Phase)
        intelligence_package = self._prepare_7b_intelligence_package(user_query)
        
        # 2. Define requirements (Currently Mocked, later decided by 7B)
        # We simulate the need for specific files based on the detected domain
        requirements = self._determine_initial_requirements(intelligence_package)

        # 3. Final Assembly of the data dossier
        final_markdown_payload = self._assemble_final_payload(
            user_query, 
            requirements, 
            intelligence_package
        )

        # For terminal testing, we return the summary and the formatted payload
        return {
            "status": "success",
            "project": intelligence_package["project_name"],
            "domain": intelligence_package["project_domain"],
            "content": final_markdown_payload
        }

    def _prepare_7b_intelligence_package(self, query: str):
        """
        Gathers basic project metadata and identifies the architectural domain.
        """
        root_path = self.file_manager.find_project_root() or "."
        # Get the actual folder name of the project
        project_dir_name = os.path.basename(os.path.abspath(root_path))
        
        # Identify domain by checking the query and directory name
        detected_domain = "unknown"
        search_target = f"{project_dir_name} {query}".lower()
        
        for keyword in self.domain_keywords:
            if keyword in search_target:
                detected_domain = keyword
                break

        return {
            "role": "Project Scout",
            "project_name": project_dir_name,
            "project_domain": detected_domain,
            "task": query,
            "metadata": {
                "root": root_path,
                "timestamp": "2026-02-02"
            }
        }

    def _determine_initial_requirements(self, intelligence: dict):
        """
        Logic to decide which files are vital based on the domain.
        This serves as the bridge until the 7B takes over this decision.
        """
        domain = intelligence["project_domain"]
        reqs = [
            {"target": "Makefile", "reason": "Build and workflow rules"},
            {"target": "server/server.py", "reason": "Entry point for MCP tools"}
        ]

        # Example of domain-specific auto-selection
        if domain == "wallet":
            reqs.append({"target": "wallet_config.json", "reason": "Domain configuration"})
        
        return reqs

    def _assemble_final_payload(self, query: str, requirements: list, intelligence: dict):
        """
        Compiles the gathered information into a structured Markdown dossier
        optimized for the Claude CLI.
        """
        header = f"# CELESTA ARCHITECT DOSSIER\n"
        header += f"**Domain:** {intelligence['project_domain'].upper()}\n"
        header += f"**Project:** {intelligence['project_name']}\n"
        header += f"**Objective:** {query}\n\n"
        
        context_body = "## TECHNICAL CONTEXT\n"
        
        for req in requirements:
            path = req["target"]
            content = self.file_manager.read_file(path)
            
            if content:
                context_body += f"### File: {path}\n"
                context_body += f"*Reason: {req['reason']}*\n"
                context_body += f"```\n{content}\n```\n\n"
            else:
                context_body += f"### File: {path} (NOT FOUND)\n\n"

        return header + context_body

    def _format_as_json(self, query, requirements, intelligence):
        """
        Alternative formatter if a JSON structure is needed for the local 7B.
        """
        return json.dumps({
            "intelligence": intelligence,
            "query": query,
            "requirements": requirements
        }, indent=4)

