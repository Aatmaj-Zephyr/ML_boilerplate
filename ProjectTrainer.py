"""
Your project specific implementation of the TrainerBase class.
This is where you implement the actual training loop and any project-specific logic.
"""
import time

from TrainerBase import TrainerBase
from model import myModel


class ProjectTrainer(TrainerBase):
    """Project specific trainer class that inherits from TrainerBase. Implement the train method with your training logic."""

    def __init__(self) -> None:
        """Initialize the ProjectTrainer. You can add any project-specific initialization here."""
        self.telemetry_fieldnames = [
            "epoch", "train_loss", "val_loss"]  # modify this as needed
        super().__init__()  # Call the base class initializer
        self.model = myModel(self.hyperparams)

    def load_database(self) -> None:
        """Load the database."""
        ...  # Implement database loading logic here if needed

    def train(self) -> None:
        """Implement your training logic here."""

        self.log.debug('In the training function')
        for epoch in range(self.hyperparams.NUM_EPOCHS):

            if epoch % self.config.TELEMETRY_INTERVAL == 0:
                self.telemetry_writer.log(
                    epoch=epoch, train_loss=0.5, val_loss=0.6)
                execution_time = time.time() - self.config.runtime.START_TIME
                execution_time_formatted = time.strftime(
                    "%H:%M:%S", time.gmtime(execution_time))
                self.log.info(
                    f"Epoch: {epoch}, Elapsed time: {execution_time_formatted}")
