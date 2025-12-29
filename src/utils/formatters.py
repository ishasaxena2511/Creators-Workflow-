"""
Formatting utilities for content output
"""


class Formatters:
    """Utilities for formatting content"""
    
    @staticmethod
    def add_line_breaks(text, max_line_length=80):
        """Add line breaks to long text"""
        if not text or len(text) <= max_line_length:
            return text
        
        words = text.split()
        lines = []
        current_line = []
        current_length = 0
        
        for word in words:
            if current_length + len(word) + 1 <= max_line_length:
                current_line.append(word)
                current_length += len(word) + 1
            else:
                lines.append(' '.join(current_line))
                current_line = [word]
                current_length = len(word)
        
        if current_line:
            lines.append(' '.join(current_line))
        
        return '\n'.join(lines)
    
    @staticmethod
    def count_characters(text):
        """Count characters in text"""
        if not text:
            return 0
        return len(text)
    
    @staticmethod
    def count_words(text):
        """Count words in text"""
        if not text:
            return 0
        return len(text.split())
    
    @staticmethod
    def truncate_text(text, max_length, suffix="..."):
        """Truncate text to max length"""
        if not text or len(text) <= max_length:
            return text
        
        return text[:max_length - len(suffix)] + suffix
    
    @staticmethod
    def insert_emoji(text, emoji, position="start"):
        """Insert emoji at specified position"""
        if not text:
            return emoji
        
        if position == "start":
            return f"{emoji} {text}"
        elif position == "end":
            return f"{text} {emoji}"
        else:
            return text
    
    @staticmethod
    def clean_whitespace(text):
        """Remove extra whitespace"""
        if not text:
            return ""
        
        # Remove leading/trailing whitespace
        text = text.strip()
        
        # Replace multiple spaces with single space
        import re
        text = re.sub(r'\s+', ' ', text)
        
        return text
    
    @staticmethod
    def capitalize_sentences(text):
        """Capitalize first letter of each sentence"""
        if not text:
            return ""
        
        sentences = text.split('. ')
        capitalized = [s[0].upper() + s[1:] if s else s for s in sentences]
        return '. '.join(capitalized)
    
    @staticmethod
    def format_hashtags(hashtags_list):
        """Format list of hashtags into string"""
        if not hashtags_list:
            return ""
        
        # Ensure all have # prefix
        formatted = []
        for tag in hashtags_list:
            if not tag.startswith('#'):
                formatted.append(f"#{tag}")
            else:
                formatted.append(tag)
        
        return ' '.join(formatted)
    
    @staticmethod
    def convert_to_markdown(text, heading_level=1):
        """Convert plain text to markdown format"""
        if not text:
            return ""
        
        markdown = '#' * heading_level + ' ' + text
        return markdown
    
    @staticmethod
    def add_bullets(items):
        """Convert list items to bullet points"""
        if not items:
            return ""
        
        bullets = [f"- {item}" for item in items]
        return '\n'.join(bullets)
    
    @staticmethod
    def format_timestamp():
        """Get formatted timestamp"""
        from datetime import datetime
        return datetime.now().strftime("%Y-%m-%d %H:%M:%S")