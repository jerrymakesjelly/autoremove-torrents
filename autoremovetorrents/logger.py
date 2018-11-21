# -*- coding:utf-8 -*-
# Logging System

import logging

LOG_FILE_PATH = 'autoremove.log'
OUTPUT_FORMAT = '%(asctime)s %(name)s %(levelname)s: %(message)s'
FILE_FORMAT = '%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s'
DATE_FORMAT = '%a, %d %b %Y %H:%M:%S'
FILE_LOG_LEVEL = logging.DEBUG
OUTPUT_LOG_LEVEL = logging.INFO

def register(name):
    # Configure logging
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)
    formatter = logging.Formatter(OUTPUT_FORMAT, datefmt=DATE_FORMAT)

    # Use FileHandler to output to file
    fh = logging.FileHandler(LOG_FILE_PATH)
    fh.setLevel(FILE_LOG_LEVEL)
    fh_formatter = logging.Formatter(FILE_FORMAT, datefmt=DATE_FORMAT)
    fh.setFormatter(fh_formatter)

    # Use StreamHandler to output to screen
    ch = logging.StreamHandler()
    ch.setLevel(OUTPUT_LOG_LEVEL)
    ch.setFormatter(formatter)

    # Add Handlers
    logger.addHandler(ch)
    logger.addHandler(fh)

    return logger