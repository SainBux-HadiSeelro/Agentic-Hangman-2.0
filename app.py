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

# Clean, modern, and accessible CSS styling
FRIENDLY_CSS = """
<style>
@import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;600;700;800&family=JetBrains+Mono:wght@500;700&display=swap');

html, body, [class*="css"] {
    font-family: 'Plus Jakarta Sans', sans-serif;
}

/* Background */
.stApp {
    background: linear-gradient(135deg, #0f172a 0%, #1e293b 100%);
    color: #f8fafc;
}

/* Main Title */
.main-title {
    font-size: 2.2rem;
    font-weight: 800;
    text-align: center;
    color: #38bdf8;
    margin-bottom: 0.2rem;
}

.main-subtitle {
    text-align: center;
    font-size: 1rem;
    color: #94a3b8;
    margin-bottom: 1.5rem;
}

/* Friendly Card */
.game-card {
    background: rgba(30, 41, 59, 0.7);
    border: 1px solid rgba(255, 255, 255, 0.1);
    border-radius: 16px;
    padding: 1.5rem;
    box-shadow: 0 10px 25px rgba(0, 0, 0, 0.3);
    margin-bottom: 1rem;
}

/* Word Box */
.word-box {
    background: #090d16;
    border: 2px solid #38bdf8;
    border-radius: 14px;
    padding: 1.4rem;
    text-align: center;
    margin: 1rem 0;
}

.word-letters {
    font-family: 'JetBrains Mono', monospace;
    font-size: 2.4rem;
    font-weight: 800;
    letter-spacing: 0.6rem;
    color: #ffffff;
}

/* Hangman Drawing Display */
.hangman-drawing {
    background: #090d16;
    border: 1px solid #334155;
    border-radius: 12px;
    padding: 1.2rem;
    font-family: 'JetBrains Mono', monospace;
    font-size: 1rem;
    line-height: 1.3;
    color: #38bdf8;
    white-space: pre;
    text-align: center;
}

/* Lives / Hearts Bar */
.lives-display {
    font-size: 1.4rem;
    text-align: center;
    margin-bottom: 0.5rem;
}

/* Button styling */
.stButton>button {
    border-radius: 10px;
    font-weight: 700;
    transition: all 0.2s ease-in-out;
}

.stButton>button:hover {
    transform: translateY(-2px);
    box-shadow: 0 4px 12px rgba(56, 189, 248, 0.3);
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
    """
       +---+
       |   |
           |
           |
           |
           |
    =========
    """,
    """
       +---+
       |   |
       O   |
           |
           |
           |
    =========
    """,
    """
       +---+
       |   |
       O   |
       |   |
           |
           |
    =========
    """,
    """
       +---+
       |   |
       O   |
      /|   |
           |
           |
    =========
    """,
    """
       +---+
       |   |
       O   |
      /|\\  |
           |
           |
    =========
    """,
    """
       +---+
       |   |
       O   |
      /|\\  |
      /    |
           |
    =========
    """,
    """
       +---+
       |   |
       O   |
      /|\\  |
      / \\  |
           |
    =========
    """
]

# Initialize AI Assistant
if "agent_instance" not in st.session_state:
    st.session_state.agent_instance = NexusAgent(
        developer_name="Sain Bux (Hadi Seelro)",
        contact_email="contact.sainbux@gmail.com"
    )

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

def get_display_word() -> str:
    """Shows letters guessed and underscores for remaining letters."""
    return " ".join([ch if ch in st.session_state.guessed else "_" for ch in st.session_state.word])

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


# ================== SIDEBAR: FRIENDLY AI HELPER ==================
with st.sidebar:
    st.markdown("### 🤖 Friendly AI Helper (NEXUS)")
    st.caption("Ask for easy hints or learn about the developer!")

    # 4 Quick Action Buttons
    col_s1, col_s2 = st.columns(2)
    with col_s1:
        if st.button("💡 Get a Hint", use_container_width=True):
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

    with col_s2:
        if st.button("🎮 How to Play", use_container_width=True):
            rules_txt = st.session_state.agent_instance.process_message("how to play")
            st.session_state.chat_history.append({"role": "user", "content": "How do I play this game?"})
            st.session_state.chat_history.append({"role": "assistant", "content": rules_txt})
            st.rerun()

    col_s3, col_s4 = st.columns(2)
    with col_s3:
        if st.button("👨‍💻 Developer", use_container_width=True):
            dev_txt = st.session_state.agent_instance.process_message("developer")
            st.session_state.chat_history.append({"role": "user", "content": "Who built this app?"})
            st.session_state.chat_history.append({"role": "assistant", "content": dev_txt})
            st.rerun()

    with col_s4:
        if st.button("🧹 Clear Chat", use_container_width=True):
            st.session_state.chat_history = [
                {"role": "assistant", "content": st.session_state.agent_instance.get_greeting()}
            ]
            st.rerun()

    # Chat Conversation Area
    chat_box = st.container(height=360)
    with chat_box:
        for msg in st.session_state.chat_history:
            with st.chat_message(msg["role"]):
                st.markdown(msg["content"])

    # Chat Input
    user_input = st.chat_input("Ask a question or ask for a hint...")
    if user_input:
        st.session_state.chat_history.append({"role": "user", "content": user_input})
        ctx = {
            "word": st.session_state.word,
            "guessed": st.session_state.guessed,
            "tries": st.session_state.tries,
            "status": st.session_state.status
        }
        reply = st.session_state.agent_instance.process_message(user_input, ctx)
        st.session_state.chat_history.append({"role": "assistant", "content": reply})
        st.rerun()

    st.markdown("---")
    st.markdown("""
        <div style="text-align:center; font-size:0.85rem; color:#94a3b8;">
            Made by <b>Sain Bux (Hadi Seelro)</b><br/>
            ⭐ <i>Agentic AI & Python Developer</i>
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
    st.markdown(f'<div class="lives-display">Lives: {hearts}</div>', unsafe_allow_html=True)
    
    # Classic ASCII Hangman Drawing
    stage_idx = 6 - st.session_state.tries
    st.markdown(f'<div class="hangman-drawing">{CLASSIC_HANGMAN_STAGES[stage_idx]}</div>', unsafe_allow_html=True)

with right_col:
    st.markdown("### 🔤 Secret Word")
    
    # Secret Word Blanks
    word_text = get_display_word()
    st.markdown(f"""
        <div class="word-box">
            <div class="word-letters">{word_text}</div>
            <div style="font-size:0.9rem; color:#94a3b8; margin-top:8px;">
                Category: <b>{st.session_state.selected_category}</b> • {len(st.session_state.word)} Letters
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
        st.success(f"🎉 **CONGRATULATIONS, YOU WON!** The word was **{st.session_state.word}**!")
    elif st.session_state.status == "lost":
        st.error(f"😢 **GAME OVER!** The word was **{st.session_state.word}**.")

    # Virtual Keyboard (A - Z)
    st.markdown("**Click a letter to guess:**")
    
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
                elif is_wrong:
                    label = f"✗ {key_letter}"
                else:
                    label = key_letter
                
                if st.button(
                    label,
                    key=f"k_{key_letter}",
                    disabled=is_guessed or (st.session_state.status != "playing"),
                    use_container_width=True
                ):
                    make_guess(key_letter)
                    st.rerun()

    st.markdown("<br/>", unsafe_allow_html=True)
    
    # Restart Button
    if st.button("🔄 Play Again / New Word", type="primary", use_container_width=True):
        start_new_game()
        st.rerun()
