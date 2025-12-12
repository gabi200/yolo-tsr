import logging
import os
from logging.handlers import RotatingFileHandler

current_dir = os.path.dirname(os.path.abspath(__file__))

# --- Configuration ---
LOG_DIR = os.path.join(current_dir, "..", "..", "logs")
LOG_FILE_NAME = "app_activity.log"
MAX_LOG_SIZE = 5 * 1024 * 1024  # 5 MB
BACKUP_COUNT = 3  # Keep 3 backup files (app.log.1, app.log.2, etc.)


def get_logger(module_name):
    """
    Configures and returns a logger instance for the specific module.

    Usage:
        from logger import get_logger
        logger = get_logger(__name__)
        logger.info("Message")
    """

    # 1. Create the logs directory if it doesn't exist
    if not os.path.exists(LOG_DIR):
        try:
            os.makedirs(LOG_DIR)
        except OSError as e:
            print(f"Error creating log directory: {e}")
            return logging.getLogger(module_name)  # Return basic logger fallback

    # 2. Get the logger for the specific module name
    logger = logging.getLogger(module_name)
    logger.setLevel(
        logging.DEBUG
    )  # Capture ALL levels globally (handlers filter them later)

    # 3. Prevent adding duplicate handlers if get_logger is called multiple times
    if not logger.hasHandlers():
        # --- Formatter ---
        # Format: [Time] [Level] [Module]: Message
        log_formatter = logging.Formatter(
            "%(asctime)s | %(levelname)-8s | %(name)-15s | %(message)s",
            datefmt="%Y-%m-%d %H:%M:%S",
        )

        # --- Handler 1: File (Rotates after 5MB) ---
        log_path = os.path.join(LOG_DIR, LOG_FILE_NAME)
        file_handler = RotatingFileHandler(
            log_path, maxBytes=MAX_LOG_SIZE, backupCount=BACKUP_COUNT, encoding="utf-8"
        )
        file_handler.setLevel(
            logging.DEBUG
        )  # Save everything to file (DEBUG, INFO, WARN, ERROR)
        file_handler.setFormatter(log_formatter)

        # --- Handler 2: Console (Standard Output) ---
        console_handler = logging.StreamHandler()
        console_handler.setLevel(
            logging.INFO
        )  # Only show INFO and above in console to keep it clean
        console_handler.setFormatter(log_formatter)

        # --- Add Handlers ---
        logger.addHandler(file_handler)
        logger.addHandler(console_handler)

        # Prevent logs from propagating to the root logger (avoids double printing)
        logger.propagate = False

    return logger


# Example of how it works if you run this file directly
if __name__ == "__main__":
    log = get_logger("TestModule")
    log.debug("This is a debug message (File only)")
    log.info("This is an info message (File + Console)")
    log.warning("This is a warning!")
    log.error("This is an error!")
    print(f"Check the '{LOG_DIR}' folder for the log file.")
