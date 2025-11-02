"""Configuration helpers for uep_core.

Provides a lightweight Settings dataclass and a load_config() helper that
loads configuration from an optional JSON file, then applies environment
variable overrides. This keeps imports simple and deterministic for tests.
"""
from __future__ import annotations

import json
import os
from dataclasses import dataclass, asdict
from typing import Optional


@dataclass
class Settings:
    app_name: str = "Universal Exchange Protocol"
    version: str = "1.0.0"
    server_host: str = "0.0.0.0"
    server_port: int = 50051
    log_level: str = "INFO"


# Default instance used when no overrides are provided
default_settings = Settings()


def _apply_overrides_from_dict(s: Settings, overrides: dict) -> Settings:
    for k, v in overrides.items():
        if hasattr(s, k):
            try:
                # Cast port to int when appropriate
                if k.endswith("port"):
                    setattr(s, k, int(v))
                else:
                    setattr(s, k, v)
            except Exception:
                # Ignore malformed overrides to keep load_config robust
                pass
    return s


def load_config(path: Optional[str] = None) -> Settings:
    """Load configuration.

    Order of precedence (highest to lowest):
      1. Values in JSON file at `path` (if provided).
      2. Environment variables: UEP_SERVER_HOST, UEP_SERVER_PORT, UEP_LOG_LEVEL
      3. Defaults defined in `default_settings`.

    Returns a Settings instance.
    """
    cfg = Settings(**asdict(default_settings))

    # 1) JSON file overrides
    if path:
        try:
            if os.path.isfile(path):
                with open(path, "r", encoding="utf-8") as fh:
                    data = json.load(fh)
                if isinstance(data, dict):
                    cfg = _apply_overrides_from_dict(cfg, data)
        except Exception:
            # Fail silently and use defaults; callers/tests shouldn't crash
            pass

    # 2) Environment variable overrides
    env_overrides = {}
    if os.getenv("UEP_SERVER_HOST"):
        env_overrides["server_host"] = os.getenv("UEP_SERVER_HOST")
    if os.getenv("UEP_SERVER_PORT"):
        env_overrides["server_port"] = os.getenv("UEP_SERVER_PORT")
    if os.getenv("UEP_LOG_LEVEL"):
        env_overrides["log_level"] = os.getenv("UEP_LOG_LEVEL")

    if env_overrides:
        cfg = _apply_overrides_from_dict(cfg, env_overrides)

    return cfg


# Provide a module-level settings variable for backwards compatibility
settings = default_settings
