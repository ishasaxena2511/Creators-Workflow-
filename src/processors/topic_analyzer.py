"""
Topic analyzer for categorizing content based on keywords
"""

from config import CATEGORIES


class TopicAnalyzer:
    """Analyzes and categorizes topics based on keyword matching"""
    
    CATEGORY_KEYWORDS = {
        "technology": [
            "ai", "tech", "software", "app", "code", "coding", "programming", "developer",
            "computer", "digital", "data", "algorithm", "machine learning", "startup",
            "innovation", "gadget", "device", "internet", "web", "mobile", "cloud",
            "cybersecurity", "blockchain", "crypto", "saas", "api", "automation"
        ],
        "business": [
            "business", "entrepreneur", "startup", "marketing", "sales", "strategy",
            "growth", "revenue", "profit", "investment", "finance", "leadership",
            "management", "productivity", "team", "brand", "customer", "client",
            "market", "competition", "negotiation", "networking", "b2b", "b2c"
        ],
        "lifestyle": [
            "lifestyle", "life", "routine", "habit", "morning", "evening", "daily",
            "wellness", "balance", "mindfulness", "meditation", "self-care", "personal",
            "home", "decor", "fashion", "style", "beauty", "relationship", "family"
        ],
        "health & fitness": [
            "health", "fitness", "workout", "exercise", "gym", "training", "nutrition",
            "diet", "healthy", "weight", "muscle", "cardio", "yoga", "running",
            "strength", "wellness", "medical", "mental health", "therapy", "sleep"
        ],
        "travel": [
            "travel", "trip", "vacation", "destination", "adventure", "explore",
            "journey", "tourist", "hotel", "flight", "beach", "mountain", "city",
            "country", "culture", "backpack", "road trip", "cruise", "touring"
        ],
        "food": [
            "food", "recipe", "cooking", "chef", "cuisine", "meal", "dinner", "lunch",
            "breakfast", "dessert", "restaurant", "kitchen", "baking", "ingredient",
            "dish", "taste", "flavor", "healthy eating", "vegan", "vegetarian"
        ],
        "education": [
            "education", "learning", "study", "student", "teacher", "course", "school",
            "university", "college", "lesson", "tutorial", "training", "skill",
            "knowledge", "academic", "exam", "degree", "online learning", "certification"
        ],
        "entertainment": [
            "entertainment", "movie", "film", "music", "game", "gaming", "show", "series",
            "tv", "netflix", "streaming", "fun", "hobby", "art", "creative", "photography",
            "video", "content", "creator", "influencer", "social media"
        ],
        "finance": [
            "finance", "money", "investment", "investing", "stock", "trading", "crypto",
            "bitcoin", "savings", "budget", "wealth", "income", "passive income",
            "financial", "portfolio", "retirement", "tax", "banking", "credit", "debt"
        ]
    }
    
    def __init__(self):
        pass
    
    def categorize_topic(self, text):
        """Categorize topic based on keyword matching"""
        if not text:
            return "general"
        
        text_lower = text.lower()
        words = text_lower.split()
        
        # Score each category
        category_scores = {}
        for category, keywords in self.CATEGORY_KEYWORDS.items():
            score = 0
            for keyword in keywords:
                # Exact word match
                if keyword in words:
                    score += 2
                # Substring match
                elif keyword in text_lower:
                    score += 1
            category_scores[category] = score
        
        # Get category with highest score
        if category_scores:
            max_score = max(category_scores.values())
            if max_score > 0:
                best_category = max(category_scores, key=category_scores.get)
                return best_category
        
        return "general"
    
    def get_category_confidence(self, text):
        """Get confidence score for categorization"""
        if not text:
            return 0.0
        
        text_lower = text.lower()
        words = text_lower.split()
        
        max_score = 0
        for keywords in self.CATEGORY_KEYWORDS.values():
            score = sum(1 for keyword in keywords if keyword in text_lower)
            max_score = max(max_score, score)
        
        # Normalize confidence (0-1 scale)
        confidence = min(max_score / 5.0, 1.0)
        return round(confidence, 2)
    
    def get_related_topics(self, text, limit=5):
        """Get related topic suggestions"""
        category = self.categorize_topic(text)
        
        if category == "general":
            return []
        
        related_keywords = self.CATEGORY_KEYWORDS.get(category, [])
        return related_keywords[:limit]
    
    def is_single_word(self, text):
        """Check if input is a single word"""
        if not text:
            return False
        return len(text.strip().split()) == 1
    
    def enhance_context(self, text, tone, audience, goal):
        """Enhance context with additional metadata"""
        category = self.categorize_topic(text)
        confidence = self.get_category_confidence(text)
        is_single = self.is_single_word(text)
        
        return {
            "category": category,
            "confidence": confidence,
            "is_single_word": is_single,
            "tone": tone,
            "audience": audience,
            "goal": goal,
            "text": text
        }