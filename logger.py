"""Setup logger for the project."""
import sys
from loguru import logger
from config import config

log = logger


def setup_logger(debug_mode: bool, run_id: str) -> None:
    """
    Configure logger using explicit config object.
    Args:
    debug_mode (bool): Whether to set log level to DEBUG or INFO.
    run_id (str): Unique identifier for the current run, used in log formatting.
    """
    logger.remove()

    LOG_FORMAT = (
        f"[{run_id}] "
        "<green>{time:YYYY-MM-DD HH:mm:ss}</green> | "
        "<level>{level}</level> | "
        "<cyan>{name}</cyan>:<cyan>{line}</cyan> - "
        "{message}"
    )

    level = "DEBUG" if debug_mode else "INFO"

    # Console handler
    logger.add(
        sys.stdout,
        level=level,
        format=LOG_FORMAT,
        colorize=True
    )

    # File handler
    logger.add(
        config.debug_log_file,
        level=level,
        format=LOG_FORMAT,
        rotation="10 MB",
        colorize=False
    )
