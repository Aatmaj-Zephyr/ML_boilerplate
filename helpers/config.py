"""File to load config from config.toml and provide a global config object. No need to modify this file."""

import time
import tomllib
from types import SimpleNamespace

import petname


def load_config(mode: str, config_file: str) -> SimpleNamespace:
    """Load config with debug or prod mode.
    Args:
        mode (str): mode to load config for (debug/prod)
        config_file (str): path to the config file
    Returns:
        SimpleNamespace: config object with attributes corresponding to config keys
    """

    with open(config_file, "rb") as f:
        data = tomllib.load(f)

    # Start with default config
    _config_dict = data.get("default", {}).copy()

    config = SimpleNamespace(**_config_dict)

    # Globals to store runtime information like start time, run id, etc.
    config.runtime = SimpleNamespace(
        START_TIME=None,
        RUN_ID=None,
    )

    config.runtime.RUN_ID = petname.generate(2)
    config.runtime.START_TIME = time.time()
    mode_overrides = data.get(mode, {})
    _config_dict.update(mode_overrides)

    # Update the existing global object instead of recreating it
    for key, value in mode_overrides.items():
        setattr(config, key, value)

    return config
