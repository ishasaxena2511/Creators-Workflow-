"""
Base generator class for all content generators
"""

from abc import ABC, abstractmethod
from src.processors.text_processor import TextProcessor
from src.processors.topic_analyzer import TopicAnalyzer


class BaseGenerator(ABC):
    """Abstract base class for content generators"""
    
    def __init__(self):
        self.text_processor = TextProcessor()
        self.topic_analyzer = TopicAnalyzer()
    
    @abstractmethod
    def generate(self, context):
        """Generate content based on context"""
        pass
    
    def _validate_input(self, context):
        """Validate input context"""
        if not context or 'topic' not in context:
            return False
        
        topic = context.get('topic', '').strip()
        if not topic:
            return False
        
        return True
    
    def _extract_keywords(self, text, count=3):
        """Extract keywords from text"""
        return self.text_processor.extract_keywords(text, max_keywords=count)
    
    def _get_category(self, text):
        """Get topic category"""
        return self.topic_analyzer.categorize_topic(text)
    
    def _capitalize(self, text):
        """Capitalize text"""
        return self.text_processor.capitalize_first_letter(text)
    
    def _clean_text(self, text):
        """Clean text"""
        return self.text_processor.clean_text(text)
    
    def _format_output(self, content):
        """Format output content"""
        return content.strip()