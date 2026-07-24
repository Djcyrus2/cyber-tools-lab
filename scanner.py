import logging
import os
from datetime import datetime

# Create log folder
if not os.path.exists("logs"):
    os.makedirs("logs")

# Logging setup
logging.basicConfig(
    filename="logs/scanner.log",
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s"
)

def log(message):
    logging.info(message)

def log_error(message):
    logging.error(message)