"""
Tweet generator for Twitter/X posts
"""

import random
from .base_generator import BaseGenerator
from src.templates.content_templates import ContentTemplates


class TweetGenerator(BaseGenerator):
    """Generates tweets optimized for Twitter/X"""
    
    def __init__(self):
        super().__init__()
        self.max_length = 280
    
    def generate(self, context):
        """Generate a tweet based on context"""
        if not self._validate_input(context):
            return "Share your insights and connect with your audience."
        
        topic = context.get('topic', '')
        tone = context.get('tone', 'professional')
        goal = context.get('goal', 'educate')
        
        # Extract keywords
        keywords = self._extract_keywords(topic, count=2)
        main_keyword = keywords[0] if keywords else topic.split()[0]
        
        # Generate hook
        hook = self._generate_hook(topic, goal)
        
        # Generate body
        body = self._generate_body(topic, main_keyword, tone)
        
        # Build tweet
        tweet = self._build_tweet(hook, body, tone)
        
        # Ensure length constraint
        tweet = self._enforce_length(tweet)
        
        return self._format_output(tweet)
    
    def _generate_hook(self, topic, goal):
        """Generate tweet hook"""
        topic_clean = self._capitalize(topic)
        
        hooks_by_goal = {
            "educate": [
                f"Key insight on {topic_clean}:",
                f"What you need to know about {topic_clean}:",
                f"Let's talk {topic_clean}:",
                f"Quick thread on {topic_clean}:"
            ],
            "inspire": [
                f"Transform your {topic_clean}:",
                f"Why {topic_clean} matters:",
                f"The power of {topic_clean}:",
                f"Level up your {topic_clean}:"
            ],
            "entertain": [
                f"Hot take on {topic_clean}:",
                f"Unpopular opinion about {topic_clean}:",
                f"Real talk: {topic_clean}",
                f"Nobody talks about {topic_clean}:"
            ],
            "sell": [
                f"Struggling with {topic_clean}?",
                f"The secret to {topic_clean}:",
                f"Master {topic_clean}:",
                f"Your {topic_clean} solution:"
            ],
            "build community": [
                f"Who else loves {topic_clean}?",
                f"Question for the {topic_clean} community:",
                f"Calling all {topic_clean} enthusiasts:",
                f"Let's discuss {topic_clean}:"
            ],
            "drive traffic": [
                f"Everything about {topic_clean} 🧵",
                f"The complete {topic_clean} guide:",
                f"Deep dive into {topic_clean}:",
                f"Your {topic_clean} roadmap:"
            ],
            "increase engagement": [
                f"Poll: What's your take on {topic_clean}?",
                f"Agree or disagree: {topic_clean}",
                f"Quick question about {topic_clean}:",
                f"Thoughts on {topic_clean}?"
            ]
        }
        
        goal_hooks = hooks_by_goal.get(goal.lower(), hooks_by_goal["educate"])
        return random.choice(goal_hooks)
    
    def _generate_body(self, topic, keyword, tone):
        """Generate tweet body"""
        bodies_professional = [
            f"Focus on {keyword}. It's the foundation of success.",
            f"{keyword} is underrated. Master it, master {topic}.",
            f"The best approach? Prioritize {keyword} first.",
            f"Most overlook {keyword}. Big mistake.",
            f"Key to {topic}: understand {keyword} deeply."
        ]
        
        bodies_casual = [
            f"Honestly? {keyword} changes everything.",
            f"Real talk: {keyword} is the move.",
            f"Everyone sleeps on {keyword}. Don't.",
            f"Pro tip: start with {keyword}.",
            f"{keyword} hits different when you get it right."
        ]
        
        bodies_inspirational = [
            f"Start with {keyword}. The rest follows.",
            f"Your journey begins with {keyword}.",
            f"{keyword} is your superpower. Use it.",
            f"Believe in {keyword}. Trust the process.",
            f"Master {keyword}. Transform everything."
        ]
        
        if tone.lower() == "casual":
            return random.choice(bodies_casual)
        elif tone.lower() in ["inspirational", "friendly"]:
            return random.choice(bodies_inspirational)
        else:
            return random.choice(bodies_professional)
    
    def _build_tweet(self, hook, body, tone):
        """Build complete tweet"""
        # Add emoji based on tone
        emoji = self._get_emoji(tone)
        
        tweet = f"{hook}\n\n{body}"
        
        if emoji and len(tweet) + len(emoji) + 1 < self.max_length:
            tweet = f"{emoji} {tweet}"
        
        return tweet
    
    def _get_emoji(self, tone):
        """Get emoji based on tone"""
        emoji_map = {
            "professional": "💡",
            "casual": "👀",
            "friendly": "💙",
            "inspirational": "✨",
            "educational": "📚",
            "humorous": "😂",
            "bold": "🔥"
        }
        return emoji_map.get(tone.lower(), "")
    
    def _enforce_length(self, tweet):
        """Ensure tweet fits within character limit"""
        if len(tweet) <= self.max_length:
            return tweet
        
        # Truncate and add ellipsis
        return tweet[:self.max_length - 3] + "..."