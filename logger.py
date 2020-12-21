# logger.py
import logging
import os


logging.basicConfig(level=os.getenv("LOGLEVEL", "INFO"))

info = logging.info
debug = logging.debug
