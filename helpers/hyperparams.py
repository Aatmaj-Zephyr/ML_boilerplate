"""Load hyperparameters from the toml file. No need to modify this file."""
import tomllib
from types import SimpleNamespace

def load_hyperparams(hyperparams_file: str) -> SimpleNamespace:
    """Load hyperparameters from the toml file.
    Args:
        hyperparams_file (str): path to the hyperparameters file
    Returns:
        SimpleNamespace: hyperparams object
    """

    with open(hyperparams_file, "rb") as f:
        data = tomllib.load(f)

    hyperparams = SimpleNamespace(**data["default"])
    return hyperparams
