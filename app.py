"""
Main Streamlit application for Creators Workflow AI
"""

import streamlit as st
from config import (
    APP_NAME,
    APP_DESCRIPTION,
    TONE_OPTIONS,
    AUDIENCE_OPTIONS,
    GOAL_OPTIONS,
    DEFAULT_TONE,
    DEFAULT_AUDIENCE,
    DEFAULT_GOAL,
    MIN_INPUT_LENGTH,
    MAX_INPUT_LENGTH
)

from src.generators.caption_generator import CaptionGenerator
from src.generators.hashtag_generator import HashtagGenerator
from src.generators.tweet_generator import TweetGenerator
from src.generators.reel_generator import ReelGenerator
from src.generators.blog_generator import BlogGenerator

# Page Configuration
st.set_page_config(
    page_title=APP_NAME,
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Initialize Session State
if 'generated' not in st.session_state:
    st.session_state.generated = False
if 'outputs' not in st.session_state:
    st.session_state.outputs = {}

# Custom CSS
st.markdown("""
    <style>
    .main-header {
        font-size: 3rem;
        font-weight: bold;
        text-align: center;
        margin-bottom: 0.5rem;
    }
    .sub-header {
        font-size: 1.2rem;
        text-align: center;
        color: #666;
        margin-bottom: 2rem;
    }
    .output-section {
        background-color: #f8f9fa;
        padding: 1.5rem;
        border-radius: 10px;
        margin-bottom: 1.5rem;
        border-left: 4px solid #4CAF50;
    }
    .output-title {
        font-size: 1.5rem;
        font-weight: bold;
        margin-bottom: 1rem;
        color: #333;
    }
    </style>
""", unsafe_allow_html=True)

# Header
st.markdown(f'<div class="main-header">🚀 {APP_NAME}</div>', unsafe_allow_html=True)
st.markdown(f'<div class="sub-header">{APP_DESCRIPTION}</div>', unsafe_allow_html=True)

# Sidebar
with st.sidebar:
    st.header("⚙️ Settings")
    
    tone = st.selectbox(
        "📝 Tone",
        options=TONE_OPTIONS,
        index=TONE_OPTIONS.index(DEFAULT_TONE),
        help="Choose the tone for your content"
    )
    
    audience = st.selectbox(
        "👥 Target Audience",
        options=AUDIENCE_OPTIONS,
        index=AUDIENCE_OPTIONS.index(DEFAULT_AUDIENCE),
        help="Who is your content for?"
    )
    
    goal = st.selectbox(
        "🎯 Content Goal",
        options=GOAL_OPTIONS,
        index=GOAL_OPTIONS.index(DEFAULT_GOAL),
        help="What do you want to achieve?"
    )
    
    st.divider()
    
    st.markdown("### 💡 Tips")
    st.markdown("""
    - Enter any topic, idea, or even a single word
    - Be specific for better results
    - Experiment with different tones
    - Adjust settings for your audience
    """)

# Main Content Area
st.header("✨ Enter Your Idea")

topic_input = st.text_area(
    "Topic / Idea / Description",
    placeholder="e.g., AI in healthcare, morning routines, sustainable fashion, or even just 'productivity'",
    height=100,
    max_chars=MAX_INPUT_LENGTH,
    help=f"Enter {MIN_INPUT_LENGTH}-{MAX_INPUT_LENGTH} characters"
)

generate_button = st.button("🚀 Generate Workflow", type="primary", use_container_width=True)

# Generation Logic
if generate_button:
    if not topic_input or len(topic_input.strip()) < MIN_INPUT_LENGTH:
        st.error("⚠️ Please enter a topic or idea to generate content.")
    else:
        with st.spinner("🎨 Generating your creator workflow..."):
            # Prepare context
            context = {
                "topic": topic_input.strip(),
                "tone": tone.lower(),
                "audience": audience.lower(),
                "goal": goal.lower()
            }
            
            # Initialize generators
            caption_gen = CaptionGenerator()
            hashtag_gen = HashtagGenerator()
            tweet_gen = TweetGenerator()
            reel_gen = ReelGenerator()
            blog_gen = BlogGenerator()
            
            # Generate all outputs
            st.session_state.outputs = {
                "caption": caption_gen.generate(context),
                "hashtags": hashtag_gen.generate(context),
                "tweet": tweet_gen.generate(context),
                "reel": reel_gen.generate(context),
                "blog": blog_gen.generate(context)
            }
            
            st.session_state.generated = True
        
        st.success("✅ Content generated successfully!")

# Display Outputs
if st.session_state.generated and st.session_state.outputs:
    st.divider()
    st.header("📋 Your Creator Workflow")
    
    # Caption Section
    with st.container():
        st.markdown('<div class="output-section">', unsafe_allow_html=True)
        st.markdown('<div class="output-title">📸 Caption</div>', unsafe_allow_html=True)
        st.markdown(st.session_state.outputs["caption"])
        if st.button("📋 Copy Caption", key="copy_caption"):
            st.toast("Caption copied!", icon="✅")
        st.markdown('</div>', unsafe_allow_html=True)
    
    # Hashtags Section
    with st.container():
        st.markdown('<div class="output-section">', unsafe_allow_html=True)
        st.markdown('<div class="output-title">#️⃣ Hashtags</div>', unsafe_allow_html=True)
        st.markdown(st.session_state.outputs["hashtags"])
        if st.button("📋 Copy Hashtags", key="copy_hashtags"):
            st.toast("Hashtags copied!", icon="✅")
        st.markdown('</div>', unsafe_allow_html=True)
    
    # Tweet Section
    with st.container():
        st.markdown('<div class="output-section">', unsafe_allow_html=True)
        st.markdown('<div class="output-title">🐦 Tweet</div>', unsafe_allow_html=True)
        st.markdown(st.session_state.outputs["tweet"])
        if st.button("📋 Copy Tweet", key="copy_tweet"):
            st.toast("Tweet copied!", icon="✅")
        st.markdown('</div>', unsafe_allow_html=True)
    
    # Reel Idea Section
    with st.container():
        st.markdown('<div class="output-section">', unsafe_allow_html=True)
        st.markdown('<div class="output-title">🎥 Reel Idea</div>', unsafe_allow_html=True)
        st.markdown(st.session_state.outputs["reel"])
        if st.button("📋 Copy Reel Idea", key="copy_reel"):
            st.toast("Reel idea copied!", icon="✅")
        st.markdown('</div>', unsafe_allow_html=True)
    
    # Blog Section
    with st.container():
        st.markdown('<div class="output-section">', unsafe_allow_html=True)
        st.markdown('<div class="output-title">📝 Blog Outline</div>', unsafe_allow_html=True)
        st.markdown(st.session_state.outputs["blog"])
        if st.button("📋 Copy Blog Outline", key="copy_blog"):
            st.toast("Blog outline copied!", icon="✅")
        st.markdown('</div>', unsafe_allow_html=True)
    
    # Reset Button
    st.divider()
    if st.button("🔄 Generate New Content", use_container_width=True):
        st.session_state.generated = False
        st.session_state.outputs = {}
        st.rerun()

# Footer
st.divider()
st.markdown("""
    <div style='text-align: center; color: #666; padding: 1rem;'>
        Made with ❤️ for Creators | © 2025 Isha Saxena 
    </div>
""", unsafe_allow_html=True)