"""
Content templates for all content types
"""


class ContentTemplates:
    """Stores and manages content templates for generation"""
    
    # Caption Templates
    CAPTION_TEMPLATES = {
        "professional": [
            "💡 {hook}\n\n{body}\n\n{cta}",
            "📌 Key insight: {hook}\n\n{body}\n\n{cta}",
            "✨ {hook}\n\n{body}\n\nWhat's your take? {cta}",
            "🎯 {hook}\n\n{body}\n\n{cta}",
            "📊 {hook}\n\n{body}\n\nShare your thoughts. {cta}"
        ],
        "casual": [
            "Hey! 👋 {hook}\n\n{body}\n\n{cta}",
            "{hook} 😊\n\n{body}\n\n{cta}",
            "So... {hook}\n\n{body}\n\nLet me know! {cta}",
            "Real talk: {hook}\n\n{body}\n\n{cta}",
            "{hook} 💭\n\n{body}\n\nThoughts? {cta}"
        ],
        "friendly": [
            "Hi friends! 🌟 {hook}\n\n{body}\n\n{cta}",
            "💙 {hook}\n\n{body}\n\nLove to hear from you! {cta}",
            "Hey there! {hook}\n\n{body}\n\n{cta}",
            "✨ {hook}\n\n{body}\n\nTag a friend! {cta}",
            "Friends, {hook}\n\n{body}\n\n{cta}"
        ],
        "inspirational": [
            "🌟 {hook}\n\n{body}\n\n{cta}",
            "✨ Remember: {hook}\n\n{body}\n\n{cta}",
            "💫 {hook}\n\n{body}\n\nYou've got this! {cta}",
            "🚀 {hook}\n\n{body}\n\nKeep pushing forward. {cta}",
            "⭐ {hook}\n\n{body}\n\nBelieve in yourself. {cta}"
        ],
        "educational": [
            "📚 Learn this: {hook}\n\n{body}\n\n{cta}",
            "🎓 {hook}\n\n{body}\n\nSave this for later! {cta}",
            "💡 Did you know? {hook}\n\n{body}\n\n{cta}",
            "📖 {hook}\n\n{body}\n\nShare to help others learn! {cta}",
            "🧠 {hook}\n\n{body}\n\n{cta}"
        ],
        "humorous": [
            "😂 {hook}\n\n{body}\n\n{cta}",
            "🤣 Not gonna lie... {hook}\n\n{body}\n\n{cta}",
            "😅 {hook}\n\n{body}\n\nTag someone who needs this! {cta}",
            "LOL {hook}\n\n{body}\n\n{cta}",
            "😆 {hook}\n\n{body}\n\nWho can relate? {cta}"
        ],
        "bold": [
            "🔥 {hook}\n\n{body}\n\n{cta}",
            "💥 Hot take: {hook}\n\n{body}\n\n{cta}",
            "⚡ {hook}\n\n{body}\n\nAgree or disagree? {cta}",
            "🎯 Truth bomb: {hook}\n\n{body}\n\n{cta}",
            "🚨 {hook}\n\n{body}\n\n{cta}"
        ]
    }
    
    # Hook Templates
    HOOK_TEMPLATES = [
        "Here's everything you need to know about {topic}",
        "The truth about {topic} that nobody tells you",
        "Why {topic} matters more than you think",
        "Stop ignoring {topic}",
        "The {topic} guide you've been waiting for",
        "Master {topic} in simple steps",
        "Everything changed when I learned about {topic}",
        "The ultimate {topic} breakdown",
        "What everyone gets wrong about {topic}",
        "Your {topic} questions, answered"
    ]
    
    # Body Templates
    BODY_TEMPLATES = [
        "This approach to {topic} has transformed how I think about {keyword}. The key is understanding the fundamentals first.",
        "Most people overlook the importance of {topic}. Here's what you need to focus on: {keyword} and consistency.",
        "After diving deep into {topic}, I discovered that {keyword} is the game-changer everyone needs.",
        "The secret to {topic}? It's simpler than you think. Focus on {keyword} and stay committed.",
        "If you're serious about {topic}, you can't ignore {keyword}. It's the foundation of everything.",
        "{topic} doesn't have to be complicated. Start with {keyword} and build from there.",
        "Three things about {topic}: clarity, {keyword}, and taking action. That's it.",
        "Real talk about {topic}: {keyword} is what separates beginners from experts."
    ]
    
    # CTA Templates
    CTA_TEMPLATES = [
        "Save this post for later!",
        "Share with someone who needs this",
        "Drop a 💙 if you found this helpful",
        "Comment your thoughts below",
        "Tag a friend who should see this",
        "Follow for more insights",
        "What's your experience with this?",
        "Double tap if you agree",
        "Save and share to spread the word",
        "Let's discuss in the comments"
    ]
    
    # Tweet Templates
    TWEET_TEMPLATES = {
        "professional": [
            "🧵 {hook}\n\n{body}\n\n{keyword}",
            "💡 {hook}\n\n{body}",
            "Quick insight: {hook}\n\n{body}",
            "{hook}\n\nKey takeaway: {body}",
            "📊 {hook}\n\n{body}\n\n{keyword}"
        ],
        "casual": [
            "{hook} 😊\n\n{body}",
            "So... {hook}\n\n{body}",
            "{hook}\n\n{body}\n\nThoughts?",
            "Hot take: {hook}\n\n{body}",
            "{hook} 💭\n\n{body}"
        ],
        "inspirational": [
            "✨ {hook}\n\n{body}\n\nYou got this! 💪",
            "🌟 {hook}\n\n{body}",
            "Remember: {hook}\n\n{body}",
            "🚀 {hook}\n\n{body}",
            "{hook}\n\n{body}\n\nKeep going! ⭐"
        ]
    }
    
    # Reel Structure Templates
    REEL_TEMPLATES = {
        "hook": [
            "Start with: '{hook_text}'",
            "Open with a question: '{hook_text}?'",
            "Show the problem: '{hook_text}'",
            "Bold statement: '{hook_text}!'",
            "Pattern interrupt: '{hook_text}'"
        ],
        "body": [
            "Break down {topic} in 3 simple points",
            "Show the transformation with {topic}",
            "Demonstrate {keyword} in action",
            "Compare before/after {topic}",
            "Walk through the {topic} process step-by-step"
        ],
        "cta": [
            "End with: 'Follow for more {topic} tips'",
            "Call to action: 'Save this for later'",
            "Engagement: 'Which tip will you try first?'",
            "Close: 'Share this with someone who needs {topic}'",
            "Final hook: 'Want more? Check the link in bio'"
        ]
    }
    
    # Blog Structure Templates
    BLOG_TITLE_TEMPLATES = [
        "The Complete Guide to {topic}",
        "How to Master {topic} in {year}",
        "{topic}: Everything You Need to Know",
        "The Ultimate {topic} Guide for Beginners",
        "{keyword} and {topic}: A Comprehensive Overview",
        "Why {topic} Matters (And How to Get Started)",
        "The {topic} Handbook: From Basics to Advanced",
        "Understanding {topic}: A Step-by-Step Guide",
        "{topic} 101: Essential Tips and Strategies",
        "Transform Your {keyword} with These {topic} Insights"
    ]
    
    BLOG_INTRO_TEMPLATES = [
        "In today's fast-paced world, {topic} has become more important than ever. This guide will walk you through everything you need to know about {keyword} and how to apply it effectively.",
        "Whether you're new to {topic} or looking to level up your {keyword} skills, this comprehensive guide has you covered. Let's dive in.",
        "Understanding {topic} can be overwhelming, but it doesn't have to be. In this article, we'll break down {keyword} into simple, actionable steps.",
        "If you've been curious about {topic}, you're in the right place. This guide explores {keyword} and provides practical insights you can use immediately."
    ]
    
    BLOG_SECTION_TEMPLATES = [
        "What is {topic}?",
        "Why {topic} Matters",
        "Getting Started with {topic}",
        "Key Principles of {keyword}",
        "Common Mistakes to Avoid",
        "Best Practices for {topic}",
        "Advanced {keyword} Techniques",
        "Tools and Resources for {topic}",
        "Real-World Applications",
        "Measuring Success with {topic}"
    ]
    
    BLOG_CONCLUSION_TEMPLATES = [
        "Now that you understand {topic}, it's time to take action. Start with {keyword} and build from there. Remember, consistency is key.",
        "Mastering {topic} takes time, but with these insights on {keyword}, you're well on your way. Keep learning and experimenting.",
        "The journey with {topic} is ongoing. Use these {keyword} strategies as your foundation and continue to grow.",
        "{topic} doesn't have to be complicated. Focus on {keyword}, stay committed, and you'll see results."
    ]
    
    @staticmethod
    def get_template(template_type, tone="professional"):
        """Get a template by type and tone"""
        tone = tone.lower()
        
        if template_type == "caption":
            templates = ContentTemplates.CAPTION_TEMPLATES.get(tone, ContentTemplates.CAPTION_TEMPLATES["professional"])
            return templates[0]
        
        elif template_type == "tweet":
            templates = ContentTemplates.TWEET_TEMPLATES.get(tone, ContentTemplates.TWEET_TEMPLATES["professional"])
            return templates[0]
        
        return ""
    
    @staticmethod
    def get_hook(topic):
        """Get a hook template"""
        import random
        template = random.choice(ContentTemplates.HOOK_TEMPLATES)
        return template.format(topic=topic)
    
    @staticmethod
    def get_body(topic, keyword):
        """Get a body template"""
        import random
        template = random.choice(ContentTemplates.BODY_TEMPLATES)
        return template.format(topic=topic, keyword=keyword)
    
    @staticmethod
    def get_cta():
        """Get a CTA template"""
        import random
        return random.choice(ContentTemplates.CTA_TEMPLATES)