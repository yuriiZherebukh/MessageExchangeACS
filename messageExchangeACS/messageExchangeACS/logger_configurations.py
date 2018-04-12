"""
This module contains configuration for logging
"""

import logging


def init(config_file: str, level: str):
    """
    Initialize logging into file with specific level

    :param config_file: File to write logs
    :param level: Log level
    :return: None
    """
    logger = logging.getLogger()
    formatter = logging.Formatter("%(pathname)s : %(asctime)s : %(levelname)s : Function(%(funcName)s) \t %(message)s")
    file_handler = logging.FileHandler(config_file)
    file_handler.setFormatter(formatter)
    file_handler.setLevel(level)
    logger.handlers = [file_handler]
