"""Training script for ML model."""
import argparse

import petname
from config import load_config
from logger import setup_logger, log
from trainer import train

parser = argparse.ArgumentParser()
parser.add_argument("--mode", help="Run mode (debug/prod)",
                    choices=["debug", "prod"], default="debug")
args = parser.parse_args()
load_config(args.mode)

debug = args.mode == "debug"

run_id = petname.generate(2)

setup_logger(run_id)

if __name__ == "__main__":
    log.info(f"Starting training with run_id: <red>{run_id}</red>")
    train()
