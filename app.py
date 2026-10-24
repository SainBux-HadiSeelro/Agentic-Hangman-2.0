"""
🎯 HANGMAN: Modern & Friendly Edition
Built by Sain Bux (Hadi Seelro) - Agentic AI & Full-Stack Python Developer.
Designed to be simple, fun, and easy for everyone to play!
"""

import streamlit as st
import random
from typing import Dict, List
from agent import NexusAgent

# Page configuration
st.set_page_config(
    page_title="Hangman Game | Friendly AI Edition",
    page_icon="🎯",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Clean, modern, accessible, and high-contrast CSS styling
FRIENDLY_CSS = """
<style>
@import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;600;700;800&family=JetBrains+Mono:wght@500;700;800&display=swap');

/* Global Font & Text Visibility */
html, body, [class*="css"], .stApp {
    font-family: 'Plus Jakarta Sans', sans-serif !important;
}

/* Background */
.stApp {
    background: linear-gradient(135deg, #090d16 0%, #0f172a 50%, #1e293b 100%) !important;
    color: #f8fafc !important;
}

/* High Contrast Headings across all elements */
h1, h2, h3, h4, h5, h6,
[data-testid="stMarkdownContainer"] h1,
[data-testid="stMarkdownContainer"] h2,
[data-testid="stMarkdownContainer"] h3,
[data-testid="stMarkdownContainer"] h4 {
    color: #ffffff !important;
    font-weight: 700 !important;
    letter-spacing: -0.01em;
}

/* High Contrast Paragraphs & Labels */
p, span, label,
[data-testid="stMarkdownContainer"] p {
    color: #f1f5f9 !important;
    line-height: 1.5;
}

/* Main Titles */
.main-title {
    font-size: 2.4rem;
    font-weight: 800;
    text-align: center;
    background: linear-gradient(135deg, #38bdf8 0%, #818cf8 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    margin-bottom: 0.2rem;
}

.main-subtitle {
    text-align: center;
    font-size: 1.05rem;
    color: #cbd5e1 !important;
    margin-bottom: 1.5rem;
    font-weight: 500;
}

/* Metric Cards Styling */
[data-testid="stMetric"] {
    background: rgba(30, 41, 59, 0.8) !important;
    border: 1px solid rgba(255, 255, 255, 0.12) !important;
    border-radius: 14px !important;
    padding: 0.7rem 1.1rem !important;
    box-shadow: 0 4px 15px rgba(0, 0, 0, 0.3) !important;
}

[data-testid="stMetricLabel"] * {
    color: #cbd5e1 !important;
    font-size: 0.95rem !important;
    font-weight: 600 !important;
}

[data-testid="stMetricValue"] * {
    color: #38bdf8 !important;
    font-size: 1.8rem !important;
    font-weight: 800 !important;
}

/* Dropdown / Selectbox Styling */
[data-testid="stSelectbox"] label p {
    color: #ffffff !important;
    font-size: 0.95rem !important;
    font-weight: 700 !important;
}

[data-testid="stSelectbox"] div[data-baseweb="select"] {
    background-color: #1e293b !important;
    border-color: #475569 !important;
    border-radius: 10px !important;
}

[data-testid="stSelectbox"] div[data-baseweb="select"] * {
    color: #ffffff !important;
    font-weight: 600 !important;
}

/* Word Box & Modern Letter Tiles */
.word-card {
    background: #111827;
    border: 1px solid rgba(56, 189, 248, 0.3);
    border-radius: 16px;
    padding: 1.5rem;
    text-align: center;
    box-shadow: 0 8px 24px rgba(0, 0, 0, 0.35);
    margin-bottom: 1.2rem;
}

.word-tiles-container {
    display: flex;
    justify-content: center;
    align-items: center;
    gap: 10px;
    flex-wrap: wrap;
    margin: 1.2rem 0;
}

.letter-tile {
    display: inline-flex;
    align-items: center;
    justify-content: center;
    width: 46px;
    height: 56px;
    font-family: 'JetBrains Mono', monospace;
    font-size: 2.1rem;
    font-weight: 800;
    border-radius: 10px;
    user-select: none;
    transition: all 0.2s ease;
}

.letter-tile.revealed {
    background: linear-gradient(180deg, #0284c7 0%, #0369a1 100%);
    color: #ffffff;
    border: 2px solid #38bdf8;
    box-shadow: 0 4px 14px rgba(56, 189, 248, 0.4);
}

.letter-tile.blank {
    background: #090e17;
    border: 2px dashed #475569;
    border-bottom: 4px solid #38bdf8;
    color: transparent;
}

.letter-tile.missed {
    background: linear-gradient(180deg, #7f1d1d 0%, #450a0a 100%);
    color: #fca5a5;
    border: 2px solid #ef4444;
}

.word-info-footer {
    font-size: 0.95rem;
    color: #cbd5e1;
    margin-top: 10px;
}

/* Hangman Drawing & Gallows Display */
.hangman-card {
    background: #111827;
    border: 1px solid rgba(255, 255, 255, 0.1);
    border-radius: 16px;
    padding: 1.2rem;
    box-shadow: 0 8px 24px rgba(0, 0, 0, 0.35);
    margin-bottom: 1rem;
}

.hangman-drawing {
    background: #070b12;
    border: 1px solid #1e293b;
    border-radius: 12px;
    padding: 1.2rem;
    font-family: 'JetBrains Mono', 'Courier New', monospace;
    font-size: 1.15rem;
    font-weight: 700;
    line-height: 1.35;
    color: #38bdf8;
    white-space: pre;
    display: flex;
    justify-content: center;
    text-align: left;
    box-shadow: inset 0 2px 10px rgba(0, 0, 0, 0.5);
}

/* Lives / Hearts Badge */
.lives-badge {
    background: #111827;
    border: 1px solid rgba(255, 255, 255, 0.1);
    border-radius: 12px;
    padding: 0.75rem 1rem;
    text-align: center;
    margin-bottom: 1rem;
}

.lives-hearts {
    font-size: 1.4rem;
    letter-spacing: 5px;
    margin-bottom: 4px;
}

.lives-text {
    font-size: 0.92rem;
    font-weight: 700;
    color: #f8fafc;
    letter-spacing: 0.5px;
}

/* Virtual Keyboard Buttons */
div[data-testid="stHorizontalBlock"] .stButton > button {
    height: 48px !important;
    min-height: 48px !important;
    padding: 2px !important;
    font-size: 1rem !important;
    font-weight: 800 !important;
    background: #1e293b !important;
    color: #ffffff !important;
    border: 1px solid #475569 !important;
    border-radius: 8px !important;
    box-shadow: 0 2px 5px rgba(0, 0, 0, 0.25) !important;
    transition: all 0.15s ease-in-out !important;
}

div[data-testid="stHorizontalBlock"] .stButton > button:hover:not(:disabled) {
    background: #0284c7 !important;
    color: #ffffff !important;
    border-color: #38bdf8 !important;
    transform: translateY(-2px);
    box-shadow: 0 4px 12px rgba(56, 189, 248, 0.45) !important;
}

/* Correct Guess Key (Green Accent) */
div[data-testid="stHorizontalBlock"] .stButton > button[data-testid="baseButton-primary"]:disabled,
div[data-testid="stHorizontalBlock"] .stButton > button[kind="primary"]:disabled {
    background: #064e3b !important;
    border-color: #10b981 !important;
    color: #6ee7b7 !important;
    opacity: 0.95 !important;
    font-weight: 800 !important;
}

/* Wrong Guess Key (Red Accent) */
div[data-testid="stHorizontalBlock"] .stButton > button[data-testid="baseButton-secondary"]:disabled,
div[data-testid="stHorizontalBlock"] .stButton > button[kind="secondary"]:disabled {
    background: #2a1215 !important;
    border-color: #7f1d1d !important;
    color: #f87171 !important;
    opacity: 0.85 !important;
    font-weight: 700 !important;
}

/* Primary Game Action Button (Restart) */
.main-game-actions .stButton > button,
button[kind="primary"]:not(:disabled) {
    background: linear-gradient(135deg, #0284c7 0%, #2563eb 100%) !important;
    color: #ffffff !important;
    border: none !important;
    font-size: 1.05rem !important;
    font-weight: 700 !important;
    border-radius: 12px !important;
    padding: 0.75rem 1.5rem !important;
    box-shadow: 0 4px 16px rgba(37, 99, 235, 0.35) !important;
}

button[kind="primary"]:not(:disabled):hover {
    background: linear-gradient(135deg, #38bdf8 0%, #3b82f6 100%) !important;
    transform: translateY(-2px);
    box-shadow: 0 6px 20px rgba(56, 189, 248, 0.45) !important;
}

/* Sidebar Styling */
[data-testid="stSidebar"] {
    background-color: #0b1120 !important;
    border-right: 1px solid rgba(255, 255, 255, 0.08) !important;
}

[data-testid="stSidebar"] [data-testid="stSidebarContent"] {
    background-color: #0b1120 !important;
}

[data-testid="stSidebar"] h1, 
[data-testid="stSidebar"] h2, 
[data-testid="stSidebar"] h3 {
    color: #38bdf8 !important;
    font-weight: 700 !important;
}

[data-testid="stSidebar"] p, 
[data-testid="stSidebar"] span, 
[data-testid="stSidebar"] label {
    color: #e2e8f0 !important;
}

[data-testid="stSidebar"] .stCaption {
    color: #cbd5e1 !important;
    font-size: 0.9rem !important;
}

/* Sidebar Quick Open Button */
[data-testid="stSidebar"] .stButton > button {
    background: #1e293b !important;
    color: #f8fafc !important;
    border: 1px solid #334155 !important;
    border-radius: 10px !important;
    font-size: 0.95rem !important;
    font-weight: 700 !important;
}

[data-testid="stSidebar"] .stButton > button:hover {
    background: #38bdf8 !important;
    color: #0f172a !important;
    border-color: #38bdf8 !important;
}

/* ======================================================== */
/* 🌐 WEBSITE-STYLE FLOATING CORNER CHATBOT WIDGET STYLING   */
/* ======================================================== */

/* 1. Floating Launcher Button (Bottom-Right Corner) */
div[class*="st-key-chat_launcher_container"] {
    position: fixed !important;
    bottom: 24px !important;
    right: 24px !important;
    z-index: 999999 !important;
}

div[class*="st-key-chat_launcher_container"] .stButton > button {
    background: linear-gradient(135deg, #0284c7 0%, #2563eb 100%) !important;
    color: #ffffff !important;
    border: 2px solid #38bdf8 !important;
    border-radius: 50px !important;
    padding: 12px 24px !important;
    font-size: 1.05rem !important;
    font-weight: 700 !important;
    box-shadow: 0 10px 25px rgba(2, 132, 199, 0.55), 0 0 16px rgba(56, 189, 248, 0.4) !important;
    cursor: pointer !important;
    transition: all 0.25s ease-in-out !important;
    display: flex !important;
    align-items: center !important;
    gap: 8px !important;
}

div[class*="st-key-chat_launcher_container"] .stButton > button:hover {
    transform: translateY(-3px) scale(1.04) !important;
    box-shadow: 0 14px 32px rgba(56, 189, 248, 0.65) !important;
}

/* 2. Floating Chat Window (Docked in Bottom-Right Corner) */
div[class*="st-key-chat_widget_container"] {
    position: fixed !important;
    bottom: 20px !important;
    right: 20px !important;
    width: 395px !important;
    max-width: calc(100vw - 32px) !important;
    background: #0f172a !important;
    border: 1px solid rgba(56, 189, 248, 0.4) !important;
    border-radius: 20px !important;
    padding: 1.1rem !important;
    box-shadow: 0 20px 50px rgba(0, 0, 0, 0.85), 0 0 25px rgba(56, 189, 248, 0.25) !important;
    z-index: 999999 !important;
    backdrop-filter: blur(16px) !important;
}

/* Close/Minimize Button */
div[class*="st-key-close_chat_btn"] > button {
    background: transparent !important;
    border: 1px solid rgba(255, 255, 255, 0.2) !important;
    border-radius: 50% !important;
    width: 32px !important;
    height: 32px !important;
    min-height: 32px !important;
    padding: 0 !important;
    color: #94a3b8 !important;
    font-size: 1rem !important;
    display: flex !important;
    align-items: center !important;
    justify-content: center !important;
    margin-left: auto !important;
}

div[class*="st-key-close_chat_btn"] > button:hover {
    background: rgba(239, 68, 68, 0.25) !important;
    color: #ef4444 !important;
    border-color: #ef4444 !important;
}

/* Quick Action Buttons inside Corner Chatbot */
div[class*="st-key-chat_widget_container"] .stButton > button {
    background: #1e293b !important;
    color: #f8fafc !important;
    border: 1px solid #334155 !important;
    border-radius: 8px !important;
    font-size: 0.82rem !important;
    font-weight: 600 !important;
    height: 34px !important;
    min-height: 34px !important;
    padding: 0 2px !important;
}

div[class*="st-key-chat_widget_container"] .stButton > button:hover {
    background: #38bdf8 !important;
    color: #0f172a !important;
    border-color: #38bdf8 !important;
    font-weight: 700 !important;
}

/* Chat Messages */
[data-testid="stChatMessage"] {
    background: rgba(30, 41, 59, 0.75) !important;
    border: 1px solid rgba(255, 255, 255, 0.08) !important;
    border-radius: 12px !important;
    padding: 0.85rem 1rem !important;
    margin-bottom: 0.6rem !important;
}

[data-testid="stChatMessage"] p {
    color: #f1f5f9 !important;
    font-size: 0.95rem !important;
    line-height: 1.55 !important;
}

[data-testid="stChatMessage"] strong, 
[data-testid="stChatMessage"] b {
    color: #38bdf8 !important;
}

/* Chat Input */
[data-testid="stChatInput"] {
    border-color: #334155 !important;
}

[data-testid="stChatInput"] textarea {
    background-color: #1e293b !important;
    color: #ffffff !important;
    font-size: 0.95rem !important;
    border-radius: 10px !important;
}

[data-testid="stChatInput"] textarea::placeholder {
    color: #94a3b8 !important;
}

/* Alert Notification Badges */
[data-testid="stAlert"] {
    border-radius: 12px !important;
    font-weight: 600 !important;
}

[data-testid="stAlert"] * {
    color: #ffffff !important;
}
</style>
"""
st.markdown(FRIENDLY_CSS, unsafe_allow_html=True)

# Simple, everyday categories that anyone can enjoy
CATEGORIES = {
    "💻 Tech & AI": [
        "PYTHON", "ROBOT", "COMPUTER", "INTERNET",
        "CHATBOT", "LAPTOP", "CODING", "SMARTPHONE"
    ],
    "🦁 Animals": [
        "ELEPHANT", "DOLPHIN", "TIGER", "GIRAFFE",
        "PENGUIN", "KANGAROO", "LION", "MONKEY"
    ],
    "🌍 Countries": [
        "PAKISTAN", "TURKEY", "JAPAN", "CANADA",
        "BRAZIL", "GERMANY", "EGYPT", "FRANCE"
    ],
    "🎬 Movies & Fun": [
        "AVATAR", "TITANIC", "INCEPTION", "GLADIATOR",
        "FROZEN", "BATMAN", "SPIDERMAN"
    ]
}

# Classic, easy-to-see Hangman Stages (0 to 6 wrong guesses)
CLASSIC_HANGMAN_STAGES = [
    r"""
  +---+
  |   |
      |
      |
      |
      |
=========""",
    r"""
  +---+
  |   |
  O   |
      |
      |
      |
=========""",
    r"""
  +---+
  |   |
  O   |
  |   |
      |
      |
=========""",
    r"""
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========""",
    r"""
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========""",
    r"""
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========""",
    r"""
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
========="""
]

# Initialize AI Assistant
if "agent_instance" not in st.session_state:
    st.session_state.agent_instance = NexusAgent(
        developer_name="Sain Bux (Hadi Seelro)",
        contact_email="contact.sainbux@gmail.com"
    )

# Initialize Chatbot Widget State (Collapsed by default, opens in bottom-right corner)
if "chat_open" not in st.session_state:
    st.session_state.chat_open = False

# Initialize Session State
if "selected_category" not in st.session_state:
    st.session_state.selected_category = "💻 Tech & AI"

if "stats" not in st.session_state:
    st.session_state.stats = {"won": 0, "played": 0, "streak": 0}

if "chat_history" not in st.session_state:
    st.session_state.chat_history = [
        {"role": "assistant", "content": st.session_state.agent_instance.get_greeting()}
    ]

def start_new_game(category: str = None):
    """Starts a new clean round."""
    cat = category or st.session_state.selected_category
    st.session_state.selected_category = cat
    word_pool = CATEGORIES.get(cat, CATEGORIES["💻 Tech & AI"])
    
    prev_word = getattr(st.session_state, "word", "")
    choices = [w for w in word_pool if w != prev_word] or word_pool
    
    st.session_state.word = random.choice(choices).upper()
    st.session_state.guessed = []
    st.session_state.tries = 6
    st.session_state.status = "playing"
    st.session_state.feedback = None

if "word" not in st.session_state:
    start_new_game()

def check_win() -> bool:
    """Returns True if player guessed all letters."""
    return all(ch in st.session_state.guessed for ch in st.session_state.word)

def make_guess(letter: str):
    """Processes a guessed letter."""
    char = letter.strip().upper()
    if st.session_state.status != "playing":
        return

    if not char.isalpha() or len(char) != 1:
        st.session_state.feedback = ("warning", "Please pick a single letter from A to Z.")
        return

    if char in st.session_state.guessed:
        st.session_state.feedback = ("info", f"You already guessed '{char}'! Try a different one.")
        return

    st.session_state.guessed.append(char)

    if char in st.session_state.word:
        st.session_state.feedback = ("success", f"Nice! '{char}' is in the word! 🎉")
        if check_win():
            st.session_state.status = "won"
            st.session_state.stats["won"] += 1
            st.session_state.stats["played"] += 1
            st.session_state.stats["streak"] += 1
            st.session_state.chat_history.append({
                "role": "assistant",
                "content": f"🎉 **Awesome job!** You guessed the word **{st.session_state.word}**! Current winning streak: **{st.session_state.stats['streak']}**."
            })
    else:
        st.session_state.tries -= 1
        st.session_state.feedback = ("error", f"Oops! '{char}' is not in the word.")
        if st.session_state.tries <= 0:
            st.session_state.status = "lost"
            st.session_state.stats["played"] += 1
            st.session_state.stats["streak"] = 0
            st.session_state.chat_history.append({
                "role": "assistant",
                "content": f"😢 **Good effort!** The secret word was **{st.session_state.word}**. Click 'Play Again' to start a new game!"
            })


# ================== SIDEBAR: GAME GUIDE & STATS ==================
with st.sidebar:
    st.markdown("### 🎯 Hangman Portal")
    st.caption("Clean, distraction-free gameplay with 24/7 AI assistance.")
    
    # Quick launcher for corner AI Helper
    if st.button("💬 Open AI Chatbot", use_container_width=True):
        st.session_state.chat_open = True
        st.rerun()

    st.markdown("---")
    st.markdown("#### 📖 How to Play")
    st.markdown("""
    1. **Choose a category** from the top menu.
    2. **Click letters** on the virtual keyboard to guess.
    3. Correct letters appear in the secret word tiles.
    4. You have **6 chances** before the hangman is complete!
    5. Need a clue? Click the **floating AI bot in the corner**!
    """)

    st.markdown("---")
    st.markdown("#### 🏆 Quick Stats")
    win_pct = (
        int((st.session_state.stats["won"] / st.session_state.stats["played"]) * 100)
        if st.session_state.stats["played"] > 0
        else 0
    )
    st.markdown(f"• **Win Rate**: `{win_pct}%`")
    st.markdown(f"• **Current Streak**: `{st.session_state.stats['streak']} 🔥`")
    st.markdown(f"• **Total Solved**: `{st.session_state.stats['won']}` of `{st.session_state.stats['played']}`")

    st.markdown("---")
    st.markdown("""
        <div style="text-align:center; padding: 0.5rem 0;">
            <div style="font-size:0.95rem; font-weight:700; color:#38bdf8;">Sain Bux (Hadi Seelro)</div>
            <div style="font-size:0.85rem; color:#cbd5e1; margin-top:2px;">⭐ Agentic AI & Python Developer</div>
        </div>
    """, unsafe_allow_html=True)


# ================== MAIN GAMEPLAY SCREEN ==================

# Title & Category Selector
st.markdown('<div class="main-title">🎯 Hangman Game</div>', unsafe_allow_html=True)
st.markdown('<div class="main-subtitle">Guess the hidden word before you run out of lives!</div>', unsafe_allow_html=True)

# Top Bar: Category & Stats
stat_col1, stat_col2, stat_col3 = st.columns([1.5, 1, 1])

with stat_col1:
    new_cat = st.selectbox(
        "Choose Word Category:",
        options=list(CATEGORIES.keys()),
        index=list(CATEGORIES.keys()).index(st.session_state.selected_category)
    )
    if new_cat != st.session_state.selected_category:
        start_new_game(new_cat)
        st.rerun()

with stat_col2:
    st.metric("Winning Streak", f"{st.session_state.stats['streak']} 🔥")

with stat_col3:
    st.metric("Total Wins", f"{st.session_state.stats['won']} / {st.session_state.stats['played']}")

st.markdown("<br/>", unsafe_allow_html=True)

# Two-column layout: Left = Hangman Drawing, Right = Word & Keyboard
left_col, right_col = st.columns([1, 1.4], gap="large")

with left_col:
    st.markdown("### 🎨 Hangman Stage")
    
    # Display Hearts for lives left
    hearts = "❤️ " * st.session_state.tries + "🖤 " * (6 - st.session_state.tries)
    st.markdown(f"""
        <div class="lives-badge">
            <div class="lives-hearts">{hearts}</div>
            <div class="lives-text">{st.session_state.tries} of 6 Chances Remaining</div>
        </div>
    """, unsafe_allow_html=True)
    
    # Classic ASCII Hangman Drawing
    stage_idx = 6 - st.session_state.tries
    st.markdown(
        f'<div class="hangman-card"><div class="hangman-drawing">{CLASSIC_HANGMAN_STAGES[stage_idx]}</div></div>', 
        unsafe_allow_html=True
    )

with right_col:
    st.markdown("### 🔤 Secret Word")
    
    # Render modern visual letter tiles
    letter_tiles = []
    for ch in st.session_state.word:
        if ch in st.session_state.guessed:
            letter_tiles.append(f'<span class="letter-tile revealed">{ch}</span>')
        elif st.session_state.status == "lost":
            letter_tiles.append(f'<span class="letter-tile missed">{ch}</span>')
        else:
            letter_tiles.append('<span class="letter-tile blank">&nbsp;</span>')
    tiles_markup = " ".join(letter_tiles)

    st.markdown(f"""
        <div class="word-card">
            <div class="word-tiles-container">{tiles_markup}</div>
            <div class="word-info-footer">
                Category: <strong style="color: #38bdf8;">{st.session_state.selected_category}</strong> • 
                <strong style="color: #ffffff;">{len(st.session_state.word)} Letters</strong>
            </div>
        </div>
    """, unsafe_allow_html=True)

    # Feedback Notification
    if st.session_state.feedback:
        fb_type, fb_msg = st.session_state.feedback
        if fb_type == "success":
            st.success(fb_msg)
        elif fb_type == "error":
            st.error(fb_msg)
        elif fb_type == "warning":
            st.warning(fb_msg)
        else:
            st.info(fb_msg)

    # Win / Loss Result Announcements
    if st.session_state.status == "won":
        st.balloons()
        st.success(f"🎉 **CONGRATULATIONS, YOU WON!** You guessed **{st.session_state.word}**! Streak: **{st.session_state.stats['streak']}** 🔥")
    elif st.session_state.status == "lost":
        st.error(f"😢 **GAME OVER!** The secret word was **{st.session_state.word}**. Click 'Play Again' to retry!")

    # Virtual Keyboard (A - Z)
    st.markdown("##### ⌨️ Click a letter to guess:")
    
    keyboard_layout = [
        list("QWERTYUIOP"),
        list("ASDFGHJKL"),
        list("ZXCVBNM")
    ]
    
    for row in keyboard_layout:
        row_cols = st.columns(len(row))
        for idx, key_letter in enumerate(row):
            with row_cols[idx]:
                is_guessed = key_letter in st.session_state.guessed
                is_correct = is_guessed and (key_letter in st.session_state.word)
                is_wrong = is_guessed and (key_letter not in st.session_state.word)
                
                if is_correct:
                    label = f"✓ {key_letter}"
                    btn_type = "primary"
                elif is_wrong:
                    label = f"✗ {key_letter}"
                    btn_type = "secondary"
                else:
                    label = key_letter
                    btn_type = "secondary"
                
                if st.button(
                    label,
                    key=f"k_{key_letter}",
                    type=btn_type,
                    disabled=is_guessed or (st.session_state.status != "playing"),
                    use_container_width=True
                ):
                    make_guess(key_letter)
                    st.rerun()

    st.markdown("<div style='margin-top: 1.2rem;' class='main-game-actions'>", unsafe_allow_html=True)
    
    # Restart Button
    if st.button("🔄 Play Again / New Word", type="primary", use_container_width=True):
        start_new_game()
        st.rerun()

    st.markdown("</div>", unsafe_allow_html=True)


# ==============================================================================
# 🌐 FLOATING WEBSITE-STYLE CORNER CHATBOT WIDGET (DOCK IN BOTTOM-RIGHT CORNER)
# ==============================================================================

if not st.session_state.chat_open:
    # Collapsed State: Floating launcher button in the bottom-right corner
    with st.container(key="chat_launcher_container"):
        if st.button("💬 🤖 AI Helper", key="btn_open_floating_chat"):
            st.session_state.chat_open = True
            st.rerun()

else:
    # Expanded State: Floating interactive chat widget docked in the bottom-right corner
    with st.container(key="chat_widget_container"):
        # Header with Title & Close/Minimize Button
        hc1, hc2 = st.columns([5, 1])
        with hc1:
            st.markdown("<h4 style='margin:0; padding:0; color:#38bdf8;'>🤖 NEXUS AI Helper</h4>", unsafe_allow_html=True)
            st.caption("Ask for clues, rules, or developer info!")
        with hc2:
            if st.button("✖", key="close_chat_btn", help="Minimize Chat"):
                st.session_state.chat_open = False
                st.rerun()

        st.markdown("<hr style='margin: 0.4rem 0 0.8rem 0; border: none; border-top: 1px solid rgba(255,255,255,0.1);'>", unsafe_allow_html=True)

        # 4 Quick Action Buttons
        qc1, qc2 = st.columns(2)
        with qc1:
            if st.button("💡 Get Hint", key="cw_hint", use_container_width=True):
                ctx = {
                    "word": st.session_state.word,
                    "guessed": st.session_state.guessed,
                    "tries": st.session_state.tries,
                    "status": st.session_state.status
                }
                hint_txt = st.session_state.agent_instance.process_message("hint", ctx)
                st.session_state.chat_history.append({"role": "user", "content": "Can you give me a hint?"})
                st.session_state.chat_history.append({"role": "assistant", "content": hint_txt})
                st.rerun()

        with qc2:
            if st.button("🎮 How to Play", key="cw_rules", use_container_width=True):
                rules_txt = st.session_state.agent_instance.process_message("how to play")
                st.session_state.chat_history.append({"role": "user", "content": "How do I play this game?"})
                st.session_state.chat_history.append({"role": "assistant", "content": rules_txt})
                st.rerun()

        qc3, qc4 = st.columns(2)
        with qc3:
            if st.button("👨‍💻 Developer", key="cw_dev", use_container_width=True):
                dev_txt = st.session_state.agent_instance.process_message("developer")
                st.session_state.chat_history.append({"role": "user", "content": "Who built this app?"})
                st.session_state.chat_history.append({"role": "assistant", "content": dev_txt})
                st.rerun()

        with qc4:
            if st.button("🧹 Clear Chat", key="cw_clear", use_container_width=True):
                st.session_state.chat_history = [
                    {"role": "assistant", "content": st.session_state.agent_instance.get_greeting()}
                ]
                st.rerun()

        # Chat Conversation Area
        chat_scroll_box = st.container(height=260)
        with chat_scroll_box:
            for msg in st.session_state.chat_history:
                with st.chat_message(msg["role"]):
                    st.markdown(msg["content"])

        # Chat Input
        corner_input = st.chat_input("Ask a hint or question...", key="cw_chat_input")
        if corner_input:
            st.session_state.chat_history.append({"role": "user", "content": corner_input})
            ctx = {
                "word": st.session_state.word,
                "guessed": st.session_state.guessed,
                "tries": st.session_state.tries,
                "status": st.session_state.status
            }
            reply = st.session_state.agent_instance.process_message(corner_input, ctx)
            st.session_state.chat_history.append({"role": "assistant", "content": reply})
            st.rerun()
