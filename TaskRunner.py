import logging


logging.basicConfig(
    filename="",
    format="{asctime} {levelname:<8} {message}"
)

logging.debug('This is a debug message')
logging.info('This is an info message')
logging.warning('This is a warning message')
logging.error('This is an error message')
logging.critical('This is a critical message')
logging.info("Application started")
