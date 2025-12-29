"""
Validation utilities for input and output
"""

import re


class Validators:
    """Utilities for validating input and output"""
    
    @staticmethod
    def validate_topic_input(topic, min_length=1, max_length=500):
        """Validate topic input"""
        if not topic:
            return False, "Topic cannot be empty"
        
        topic = topic.strip()
        
        if len(topic) < min_length:
            return False, f"Topic must be at least {min_length} character(s)"
        
        if len(topic) > max_length:
            return False, f"Topic must be less than {max_length} characters"
        
        return True, "Valid"
    
    @staticmethod
    def validate_caption_length(caption, min_length=20, max_length=300):
        """Validate caption length"""
        if not caption:
            return False, "Caption is empty"
        
        length = len(caption)
        
        if length < min_length:
            return False, f"Caption too short (min: {min_length})"
        
        if length > max_length:
            return False, f"Caption too long (max: {max_length})"
        
        return True, "Valid"
    
    @staticmethod
    def validate_tweet_length(tweet, max_length=280):
        """Validate tweet length"""
        if not tweet:
            return False, "Tweet is empty"
        
        if len(tweet) > max_length:
            return False, f"Tweet exceeds {max_length} characters"
        
        return True, "Valid"
    
    @staticmethod
    def validate_hashtags(hashtags, min_count=5, max_count=30):
        """Validate hashtag count"""
        if not hashtags:
            return False, "No hashtags provided"
        
        # Count hashtags
        count = hashtags.count('#')
        
        if count < min_count:
            return False, f"Too few hashtags (min: {min_count})"
        
        if count > max_count:
            return False, f"Too many hashtags (max: {max_count})"
        
        return True, "Valid"
    
    @staticmethod
    def contains_special_chars(text):
        """Check if text contains special characters"""
        if not text:
            return False
        
        pattern = r'[^a-zA-Z0-9\s]'
        return bool(re.search(pattern, text))
    
    @staticmethod
    def is_url(text):
        """Check if text is a URL"""
        if not text:
            return False
        
        url_pattern = r'https?://(?:www\.)?[-a-zA-Z0-9@:%._\+~#=]{1,256}\.[a-zA-Z0-9()]{1,6}\b(?:[-a-zA-Z0-9()@:%_\+.~#?&/=]*)'
        return bool(re.match(url_pattern, text))
    
    @staticmethod
    def sanitize_input(text):
        """Sanitize user input"""
        if not text:
            return ""
        
        # Remove leading/trailing whitespace
        text = text.strip()
        
        # Remove any HTML tags
        text = re.sub(r'<[^>]+>', '', text)
        
        # Remove excessive special characters
        text = re.sub(r'[^\w\s\-.,!?;:\'"()]', '', text)
        
        return text
    
    @staticmethod
    def validate_context(context):
        """Validate context dictionary"""
        if not context:
            return False, "Context is empty"
        
        required_keys = ['topic']
        
        for key in required_keys:
            if key not in context:
                return False, f"Missing required key: {key}"
        
        return True, "Valid"