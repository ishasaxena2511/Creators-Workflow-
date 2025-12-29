"""
Configuration file for Creators Workflow AI
Contains app-wide constants and settings
"""

# App Metadata
APP_NAME = "Creators Workflow AI"
APP_DESCRIPTION = "Transform your ideas into ready-to-publish content"
VERSION = "1.0.0"

# Content Type Configurations
CAPTION_CONFIG = {
    "min_length": 50,
    "max_length": 200,
    "include_emojis": True,
    "include_cta": True
}

HASHTAG_CONFIG = {
    "min_count": 10,
    "max_count": 15,
    "mix_popular": True,
    "mix_niche": True
}

TWEET_CONFIG = {
    "max_length": 280,
    "include_emojis": True,
    "thread_mode": False
}

REEL_CONFIG = {
    "structure": ["hook", "body", "cta"],
    "include_scenes": True,
    "max_scenes": 3
}

BLOG_CONFIG = {
    "min_sections": 3,
    "max_sections": 5,
    "include_intro": True,
    "include_conclusion": True,
    "seo_optimized": True
}

# Tone Options
TONE_OPTIONS = [
    "Professional",
    "Casual",
    "Friendly",
    "Inspirational",
    "Educational",
    "Humorous",
    "Bold"
]

# Audience Options
AUDIENCE_OPTIONS = [
    "General",
    "Entrepreneurs",
    "Students",
    "Professionals",
    "Creators",
    "Tech Enthusiasts",
    "Fitness Lovers",
    "Travelers"
]

# Goal Options
GOAL_OPTIONS = [
    "Educate",
    "Inspire",
    "Entertain",
    "Sell",
    "Build Community",
    "Drive Traffic",
    "Increase Engagement"
]

# UI Settings
DEFAULT_TONE = "Professional"
DEFAULT_AUDIENCE = "General"
DEFAULT_GOAL = "Educate"

# Input Validation
MIN_INPUT_LENGTH = 1
MAX_INPUT_LENGTH = 500

# Categories for Topic Analysis
CATEGORIES = [
    "Technology",
    "Business",
    "Lifestyle",
    "Health & Fitness",
    "Travel",
    "Food",
    "Education",
    "Entertainment",
    "Finance",
    "General"
]