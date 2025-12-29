"""
Data module for static content databases
"""

from .hashtag_database import HASHTAG_DATABASE
from .keywords import CATEGORY_KEYWORDS, ACTION_VERBS, POWER_WORDS
from .sentence_structures import HOOK_STRUCTURES, CTA_STRUCTURES, TRANSITION_PHRASES

__all__ = [
    'HASHTAG_DATABASE',
    'CATEGORY_KEYWORDS',
    'ACTION_VERBS',
    'POWER_WORDS',
    'HOOK_STRUCTURES',
    'CTA_STRUCTURES',
    'TRANSITION_PHRASES'
]
