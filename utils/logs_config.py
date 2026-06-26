import logging
from logging.handlers import RotatingFileHandler
from pathlib import Path

LOG_DIR = Path("logs")
LOG_DIR.mkdir(exist_ok=True)

handler = RotatingFileHandler(
    LOG_DIR / "nmap_engine.log",
    maxBytes=4 * 1024 * 1024,
    backupCount=4
)
logging.basicConfig(
    level=logging.INFO,
    handlers=[handler],
    format="%(asctime)s - %(name)s - %(message)s"
)

def get_logger():
    return logging.getLogger(__name__)