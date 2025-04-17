"""
WordPress integration for the WealthAutomation system.

This module provides a utility class to publish content to WordPress via REST API.
"""

import os
import requests
from requests.auth import HTTPBasicAuth
from .logger import log_info, log_error

class WordPressIntegration:
    def __init__(self):
        self.base_url = os.getenv("WORDPRESS_API_URL")
        self.username = os.getenv("WORDPRESS_USERNAME")
        self.password = os.getenv("WORDPRESS_APP_PASSWORD")

        if not all([self.base_url, self.username, self.password]):
            raise ValueError("WordPress credentials are not fully set in environment variables.")

        self.auth = HTTPBasicAuth(self.username, self.password)

    def publish_post(self, title, content, status="publish"):
        url = f"{self.base_url}/wp-json/wp/v2/posts"
        headers = {
            "Content-Type": "application/json"
        }
        payload = {
            "title": title,
            "content": content,
            "status": status
        }

        try:
            log_info(f"Publishing post to WordPress: {title}")
            response = requests.post(url, headers=headers, json=payload, auth=self.auth)
            response.raise_for_status()
            log_info("Post published successfully.")
            return response.json()
        except requests.exceptions.RequestException as e:
            log_error(f"Failed to publish post: {e}", exc_info=True)
            raise
