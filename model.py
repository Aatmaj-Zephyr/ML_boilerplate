"""Model architecture definition."""
from types import SimpleNamespace

from torch import nn
import torch


class myModel(nn.Module):
    """Model which does RL work."""

    def __init__(self, archparams: SimpleNamespace) -> None:
        """Initialize and define the layers."""
        super().__init__()
        self.archparams = archparams  # architectural parameters

        # modify this
        self.encoder = nn.Sequential(
            nn.Conv2d(1, 8, 3, padding=1, stride=4),
            nn.LeakyReLU(),
        )

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        """Forward pass of the model.
        Args:
            x: The input
        Returns:
            A tensor of shape (batch_size, 3 * num_circles) containing the predicted parameters for each circle.
        """

        # modify this
        x = self.encoder(x)

        return x
