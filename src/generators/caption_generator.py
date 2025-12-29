"""
Caption generator for social media posts
"""

import random
from .base_generator import BaseGenerator
from src.templates.content_templates import ContentTemplates


class CaptionGenerator(BaseGenerator):
    """Generates social media captions"""
    
    def __init__(self):
        super().__init__()
    
    def generate(self, context):
        """Generate a caption based on context"""
        if not self._validate_input(context):
            return "Please provide a valid topic."
        
        topic = context.get('topic', '')
        tone = context.get('tone', 'professional')
        audience = context.get('audience', 'general')
        goal = context.get('goal', 'educate')
        
        # Extract keywords and get main theme
        keywords = self._extract_keywords(topic, count=2)
        main_keyword = keywords[0] if keywords else topic.split()[0]
        
        # Get category
        category = self._get_category(topic)
        
        # Generate hook
        hook = self._generate_hook(topic, goal)
        
        # Generate body
        body = self._generate_body(topic, main_keyword, audience, category)
        
        # Generate CTA
        cta = self._generate_cta(goal)
        
        # Select template based on tone
        template = self._select_template(tone)
        
        # Fill template
        caption = template.format(
            hook=hook,
            body=body,
            cta=cta
        )
        
        return self._format_output(caption)
    
    def _generate_hook(self, topic, goal):
        """Generate opening hook"""
        topic_clean = self._capitalize(topic)
        
        hooks_by_goal = {
            "educate": [
                f"Here's what you need to know about {topic_clean}",
                f"Understanding {topic_clean} made simple",
                f"Let's talk about {topic_clean}",
                f"Everything you need to know about {topic_clean}"
            ],
            "inspire": [
                f"Transform your approach to {topic_clean}",
                f"Why {topic_clean} can change everything",
                f"The power of {topic_clean}",
                f"Ready to level up with {topic_clean}?"
            ],
            "entertain": [
                f"You won't believe what I learned about {topic_clean}",
                f"Plot twist: {topic_clean} is actually fascinating",
                f"Let me tell you about {topic_clean}",
                f"Okay, so {topic_clean}..."
            ],
            "sell": [
                f"Looking to improve your {topic_clean}?",
                f"The secret to better {topic_clean}",
                f"Struggling with {topic_clean}? Here's help",
                f"Transform your {topic_clean} today"
            ],
            "build community": [
                f"Who else is passionate about {topic_clean}?",
                f"Let's discuss {topic_clean} together",
                f"Calling all {topic_clean} enthusiasts",
                f"Join the conversation about {topic_clean}"
            ],
            "drive traffic": [
                f"The complete {topic_clean} guide (link in bio)",
                f"Everything about {topic_clean} you need to see",
                f"Deep dive into {topic_clean}",
                f"Your {topic_clean} resource is here"
            ],
            "increase engagement": [
                f"Quick question about {topic_clean}",
                f"What's your take on {topic_clean}?",
                f"Let me know your thoughts on {topic_clean}",
                f"Poll time: {topic_clean} - yes or no?"
            ]
        }
        
        goal_hooks = hooks_by_goal.get(goal.lower(), hooks_by_goal["educate"])
        return random.choice(goal_hooks)
    
    def _generate_body(self, topic, keyword, audience, category):
        """Generate main body content"""
        topic_clean = self._capitalize(topic)
        keyword_clean = keyword.lower()
        
        bodies = [
            f"This is your sign to start focusing on {keyword_clean}. The impact on {topic_clean} is undeniable, and the results speak for themselves.",
            f"After exploring {topic_clean}, one thing is clear: {keyword_clean} matters more than most realize. Here's why it's worth your attention.",
            f"The key to mastering {topic_clean}? Understanding {keyword_clean} at its core. Once you get this right, everything else falls into place.",
            f"Most people miss the connection between {keyword_clean} and {topic_clean}. Don't make that mistake.",
            f"If you're serious about {topic_clean}, you need to prioritize {keyword_clean}. It's that simple.",
            f"Three insights on {topic_clean}: clarity on {keyword_clean}, consistent action, and patience. That's the winning formula.",
            f"Real talk about {topic_clean}: {keyword_clean} is the foundation. Build from there and watch what happens."
        ]
        
        return random.choice(bodies)
    
    def _generate_cta(self, goal):
        """Generate call-to-action"""
        ctas_by_goal = {
            "educate": [
                "Save this for later!",
                "Share this with someone learning about this",
                "Bookmark for future reference"
            ],
            "inspire": [
                "Tag someone who needs to see this",
                "Share if this resonated with you",
                "Drop a 💙 if you're ready to take action"
            ],
            "entertain": [
                "Who can relate? 😂",
                "Tag a friend who needs to see this",
                "Comment if this is you"
            ],
            "sell": [
                "Link in bio to learn more",
                "DM me for details",
                "Ready to get started? Check the link"
            ],
            "build community": [
                "Join the conversation below",
                "What's your experience? Comment!",
                "Let's connect - follow for more"
            ],
            "drive traffic": [
                "Full guide in bio",
                "Link to resources in bio",
                "Click the link to read more"
            ],
            "increase engagement": [
                "Comment your thoughts!",
                "Drop your answer below",
                "Let me know what you think"
            ]
        }
        
        goal_ctas = ctas_by_goal.get(goal.lower(), ctas_by_goal["educate"])
        return random.choice(goal_ctas)
    
    def _select_template(self, tone):
        """Select template based on tone"""
        tone_lower = tone.lower()
        templates = ContentTemplates.CAPTION_TEMPLATES.get(
            tone_lower,
            ContentTemplates.CAPTION_TEMPLATES["professional"]
        )
        return random.choice(templates)