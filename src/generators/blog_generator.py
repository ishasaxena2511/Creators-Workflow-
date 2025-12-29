"""
Blog outline generator for long-form content
"""

import random
from datetime import datetime
from .base_generator import BaseGenerator
from src.templates.content_templates import ContentTemplates


class BlogGenerator(BaseGenerator):
    """Generates structured blog outlines"""
    
    def __init__(self):
        super().__init__()
        self.min_sections = 3
        self.max_sections = 5
    
    def generate(self, context):
        """Generate a blog outline based on context"""
        if not self._validate_input(context):
            return "Create compelling long-form content."
        
        topic = context.get('topic', '')
        tone = context.get('tone', 'professional')
        audience = context.get('audience', 'general')
        
        # Extract keywords
        keywords = self._extract_keywords(topic, count=3)
        main_keyword = keywords[0] if keywords else topic.split()[0]
        
        # Get category
        category = self._get_category(topic)
        
        # Generate components
        title = self._generate_title(topic, main_keyword)
        intro = self._generate_intro(topic, main_keyword, audience)
        sections = self._generate_sections(topic, keywords, category)
        conclusion = self._generate_conclusion(topic, main_keyword)
        
        # Build blog structure
        blog = self._build_blog_structure(title, intro, sections, conclusion)
        
        return self._format_output(blog)
    
    def _generate_title(self, topic, keyword):
        """Generate SEO-friendly blog title"""
        topic_clean = self._capitalize(topic)
        current_year = datetime.now().year
        
        title_templates = [
            f"The Complete Guide to {topic_clean} in {current_year}",
            f"How to Master {topic_clean}: A Step-by-Step Guide",
            f"{topic_clean}: Everything You Need to Know",
            f"The Ultimate {topic_clean} Handbook for Beginners",
            f"Understanding {topic_clean}: Tips, Tricks, and Best Practices",
            f"{keyword.capitalize()} and {topic_clean}: A Comprehensive Overview",
            f"Transform Your {keyword.capitalize()} with {topic_clean}",
            f"Why {topic_clean} Matters (And How to Get Started)",
            f"{topic_clean} 101: Essential Strategies for Success",
            f"The Essential {topic_clean} Guide: From Basics to Advanced"
        ]
        
        return random.choice(title_templates)
    
    def _generate_intro(self, topic, keyword, audience):
        """Generate introduction paragraph"""
        topic_clean = topic.lower()
        keyword_clean = keyword.lower()
        
        intros = [
            f"In today's world, {topic_clean} has become essential for anyone looking to succeed. Whether you're just starting out or looking to refine your approach, understanding {keyword_clean} is the key to unlocking better results. This comprehensive guide will walk you through everything you need to know.",
            
            f"If you've been curious about {topic_clean}, you're in the right place. This guide breaks down {keyword_clean} into clear, actionable steps that anyone can follow. By the end, you'll have a solid foundation to build upon.",
            
            f"Understanding {topic_clean} can seem overwhelming at first, but it doesn't have to be. In this article, we'll explore {keyword_clean} and show you how to apply these insights immediately. Let's dive in.",
            
            f"Whether you're new to {topic_clean} or looking to level up your skills, this guide has you covered. We'll focus on {keyword_clean} and the strategies that actually work in real-world scenarios."
        ]
        
        return random.choice(intros)
    
    def _generate_sections(self, topic, keywords, category):
        """Generate main content sections"""
        topic_clean = self._capitalize(topic)
        main_keyword = keywords[0] if keywords else "this topic"
        
        # Base sections that work for any topic
        sections = [
            {
                "heading": f"What is {topic_clean}?",
                "points": [
                    f"Define {topic_clean} in simple terms",
                    f"Explain why {topic_clean} matters today",
                    f"Common misconceptions about {topic_clean}",
                    f"The role of {main_keyword} in {topic_clean}"
                ]
            },
            {
                "heading": f"Why {topic_clean} Matters",
                "points": [
                    f"The impact of {topic_clean} on your goals",
                    f"Real-world applications and benefits",
                    f"How {main_keyword} creates value",
                    f"Common challenges and how to overcome them"
                ]
            },
            {
                "heading": f"Getting Started with {topic_clean}",
                "points": [
                    f"First steps for beginners",
                    f"Essential tools and resources",
                    f"Setting up your {main_keyword} foundation",
                    f"Avoiding common beginner mistakes"
                ]
            },
            {
                "heading": f"Best Practices for {topic_clean}",
                "points": [
                    f"Proven strategies that work",
                    f"How to optimize your {main_keyword} approach",
                    f"Tips from experts in the field",
                    f"Measuring success and progress"
                ]
            },
            {
                "heading": f"Advanced {topic_clean} Techniques",
                "points": [
                    f"Taking your {main_keyword} to the next level",
                    f"Advanced strategies for experienced users",
                    f"Innovative approaches to try",
                    f"Future trends in {topic_clean}"
                ]
            }
        ]
        
        # Select appropriate number of sections
        num_sections = random.randint(self.min_sections, self.max_sections)
        return sections[:num_sections]
    
    def _generate_conclusion(self, topic, keyword):
        """Generate conclusion paragraph"""
        topic_clean = topic.lower()
        keyword_clean = keyword.lower()
        
        conclusions = [
            f"Mastering {topic_clean} takes time and practice, but with the insights shared in this guide, you're well-equipped to succeed. Focus on {keyword_clean}, stay consistent, and don't be afraid to experiment. Remember, everyone starts somewhere—what matters is taking that first step.",
            
            f"Now that you understand the fundamentals of {topic_clean}, it's time to put this knowledge into action. Start with {keyword_clean}, build from there, and keep learning along the way. Your journey is just beginning, and the possibilities are endless.",
            
            f"The world of {topic_clean} is constantly evolving, but the core principles remain the same. By prioritizing {keyword_clean} and applying the strategies we've discussed, you'll be ahead of the curve. Keep pushing forward, stay curious, and enjoy the process.",
            
            f"{topic_clean.capitalize()} doesn't have to be complicated. With a solid understanding of {keyword_clean} and a commitment to continuous improvement, you'll see real results. Thank you for reading, and here's to your success!"
        ]
        
        return random.choice(conclusions)
    
    def _build_blog_structure(self, title, intro, sections, conclusion):
        """Build complete blog outline"""
        output = f"# {title}\n\n"
        output += "---\n\n"
        output += f"**Introduction**\n\n{intro}\n\n"
        output += "---\n\n"
        
        for i, section in enumerate(sections, 1):
            output += f"## {section['heading']}\n\n"
            for point in section['points']:
                output += f"- {point}\n"
            output += "\n"
        
        output += "---\n\n"
        output += f"**Conclusion**\n\n{conclusion}\n\n"
        output += "---\n\n"
        output += "**Additional Resources:**\n"
        output += "- Further reading and references\n"
        output += "- Related articles and guides\n"
        output += "- Tools and templates\n"
        output += "- Community forums and support"
        
        return output