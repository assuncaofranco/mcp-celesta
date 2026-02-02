import subprocess
import os

class FileManager:
    def __init__(self, root_dir="."):
        self.root_dir = root_dir

    def run_command(self, command: list):
        try:
            result = subprocess.run(
                command,
                capture_output=True,
                text=True,
                cwd=self.root_dir,
                timeout=10
            )
            return result.stdout.strip() if result.returncode == 0 else None
        except Exception as e:
            return f"Error executing command: {str(e)}"

    def find_project_root(self, marker="composer.json"):
        """Locates the root based on a marker file."""
        cmd = ["find", ".", "-name", marker, "-maxdepth", "3"]
        path = self.run_command(cmd)
        return os.path.dirname(path) if path else None

    def list_structure(self, path="."):
        """Returns a simplified directory tree."""
        return self.run_command(["ls", "-R", path])

    def read_file(self, file_path):
        """Reads the content of a specific file."""
        if os.path.exists(file_path):
            with open(file_path, 'r', encoding='utf-8') as f:
                return f.read()
        return "File not found."