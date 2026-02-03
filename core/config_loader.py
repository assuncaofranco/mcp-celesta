"""
Configuration loader for Celesta MCP.
Handles loading of environment variables, settings, and project-specific configurations.
"""
import os
from typing import Dict, Any, Optional


class ConfigLoader:
    """Loads and manages configuration for the Celesta MCP server."""
    
    def __init__(self, config_path: Optional[str] = None):
        """
        Initialize the configuration loader.
        
        Args:
            config_path: Optional path to a configuration file (future use)
        """
        self.config_path = config_path
        self._config: Dict[str, Any] = {}
        self._load_config()
    
    def _load_config(self):
        """Load configuration from environment variables and config files."""
        # Environment-based configuration
        self._config = {
            "debug_mode": os.getenv("CELESTA_DEBUG") == "1",
            "debug_port": int(os.getenv("CELESTA_DEBUG_PORT", "5678")),
            "anthropic_api_key": os.getenv("ANTHROPIC_API_KEY"),
            "project_root": os.getenv("CELESTA_PROJECT_ROOT", "."),
        }
        
        # Future: Load from config file if provided
        if self.config_path and os.path.exists(self.config_path):
            # TODO: Implement JSON/YAML config file loading
            pass
    
    def get(self, key: str, default: Any = None) -> Any:
        """
        Get a configuration value.
        
        Args:
            key: Configuration key
            default: Default value if key not found
            
        Returns:
            Configuration value or default
        """
        return self._config.get(key, default)
    
    def is_debug_enabled(self) -> bool:
        """Check if debug mode is enabled."""
        return self._config.get("debug_mode", False)
    
    def get_debug_port(self) -> int:
        """Get the debug port number."""
        return self._config.get("debug_port", 5678)
    
    def get_api_key(self) -> Optional[str]:
        """Get the Anthropic API key."""
        return self._config.get("anthropic_api_key")
    
    def get_project_root(self) -> str:
        """Get the project root path."""
        return self._config.get("project_root", ".")

