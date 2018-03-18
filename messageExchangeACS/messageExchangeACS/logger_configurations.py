"""
This module contains configuration for logging
"""

import os
import logging

PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))
LOG_DIR = os.path.join(PROJECT_ROOT, '..', 'logs')


LOG_FILE = "requests.log"

logging.basicConfig(
    level=logging.DEBUG,
    format="%(pathname)s : %(asctime)s : %(levelname)s : Function(%(funcName)s) \t %(message)s",
    filename="{}//{}".format(LOG_DIR, LOG_FILE))
