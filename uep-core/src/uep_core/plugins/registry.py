from typing import Dict, Any

class PluginRegistry:
    def __init__(self):
        self._plugins: Dict[str, Any] = {}

    def register(self, name: str, plugin: Any) -> None:
        if name in self._plugins:
            raise ValueError(f"Plugin '{name}' is already registered.")
        self._plugins[name] = plugin

    def unregister(self, name: str) -> None:
        if name not in self._plugins:
            raise ValueError(f"Plugin '{name}' is not registered.")
        del self._plugins[name]

    def get_plugin(self, name: str) -> Any:
        return self._plugins.get(name)

    def list_plugins(self) -> Dict[str, Any]:
        return self._plugins.copy()


# Backwards-compatible name used across the codebase/tests
ModelRegistry = PluginRegistry