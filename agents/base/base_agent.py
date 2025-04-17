"""
Base Agent class for the WealthAutomation system.

This module defines the BaseAgent class that all specialized agents inherit from.
"""

import os
import json
import openai
from abc import ABC, abstractmethod
from ...utils.logger import log_info, log_error, setup_logger

# Set up a logger for the base agent
logger = setup_logger('base_agent')

class BaseAgent(ABC):
    """
    Base class for all agents in the WealthAutomation system.
    
    This abstract class defines the common interface and functionality
    that all specialized agents must implement.
    """
    
    def __init__(self, name="BaseAgent", model="gpt-4o"):
        self.name = name
        self.model = model
        self.api_key = os.environ.get('OPENAI_API_KEY')
        
        if not self.api_key:
            log_error(f"{self.name}: OpenAI API key not found in environment variables")
            raise ValueError("OpenAI API key not found in environment variables")
        
        openai.api_key = self.api_key
        log_info(f"{self.name} initialized with model: {self.model}")
    
    def _call_openai_api(self, prompt, system_message=None, temperature=0.7, max_tokens=2000):
        try:
            messages = []
            if system_message:
                messages.append({"role": "system", "content": system_message})
            messages.append({"role": "user", "content": prompt})
            
            log_info(f"{self.name}: Calling OpenAI API with model {self.model}")
            
            response = openai.ChatCompletion.create(
                model=self.model,
                messages=messages,
                temperature=temperature,
                max_tokens=max_tokens
            )
            
            return response.choices[0].message.content.strip()
            
        except Exception as e:
            log_error(f"{self.name}: Error calling OpenAI API: {str(e)}", exc_info=True)
            raise

    @abstractmethod
    def process(self, *args, **kwargs):
        pass
    
    def get_status(self):
        return {
            "name": self.name,
            "model": self.model,
            "status": "active"
        }
    
    def __str__(self):
        return f"{self.name} (using {self.model})"
