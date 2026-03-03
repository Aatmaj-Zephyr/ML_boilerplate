"""Training script for ML model."""
import argparse
import time

import petname
from helpers.config import load_config,config
from helpers.logger import setup_logger, log
from trainer import train
from helpers.telemetry_writer import telemetry_writer

parser = argparse.ArgumentParser()
parser.add_argument("--mode", help="Run mode (debug/prod)",
                    choices=["debug", "prod"], default="debug")
args = parser.parse_args()
load_config(args.mode)

debug = args.mode == "debug"

setup_logger()
telemetry_writer.setup_writer(
    fieldnames=["epoch", "train_loss", "val_loss"] # modify this as needed
)


if __name__ == "__main__":
    log.info(f"Starting training with run_id: <red>{config.runtime.RUN_ID}</red> at time: {config.runtime.START_TIME}")
    train()
