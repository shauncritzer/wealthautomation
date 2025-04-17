"""
Routes package initialization.

This package contains all the route definitions for the Flask application.
"""

from flask import Blueprint

# Create blueprints
main_bp = Blueprint('main', __name__)
content_bp = Blueprint('content', __name__)
api_bp = Blueprint('api', __name__)
wordpress_bp = Blueprint('wordpress', __name__, url_prefix='/wordpress')
convertkit_bp = Blueprint('convertkit', __name__, url_prefix='/convertkit')
monitoring_bp = Blueprint('monitoring', __name__, url_prefix='/monitoring')

# Import route modules
from . import main_routes
from . import content_routes
from . import api_routes
from . import wordpress_routes
from . import convertkit_routes
from . import monitoring_routes

def register_blueprints(app):
    """Register all blueprints with the Flask application."""
    app.register_blueprint(main_bp)
    app.register_blueprint(content_bp, url_prefix='/content')
    app.register_blueprint(api_bp, url_prefix='/api')
    app.register_blueprint(wordpress_bp)
    app.register_blueprint(convertkit_bp)
    app.register_blueprint(monitoring_bp)
    
    return app
