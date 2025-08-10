import logging
def setup_logger(name):
    logger=logging.getLogger(name)
    logger.setLevel(logging.INFO)
    return logger
