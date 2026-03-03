"""Training code goes here"""
from helpers.hyperparams import hyperparams
from helpers.telemetry_writer import telemetry_writer
from helpers.logger import log
# from model import *


def train() -> None:
    """Train the model."""
    log.debug('In the training function')
    for epoch in range(hyperparams.NUM_EPOCHS):
        telemetry_writer.log(epoch=epoch, train_loss=0.5, val_loss=0.6)