"""
Logger utility for all of EoC.
NEVER logs sensitive data, follows English-only, store-validation guideline.
"""
import logging

def get_logger(name="EoC"):
    logger = logging.getLogger(name)
    if not logger.handlers:
        handler = logging.StreamHandler()
        formatter = logging.Formatter('[%(levelname)s] %(asctime)s: %(message)s')
        handler.setFormatter(formatter)
        logger.addHandler(handler)
    logger.setLevel(logging.INFO)
    return logger