"""
Utility functions for logging in the WealthAutomation application.

This module provides logging functionality for the application.
"""

import logging
import os
import sys
from datetime import datetime

# Configure logging
def setup_logger(name, log_level=logging.INFO):
    """
    Set up a logger with the specified name and log level.
    
    Args:
        name (str): The name of the logger
        log_level (int): The logging level (default: logging.INFO)
        
    Returns:
        logging.Logger: The configured logger
    """
    # Create logs directory if it doesn't exist
    log_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'logs')
    os.makedirs(log_dir, exist_ok=True)
    
    # Create a logger
    logger = logging.getLogger(name)
    logger.setLevel(log_level)
    
    # Create handlers
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setLevel(log_level)
    
    # Create formatters
    formatter = logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    )
    
    # Add formatters to handlers
    console_handler.setFormatter(formatter)
    
    # Add handlers to logger
    logger.addHandler(console_handler)
    
    # Create file handler for important logs
    current_date = datetime.now().strftime('%Y-%m-%d')
    file_handler = logging.FileHandler(
        os.path.join(log_dir, f'{name}_{current_date}.log')
    )
    file_handler.setLevel(log_level)
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)
    
    return logger

# Create a default application logger
app_logger = setup_logger('wealthautomation')

def log_info(message):
    """Log an info message."""
    app_logger.info(message)

def log_error(message, exc_info=None):
    """Log an error message."""
    if exc_info:
        app_logger.error(message, exc_info=exc_info)
    else:
        app_logger.error(message)

def log_warning(message):
    """Log a warning message."""
    app_logger.warning(message)

def log_debug(message):
    """Log a debug message."""
    app_logger.debug(message)
