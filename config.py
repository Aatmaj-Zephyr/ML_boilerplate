# config.py
import tomllib
from types import SimpleNamespace

with open("./config.toml", "rb") as f:
    data = tomllib.load(f)

# Start with default config
_config_dict = data.get("default", {}).copy()

# Global config object
config = SimpleNamespace(**_config_dict)


def load_config(mode: str):
    """Load config with debug or prod mode.

    Args:
        mode (str): mode to load config for (debug/prod)
    """

    mode_overrides = data.get(mode, {})
    _config_dict.update(mode_overrides)

    # Update the existing global object instead of recreating it
    for key, value in mode_overrides.items():
        setattr(config, key, value)