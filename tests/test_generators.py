"""
Tests for content generators
"""

import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.generators.caption_generator import CaptionGenerator
from src.generators.hashtag_generator import HashtagGenerator
from src.generators.tweet_generator import TweetGenerator
from src.generators.reel_generator import ReelGenerator
from src.generators.blog_generator import BlogGenerator


def create_test_context(topic="productivity"):
    """Create test context"""
    return {
        "topic": topic,
        "tone": "professional",
        "audience": "general",
        "goal": "educate"
    }


def test_caption_generator():
    """Test caption generation"""
    generator = CaptionGenerator()
    context = create_test_context()
    
    caption = generator.generate(context)
    
    assert caption is not None
    assert len(caption) > 0
    assert "productivity" in caption.lower() or "topic" in caption.lower()
    print("✓ Caption generation works")


def test_caption_single_word():
    """Test caption with single word"""
    generator = CaptionGenerator()
    context = create_test_context("ai")
    
    caption = generator.generate(context)
    
    assert caption is not None
    assert len(caption) > 0
    print("✓ Caption single word works")


def test_hashtag_generator():
    """Test hashtag generation"""
    generator = HashtagGenerator()
    context = create_test_context("technology")
    
    hashtags = generator.generate(context)
    
    assert hashtags is not None
    assert "#" in hashtags
    assert hashtags.count("#") >= 5
    print("✓ Hashtag generation works")


def test_tweet_generator():
    """Test tweet generation"""
    generator = TweetGenerator()
    context = create_test_context()
    
    tweet = generator.generate(context)
    
    assert tweet is not None
    assert len(tweet) > 0
    assert len(tweet) <= 280
    print("✓ Tweet generation works")


def test_tweet_length_constraint():
    """Test tweet length constraint"""
    generator = TweetGenerator()
    context = create_test_context("artificial intelligence machine learning deep learning")
    
    tweet = generator.generate(context)
    
    assert len(tweet) <= 280
    print("✓ Tweet length constraint works")


def test_reel_generator():
    """Test reel generation"""
    generator = ReelGenerator()
    context = create_test_context()
    
    reel = generator.generate(context)
    
    assert reel is not None
    assert len(reel) > 0
    assert "Hook" in reel or "hook" in reel
    assert "Scene" in reel or "scene" in reel
    print("✓ Reel generation works")


def test_blog_generator():
    """Test blog generation"""
    generator = BlogGenerator()
    context = create_test_context()
    
    blog = generator.generate(context)
    
    assert blog is not None
    assert len(blog) > 0
    assert "Introduction" in blog or "introduction" in blog
    assert "Conclusion" in blog or "conclusion" in blog
    print("✓ Blog generation works")


def test_blog_structure():
    """Test blog structure"""
    generator = BlogGenerator()
    context = create_test_context("fitness")
    
    blog = generator.generate(context)
    
    assert "##" in blog  # Check for section headings
    assert "-" in blog   # Check for bullet points
    print("✓ Blog structure works")


def test_empty_input():
    """Test empty input handling"""
    generator = CaptionGenerator()
    context = {"topic": "", "tone": "professional", "audience": "general", "goal": "educate"}
    
    caption = generator.generate(context)
    
    assert caption is not None
    print("✓ Empty input handling works")


def run_all_generator_tests():
    """Run all generator tests"""
    print("\n=== Running Generator Tests ===\n")
    
    test_caption_generator()
    test_caption_single_word()
    test_hashtag_generator()
    test_tweet_generator()
    test_tweet_length_constraint()
    test_reel_generator()
    test_blog_generator()
    test_blog_structure()
    test_empty_input()
    
    print("\n=== All Generator Tests Passed ===\n")


if __name__ == "__main__":
    run_all_generator_tests()