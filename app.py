"""
Main application module for the WealthAutomation system.

This module initializes the Flask application and registers all components.
"""

from flask import Flask, render_template, request
import os

# Import components
from routes import register_blueprints
from utils import log_info, log_error
from agents import agent_manager

def create_app():
    """
    Create and configure the Flask application.
    
    Returns:
        Flask: The configured Flask application
    """
    # Create Flask app
    app = Flask(__name__)
    
    # Register blueprints
    register_blueprints(app)
    
    # Log application startup
    log_info("WealthAutomation application initialized")
    
    return app

# Create the application instance
app = create_app()

# Run the application if executed directly
if __name__ == "__main__":
    host = os.environ.get('HOST', '0.0.0.0')
    port = int(os.environ.get('PORT', 8080))
    debug = os.environ.get('DEBUG', 'False').lower() == 'true'
    
    log_info(f"Starting WealthAutomation application on {host}:{port}")
    app.run(host=host, port=port, debug=debug)
