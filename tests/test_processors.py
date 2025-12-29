"""
Tests for text processors and topic analyzers
"""

import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.processors.text_processor import TextProcessor
from src.processors.topic_analyzer import TopicAnalyzer


def test_text_processor_clean():
    """Test text cleaning"""
    processor = TextProcessor()
    
    text = "Hello World! This is a TEST."
    cleaned = processor.clean_text(text)
    
    assert cleaned == "hello world this is a test"
    print("✓ Text cleaning works")


def test_text_processor_keywords():
    """Test keyword extraction"""
    processor = TextProcessor()
    
    text = "artificial intelligence and machine learning"
    keywords = processor.extract_keywords(text, max_keywords=3)
    
    assert len(keywords) > 0
    assert "artificial" in keywords or "intelligence" in keywords
    print("✓ Keyword extraction works")


def test_text_processor_single_word():
    """Test single word input"""
    processor = TextProcessor()
    
    text = "productivity"
    keywords = processor.extract_keywords(text)
    
    assert len(keywords) == 1
    assert keywords[0] == "productivity"
    print("✓ Single word handling works")


def test_topic_analyzer_categorization():
    """Test topic categorization"""
    analyzer = TopicAnalyzer()
    
    tech_topic = "artificial intelligence and machine learning"
    category = analyzer.categorize_topic(tech_topic)
    
    assert category == "technology"
    print("✓ Topic categorization works")


def test_topic_analyzer_business():
    """Test business categorization"""
    analyzer = TopicAnalyzer()
    
    business_topic = "startup marketing strategy"
    category = analyzer.categorize_topic(business_topic)
    
    assert category == "business"
    print("✓ Business categorization works")


def test_topic_analyzer_single_word():
    """Test single word detection"""
    analyzer = TopicAnalyzer()
    
    assert analyzer.is_single_word("productivity") == True
    assert analyzer.is_single_word("machine learning") == False
    print("✓ Single word detection works")


def test_topic_analyzer_confidence():
    """Test confidence scoring"""
    analyzer = TopicAnalyzer()
    
    topic = "fitness workout routine"
    confidence = analyzer.get_category_confidence(topic)
    
    assert 0 <= confidence <= 1
    print("✓ Confidence scoring works")


def run_all_processor_tests():
    """Run all processor tests"""
    print("\n=== Running Processor Tests ===\n")
    
    test_text_processor_clean()
    test_text_processor_keywords()
    test_text_processor_single_word()
    test_topic_analyzer_categorization()
    test_topic_analyzer_business()
    test_topic_analyzer_single_word()
    test_topic_analyzer_confidence()
    
    print("\n=== All Processor Tests Passed ===\n")


if __name__ == "__main__":
    run_all_processor_tests()