from dlSegmentation.logger import logging
from dlSegmentation.exception import AppException
import sys

logging.info("Welcome to custom logging")


try:
    a = 4/"4"
except Exception as e:
    raise AppException(e, sys)