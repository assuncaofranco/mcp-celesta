import os
import yaml
from pathlib import Path
from typing import Optional, Dict, Any

class ConfigLoader:
    """
    Celesta configuration and path resolution system.
    """

    def __init__(self, project_name_arg: Optional[str] = None):
        self.global_config_path = Path.home() / ".celesta" / "config.yaml"
        self.env_var_name = "CELESTA_PROJECTS_ROOT"
        self.project_name_arg = project_name_arg

    def get_projects_root(self) -> Path:
        env_path = os.getenv(self.env_var_name)
        if env_path:
            return Path(env_path).expanduser().resolve()

        # Fallback to parent directory of current project
        return Path.cwd().parent.resolve()

    def resolve_project_path(self) -> Path:
        root = self.get_projects_root()

        if self.project_name_arg:
            target = (root / self.project_name_arg).resolve()
            return target

        return Path.cwd().resolve()

    def resolve_path(self, relative_path: str) -> Path:
        """
        [Item 1.2] Converts relative project paths to absolute system paths.
        Includes security check to prevent directory traversal.
        """
        project_root = self.resolve_project_path()
        target_path = (project_root / relative_path).resolve()

        if not str(target_path).startswith(str(project_root)):
            raise PermissionError(f"Security: Path {relative_path} is outside project root!")

        return target_path

    def load_global_config(self) -> Dict[str, Any]:
        if not self.global_config_path.exists():
            return {}
        try:
            with open(self.global_config_path, 'r') as f:
                return yaml.safe_load(f) or {}
        except Exception as e:
            print(f"[!] Error reading global config: {e}")
            return {}

    def load_project_config(self, project_path: Path) -> Dict[str, Any]:
        project_config_file = project_path / ".celesta" / "project.yaml"
        if not project_config_file.exists():
            return {}
        try:
            with open(project_config_file, 'r') as f:
                return yaml.safe_load(f) or {}
        except Exception as e:
            print(f"[!] Error reading project.yaml: {e}")
            return {}

    def get_full_context(self) -> Dict[str, Any]:
        project_path = self.resolve_project_path()
        return {
            "project_path": project_path,
            "global_config": self.load_global_config(),
            "project_config": self.load_project_config(project_path),
            "is_valid": project_path.exists()
        }
