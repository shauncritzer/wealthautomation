"""
Main routes for the WealthAutomation application.

This module contains the main routes for the application, including
the home page, dashboard, and other primary user interfaces.
"""

from flask import render_template, request, jsonify
from . import main_bp

@main_bp.route('/')
def index():
    """Render the home page."""
    return render_template('index.html')

@main_bp.route('/dashboard')
def dashboard():
    """Render the dashboard page."""
    return render_template('dashboard.html')

@main_bp.route('/status')
def status():
    """Return the system status."""
    return jsonify({
        'status': 'online',
        'version': '1.0.0',
        'services': {
            'content_engine': 'active',
            'shorts_engine': 'active',
            'cta_engine': 'active'
        }
    })
