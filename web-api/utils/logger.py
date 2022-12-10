
import logging

_logger = logging.getLogger('uvicorn')


def info(message: str):
    _logger.info(message)


def warn(message: str):
    _logger.warn(message)


def get_logger():
    return _logger
