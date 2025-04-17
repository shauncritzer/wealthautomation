"""
ConvertKit integration for the WealthAutomation system.

This module provides a utility class to interact with ConvertKit's API for
subscriber management, tagging, and form automation.
"""

import os
import requests
from .logger import log_info, log_error

class ConvertKitIntegration:
    def __init__(self):
        self.api_key = os.getenv("CONVERTKIT_API_KEY")
        self.form_id = os.getenv("CONVERTKIT_FORM_ID")
        self.base_url = "https://api.convertkit.com/v3"

        if not self.api_key or not self.form_id:
            raise ValueError("ConvertKit credentials not fully set in environment variables.")

    def add_subscriber(self, email, first_name=None, tags=None):
        url = f"{self.base_url}/forms/{self.form_id}/subscribe"
        payload = {
            "api_key": self.api_key,
            "email": email
        }

        if first_name:
            payload["first_name"] = first_name

        try:
            log_info(f"Subscribing user: {email}")
            response = requests.post(url, data=payload)
            response.raise_for_status()
            data = response.json()

            subscriber_id = data.get("subscription", {}).get("subscriber", {}).get("id")
            if subscriber_id and tags:
                self.apply_tags(subscriber_id, tags)

            return data
        except requests.exceptions.RequestException as e:
            log_error(f"Failed to subscribe user: {e}", exc_info=True)
            raise

    def apply_tags(self, subscriber_id, tags):
        for tag in tags:
            try:
                log_info(f"Applying tag '{tag}' to subscriber {subscriber_id}")
                tag_url = f"{self.base_url}/tags/{tag}/subscribe"
                payload = {
                    "api_key": self.api_key,
                    "subscriber_id": subscriber_id
                }
                response = requests.post(tag_url, data=payload)
                response.raise_for_status()
            except requests.exceptions.RequestException as e:
                log_error(f"Failed to apply tag '{tag}': {e}", exc_info=True)
