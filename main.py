"""Training script for ML model."""
import argparse

import petname

from logger import setup_logger
from trainer import train

parser = argparse.ArgumentParser()
parser.add_argument("--mode", help="Run mode (debug/prod)",
                    choices=["debug", "prod"], default="debug")
args = parser.parse_args()

debug = args.mode == "debug"

run_id = petname.generate(2)

setup_logger(debug,run_id)

if __name__ == "__main__":
    train()
