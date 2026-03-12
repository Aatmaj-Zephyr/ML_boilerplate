"""Training script for ML model."""
import argparse
from typing import Any
import torch

from helpers.config import load_config
from helpers.logger import setup_logger
from helpers.telemetry_writer import TelemetryWriter
from helpers.hyperparams import load_hyperparams


class TrainerBase():
    """Base class for training ML models. Handles configuration, logging, and telemetry setup."""

    def __init__(self) -> None:
        """Initialize."""
        self.config_file = "./config.toml"
        self.hyperparams_file = "./hyperparameters.toml"
        self.telemetry_log_directory = "./telemetry_logs"
        self.telemetry_fieldnames: list[str]
        assert self.telemetry_fieldnames is not None, "telemetry_fieldnames must be defined in the subclass before calling super().__init__()"
        self._setup()

    def load_database(self) -> Any:
        """Load the database. Implement this in subclass if needed."""
        raise NotImplementedError(
            "Subclasses can implement this method to load the database if needed.")

    def _setup(self) -> None:
        """Set up configuration, logging, and telemetry."""

        parser = argparse.ArgumentParser()
        parser.add_argument("--mode", help="Run mode (debug/prod)",
                            choices=["debug", "prod"], default="debug")
        args = parser.parse_args()
        self.config = load_config(args.mode, self.config_file)
        self.hyperparams = load_hyperparams(self.hyperparams_file)
        self.log = setup_logger(self.config)
        self.telemetry_writer = TelemetryWriter(
            fieldnames=self.telemetry_fieldnames, directory=self.telemetry_log_directory, config=self.config
        )

        if self.config.IS_DEBUG_TORCH:
            # Note: If using DDP with torch.multiprocessing.spawn, anomaly detection must
            # be enabled inside each worker process, not only in the main file.
            torch.autograd.set_detect_anomaly(True)
            torch.set_warn_always(True)

        self.log.info(
            f"Starting training with run_id: <red>{self.config.runtime.RUN_ID}</red> at time: {self.config.runtime.START_TIME}")

    def train(self) -> None:
        """Implement this in subclass."""
        raise NotImplementedError(
            "Subclasses must implement the train method.")
