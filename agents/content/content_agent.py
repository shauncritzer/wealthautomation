"""
Enhanced ContentAgent with improved WordPress integration.

This module updates the ContentAgent class to use the dedicated WordPress integration.
"""

import os
from ..base.base_agent import BaseAgent
from ...utils.logger import log_info, log_warning, setup_logger
from ...utils.wordpress_integration import WordPressIntegration

# Set up a logger for the content agent
logger = setup_logger('content_agent')

class ContentAgent(BaseAgent):
    """
    Agent responsible for generating and managing content.
    
    This agent handles the creation of various types of content,
    including articles, blog posts, and product reviews.
    """
    
    def __init__(self, model="gpt-4o"):
        super().__init__(name="ContentAgent", model=model)
        
        try:
            self.wp = WordPressIntegration()
            self.wp_enabled = True
            log_info("WordPress integration enabled for ContentAgent")
        except ValueError as e:
            self.wp_enabled = False
            log_warning(f"WordPress integration disabled: {str(e)}")
        
        log_info("ContentAgent initialized")
    
    def generate_content(self, topic, content_type="article", keywords=None):
        prompt = f"Write a {content_type} about '{topic}'."
        if keywords:
            prompt += f" Include these keywords: {', '.join(keywords)}."
        
        return self._call_openai_api(prompt)
    
    def publish_to_wordpress(self, title, content):
        if not self.wp_enabled:
            raise RuntimeError("WordPress integration is disabled.")
        return self.wp.publish_post(title, content)
    
    def process(self, topic, content_type="article", keywords=None):
        log_info(f"Processing content request for topic: {topic}, type: {content_type}")
        content = self.generate_content(topic, content_type, keywords)
        
        post_result = None
        if self.wp_enabled:
            post_result = self.publish_to_wordpress(title=topic, content=content)
        
        return {
            "topic": topic,
            "content_type": content_type,
            "content": content,
            "wordpress_result": post_result
        }
