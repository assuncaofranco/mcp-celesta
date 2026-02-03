import unittest
from core.config_loader import ConfigLoader
from core.orchestrator import Orchestrator

class TestCelestaFlow(unittest.TestCase):
    def setUp(self):
        """Prepare common objects for all tests."""
        self.project_name = "mcp-celesta"
        self.loader = ConfigLoader(project_name_arg=self.project_name)
        self.context = self.loader.get_full_context()
        self.orch = Orchestrator(self.context)

    def test_prompt_structure_integrity(self):
        """Validates if the prompt has the mandatory Markdown sections."""
        result = self.orch.run("Generate a new service")
        prompt = result["content"]

        # Requirements list for a valid Dossier
        mandatory_sections = [
            "# CELESTA ARCHITECT DOSSIER",
            "## SYSTEM INSTRUCTIONS",
            "## ATTACHED FILES",
            "### File: Makefile"
        ]

        for section in mandatory_sections:
            with self.subTest(section=section):
                self.assertIn(section, prompt, f"Missing mandatory section: {section}")

    def test_symfony_specialized_content(self):
        """Specifically checks for Symfony domain knowledge injection."""
        # Only runs if the loader actually detected Symfony
        if self.context.get("project_config", {}).get("project_type") == "symfony":
            result = self.orch.run("Build a controller")
            prompt = result["content"]
            
            self.assertIn("MODE: SYMFONY", prompt)
            self.assertIn("src/Controller", prompt)
            self.assertIn("Twig", prompt)

if __name__ == "__main__":
    unittest.main()