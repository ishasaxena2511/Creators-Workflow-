"""
Reel idea generator for short-form video content
"""

import random
from .base_generator import BaseGenerator
from src.templates.content_templates import ContentTemplates


class ReelGenerator(BaseGenerator):
    """Generates Instagram/TikTok reel concepts"""
    
    def __init__(self):
        super().__init__()
    
    def generate(self, context):
        """Generate a reel idea based on context"""
        if not self._validate_input(context):
            return "Create engaging short-form video content."
        
        topic = context.get('topic', '')
        tone = context.get('tone', 'professional')
        goal = context.get('goal', 'educate')
        
        # Extract keywords
        keywords = self._extract_keywords(topic, count=2)
        main_keyword = keywords[0] if keywords else topic.split()[0]
        
        # Generate components
        hook = self._generate_hook(topic, tone)
        core_idea = self._generate_core_idea(topic, main_keyword, goal)
        scenes = self._generate_scenes(topic, main_keyword)
        cta = self._generate_cta(goal)
        
        # Build reel structure
        reel = self._build_reel_structure(hook, core_idea, scenes, cta)
        
        return self._format_output(reel)
    
    def _generate_hook(self, topic, tone):
        """Generate attention-grabbing hook"""
        topic_clean = self._capitalize(topic)
        
        hooks_bold = [
            f"Stop scrolling! This {topic_clean} tip will blow your mind",
            f"You're doing {topic_clean} wrong (here's why)",
            f"The {topic_clean} secret nobody tells you",
            f"POV: You finally understand {topic_clean}",
            f"Wait... {topic_clean} is THAT easy?"
        ]
        
        hooks_casual = [
            f"Let's talk about {topic_clean}",
            f"So you want to learn {topic_clean}?",
            f"Here's what I learned about {topic_clean}",
            f"Quick {topic_clean} tip for you",
            f"Story time: {topic_clean} edition"
        ]
        
        hooks_professional = [
            f"Master {topic_clean} in 60 seconds",
            f"The {topic_clean} framework you need",
            f"3 steps to better {topic_clean}",
            f"Your {topic_clean} guide starts here",
            f"Essential {topic_clean} insights"
        ]
        
        if tone.lower() in ["bold", "humorous"]:
            return random.choice(hooks_bold)
        elif tone.lower() == "casual":
            return random.choice(hooks_casual)
        else:
            return random.choice(hooks_professional)
    
    def _generate_core_idea(self, topic, keyword, goal):
        """Generate main content idea"""
        topic_clean = self._capitalize(topic)
        
        ideas_by_goal = {
            "educate": f"Break down {topic_clean} into 3 simple steps, focusing on {keyword} as the foundation.",
            "inspire": f"Show the transformation possible with {topic_clean}, highlighting {keyword} as the key.",
            "entertain": f"Create a relatable scenario about {topic_clean}, making {keyword} the punchline.",
            "sell": f"Demonstrate the problem without {topic_clean}, then reveal {keyword} as the solution.",
            "build community": f"Share your personal {topic_clean} story, emphasizing {keyword} throughout.",
            "drive traffic": f"Tease your best {topic_clean} content, with {keyword} as the main hook.",
            "increase engagement": f"Ask viewers to choose between two {topic_clean} approaches involving {keyword}."
        }
        
        return ideas_by_goal.get(goal.lower(), ideas_by_goal["educate"])
    
    def _generate_scenes(self, topic, keyword):
        """Generate scene-by-scene breakdown"""
        topic_clean = topic.lower()
        
        scenes = [
            {
                "number": 1,
                "description": f"Open with the hook - grab attention immediately",
                "text_overlay": f"The {topic_clean} mistake everyone makes",
                "duration": "2-3 seconds"
            },
            {
                "number": 2,
                "description": f"Present the main concept about {keyword}",
                "text_overlay": f"Here's the truth about {keyword}",
                "duration": "3-5 seconds"
            },
            {
                "number": 3,
                "description": f"Show the application or transformation",
                "text_overlay": f"When you apply {keyword} correctly",
                "duration": "3-4 seconds"
            }
        ]
        
        return scenes
    
    def _generate_cta(self, goal):
        """Generate call-to-action"""
        ctas_by_goal = {
            "educate": "Follow for more tips like this!",
            "inspire": "Save this for motivation later",
            "entertain": "Tag someone who needs to see this",
            "sell": "Link in bio for the full guide",
            "build community": "Comment your experience below",
            "drive traffic": "Check the link in bio for more",
            "increase engagement": "Drop a ❤️ if you agree"
        }
        
        return ctas_by_goal.get(goal.lower(), "Follow for more!")
    
    def _build_reel_structure(self, hook, core_idea, scenes, cta):
        """Build complete reel structure"""
        output = "🎥 **REEL CONCEPT**\n\n"
        output += f"**Hook (First 1 second):**\n{hook}\n\n"
        output += f"**Core Idea:**\n{core_idea}\n\n"
        output += "**Scene Breakdown:**\n\n"
        
        for scene in scenes:
            output += f"Scene {scene['number']} ({scene['duration']}):\n"
            output += f"- Visual: {scene['description']}\n"
            output += f"- Text Overlay: \"{scene['text_overlay']}\"\n\n"
        
        output += f"**Call-to-Action:**\n{cta}\n\n"
        output += "**Pro Tips:**\n"
        output += "- Use trending audio for better reach\n"
        output += "- Add captions for accessibility\n"
        output += "- Keep transitions smooth and quick\n"
        output += "- Post during peak engagement hours"
        
        return output