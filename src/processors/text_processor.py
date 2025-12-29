"""
Text processing utilities for keyword extraction and analysis
"""

import re
from collections import Counter


class TextProcessor:
    """Processes text input to extract keywords and analyze content"""
    
    STOP_WORDS = {
        'a', 'an', 'and', 'are', 'as', 'at', 'be', 'by', 'for', 'from',
        'has', 'he', 'in', 'is', 'it', 'its', 'of', 'on', 'that', 'the',
        'to', 'was', 'will', 'with', 'the', 'this', 'but', 'they', 'have',
        'had', 'what', 'when', 'where', 'who', 'which', 'why', 'how', 'all',
        'each', 'every', 'both', 'few', 'more', 'most', 'other', 'some', 'such',
        'or', 'own', 'same', 'so', 'than', 'too', 'very', 'can', 'just', 'should',
        'now', 'i', 'you', 'we', 'my', 'your', 'our', 'their', 'am', 'been', 'being'
    }
    
    def __init__(self):
        pass
    
    def clean_text(self, text):
        """Clean and normalize text input"""
        if not text:
            return ""
        
        # Convert to lowercase
        text = text.lower()
        
        # Remove special characters but keep spaces and hyphens
        text = re.sub(r'[^a-z0-9\s\-]', ' ', text)
        
        # Remove extra whitespace
        text = ' '.join(text.split())
        
        return text
    
    def extract_keywords(self, text, max_keywords=5):
        """Extract main keywords from text"""
        if not text:
            return []
        
        cleaned = self.clean_text(text)
        words = cleaned.split()
        
        # Handle single word input
        if len(words) == 1:
            return [words[0]]
        
        # Filter out stop words
        filtered_words = [word for word in words if word not in self.STOP_WORDS and len(word) > 2]
        
        # Handle case where all words are stop words
        if not filtered_words:
            filtered_words = [word for word in words if len(word) > 2]
        
        # Count word frequency
        word_freq = Counter(filtered_words)
        
        # Get top keywords
        top_keywords = [word for word, _ in word_freq.most_common(max_keywords)]
        
        # If still no keywords, return first word
        if not top_keywords and words:
            return [words[0]]
        
        return top_keywords
    
    def get_word_count(self, text):
        """Get word count of text"""
        if not text:
            return 0
        return len(text.split())
    
    def capitalize_first_letter(self, text):
        """Capitalize first letter of text"""
        if not text:
            return ""
        return text[0].upper() + text[1:] if len(text) > 1 else text.upper()
    
    def extract_phrases(self, text, phrase_length=2):
        """Extract common phrases (n-grams) from text"""
        if not text:
            return []
        
        cleaned = self.clean_text(text)
        words = [w for w in cleaned.split() if w not in self.STOP_WORDS]
        
        if len(words) < phrase_length:
            return [' '.join(words)] if words else []
        
        phrases = []
        for i in range(len(words) - phrase_length + 1):
            phrase = ' '.join(words[i:i + phrase_length])
            phrases.append(phrase)
        
        return phrases[:3]  # Return top 3 phrases
    
    def get_main_theme(self, text):
        """Get the main theme/subject from text"""
        keywords = self.extract_keywords(text, max_keywords=3)
        if keywords:
            return keywords[0]
        return self.clean_text(text).split()[0] if text else "topic"
    
    def expand_single_word(self, word):
        """Expand single word input with context variations"""
        if not word:
            return []
        
        word = word.lower().strip()
        variations = [
            word,
            f"{word} tips",
            f"{word} guide",
            f"{word} strategy",
            f"how to {word}",
            f"{word} ideas"
        ]
        return variations