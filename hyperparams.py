"""Load hyperparameters from. toml file."""
import tomllib
from types import SimpleNamespace

with open("./hyperparameters.toml", "rb") as f:
    data = tomllib.load(f)

hyperparams = SimpleNamespace(**data["default"])
