import logging

def setup_logging():
    """
    Set up logging configuration.
    """
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
    logger = logging.getLogger(__name__)
    return logger

def log_error(logger, error):
    """
    Log an error message.
    """
    logger.error(f"An error occurred: {error}")
