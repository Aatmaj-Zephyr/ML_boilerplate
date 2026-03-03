"""Setup logger for the project."""
import sys
from loguru import logger
from config import config

log = logger.opt(colors=True)

def setup_logger(run_id: str) -> None:
    """
    Configure logger using explicit config object.
    Args:
    run_id (str): Unique identifier for the current run, used in log formatting.
    """
    logger.remove()

    LOG_FORMAT = (
        f"[{run_id}] "
        "<cyan>{time:YYYY-MM-DD HH:mm:ss}</cyan> | "
        "<level>{level}</level> | "
        "<cyan>{name}</cyan>:<cyan>{line}</cyan> - "
        "{message}"
    )

    level = "DEBUG" if config.IS_DEBUG else "INFO"

    # Console handler
    logger.add(
        sys.stdout,
        level=level,
        format=LOG_FORMAT,
        colorize=True,
        
    )

    # File handler
    logger.add(
        config.DEBUG_LOG_FILE_PATH,
        level=level,
        format=LOG_FORMAT,
        rotation="10 MB",
        colorize=False
    )
    
