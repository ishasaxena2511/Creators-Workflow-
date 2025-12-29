"""
Hashtag generator for social media posts
"""

import random
from .base_generator import BaseGenerator
from data.hashtag_database import HASHTAG_DATABASE


class HashtagGenerator(BaseGenerator):
    """Generates relevant hashtags for content"""
    
    def __init__(self):
        super().__init__()
        self.min_hashtags = 10
        self.max_hashtags = 15
    
    def generate(self, context):
        """Generate hashtags based on context"""
        if not self._validate_input(context):
            return "#content #socialmedia #creator"
        
        topic = context.get('topic', '')
        
        # Get category
        category = self._get_category(topic)
        
        # Extract keywords
        keywords = self._extract_keywords(topic, count=3)
        
        # Get hashtags
        hashtags = self._get_category_hashtags(category)
        hashtags.extend(self._get_keyword_hashtags(keywords))
        hashtags.extend(self._get_general_hashtags())
        
        # Remove duplicates and limit count
        unique_hashtags = list(dict.fromkeys(hashtags))
        selected_hashtags = unique_hashtags[:self.max_hashtags]
        
        # Format output
        return " ".join(selected_hashtags)
    
    def _get_category_hashtags(self, category):
        """Get hashtags for specific category"""
        category_lower = category.lower().replace(" ", "")
        
        # Get from database
        category_tags = HASHTAG_DATABASE.get(category_lower, [])
        
        # Select random subset
        if len(category_tags) > 8:
            return random.sample(category_tags, 8)
        return category_tags
    
    def _get_keyword_hashtags(self, keywords):
        """Generate hashtags from keywords"""
        hashtags = []
        for keyword in keywords:
            # Clean keyword
            clean_keyword = keyword.replace(" ", "").replace("-", "")
            if len(clean_keyword) > 2:
                hashtags.append(f"#{clean_keyword}")
                
                # Add common variations
                if len(clean_keyword) > 4:
                    hashtags.append(f"#{clean_keyword}tips")
        
        return hashtags[:4]
    
    def _get_general_hashtags(self):
        """Get general engagement hashtags"""
        general = HASHTAG_DATABASE.get("general", [])
        if len(general) > 3:
            return random.sample(general, 3)
        return general