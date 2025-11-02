from loguru import logger
import sys
import os
import json

class InterceptHandler:
    def __init__(self):
        self.levels = {
            "DEBUG": logger.debug,
            "INFO": logger.info,
            "WARNING": logger.warning,
            "ERROR": logger.error,
            "CRITICAL": logger.critical,
        }

    def emit(self, record):
        log_level = record["level"].name
        log_message = record["message"]
        if log_level in self.levels:
            self.levels[log_level](log_message)

def setup_logging():
    log_format = "<green>{time:YYYY-MM-DD HH:mm:ss}</green> | " \
                 "<level>{level: <8}</level> | " \
                 "<cyan>{name}</cyan>:<cyan>{function}</cyan>:<cyan>{line}</cyan> | " \
                 "<level>{message}</level>"
    
    logger.remove()
    logger.add(sys.stdout, format=log_format, level=os.getenv("LOG_LEVEL", "INFO"))

    # Optional: Add a JSON log file
    if os.getenv("JSON_LOG_FILE"):
        logger.add(os.getenv("JSON_LOG_FILE"), format=json.dumps, level="DEBUG", serialize=True)

setup_logging()