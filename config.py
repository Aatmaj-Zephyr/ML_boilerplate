"""Load hyperparameters from. toml file."""
import tomllib
from types import SimpleNamespace

with open("./config.toml", "rb") as f:
    data = tomllib.load(f)

config = SimpleNamespace(**data["default"])
