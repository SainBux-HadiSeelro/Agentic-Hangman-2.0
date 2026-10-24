"""
🎯 NEXUS HANGMAN: CYBERPUNK AGENTIC AI EDITION
Architected by an Agentic AI Developer.
Features:
- 24/7 Autonomous AI Resident Agent (NEXUS-7) for Game Hints & Portfolio Inquiries
- High-Tech Cyber Terminal Hangman Visualizer & Core Containment Gauge
- Interactive On-Screen Cyber Keyboard + Quick Keyboard Input
- Multi-Category Word Engine (Agentic AI, Python Engineering, Quantum Cybernetics)
- Comprehensive Session Statistics & Persistent Streak Tracking
"""

import streamlit as st
import random
from typing import Dict, List
from agent import NexusAgent

# Set Page Config with futuristic title and layout
st.set_page_config(
    page_title="NEXUS // Agentic Hangman Cyber-Terminal",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom Cyberpunk & Glassmorphic CSS Styling
CYBER_CSS = """
<style>
@import url('https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@400;600;800&family=Orbitron:wght@500;700;900&display=swap');

:root {
    --neon-cyan: #00f0ff;
    --neon-magenta: #ff007f;
    --neon-purple: #9d4edd;
    --neon-green: #00ff66;
    --neon-red: #ff3344;
    --cyber-dark: #070b12;
    --card-bg: rgba(13, 20, 36, 0.78);
    --border-glow: rgba(0, 240, 255, 0.35);
}

/* Background & Core Fonts */
.stApp {
    background: radial-gradient(circle at 15% 15%, #0f172a 0%, #070b12 85%);
    font-family: 'JetBrains Mono', monospace;
    color: #e2e8f0;
}

h1, h2, h3, h4, .cyber-font {
    font-family: 'Orbitron', sans-serif !important;
    letter-spacing: 1.5px;
}

/* Cyber Title Glow */
.cyber-title {
    font-size: 2.3rem;
    font-weight: 900;
    text-align: center;
    background: linear-gradient(135deg, #00f0ff 0%, #a855f7 50%, #ff007f 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    text-shadow: 0 0 25px rgba(0, 240, 255, 0.3);
    margin-bottom: 0.2rem;
}

.cyber-subtitle {
    text-align: center;
    font-size: 0.85rem;
    color: #94a3b8;
    text-transform: uppercase;
    letter-spacing: 3px;
    margin-bottom: 1.5rem;
}

/* Glassmorphism Containers */
.cyber-card {
    background: var(--card-bg);
    border: 1px solid var(--border-glow);
    border-radius: 14px;
    padding: 1.2rem;
    box-shadow: 0 8px 32px 0 rgba(0, 0, 0, 0.45);
    backdrop-filter: blur(10px);
    margin-bottom: 1rem;
}

/* Word Display */
.word-display-box {
    background: rgba(4, 9, 20, 0.85);
    border: 2px solid var(--neon-cyan);
    border-radius: 12px;
    padding: 1.2rem;
    text-align: center;
    box-shadow: 0 0 20px rgba(0, 240, 255, 0.25) inset, 0 0 15px rgba(0, 240, 255, 0.2);
    margin-bottom: 1rem;
}

.word-display-text {
    font-family: 'JetBrains Mono', monospace;
    font-size: 2.2rem;
    font-weight: 800;
    letter-spacing: 0.6rem;
    color: #ffffff;
    text-shadow: 0 0 10px var(--neon-cyan);
}

/* ASCII Terminal Stage Box */
.terminal-stage-box {
    background: #020610;
    border: 1px solid #1e293b;
    border-left: 3px solid var(--neon-cyan);
    border-radius: 10px;
    padding: 1rem;
    font-family: 'JetBrains Mono', monospace;
    font-size: 0.85rem;
    line-height: 1.25;
    color: #38bdf8;
    white-space: pre;
    box-shadow: 0 4px 20px rgba(0,0,0,0.6);
}

/* Live Agent Online Pill */
.agent-pill {
    display: inline-flex;
    align-items: center;
    gap: 8px;
    background: rgba(0, 255, 102, 0.12);
    border: 1px solid #00ff66;
    color: #00ff66;
    padding: 4px 14px;
    border-radius: 20px;
    font-size: 0.8rem;
    font-weight: 700;
    letter-spacing: 1px;
}

.agent-pulse {
    width: 8px;
    height: 8px;
    background-color: #00ff66;
    border-radius: 50%;
    box-shadow: 0 0 10px #00ff66;
}

/* Button enhancements */
.stButton>button {
    border-radius: 8px;
    font-family: 'JetBrains Mono', monospace;
    font-weight: 700;
    transition: all 0.25s ease-in-out;
}

.stButton>button:hover {
    border-color: var(--neon-cyan);
    box-shadow: 0 0 14px rgba(0, 240, 255, 0.4);
    transform: translateY(-1px);
}
</style>
"""
st.markdown(CYBER_CSS, unsafe_allow_html=True)

# Word Database Categorized by Themes
WORD_DATABASE = {
    "Agentic AI & LLMs": [
        "AUTONOMOUS", "REASONING", "EMBEDDING", "TRANSFORMER",
        "WORKFLOW", "MULTIMODAL", "LANGCHAIN", "FINE_TUNING",
        "AGENT", "PROMPT"
    ],
    "Python & Engineering": [
        "STREAMLIT", "ASYNCHRONOUS", "ALGORITHM", "FRAMEWORK",
        "CONTAINER", "DECORATOR", "GENERATOR", "BYTECODE"
    ],
    "Cybernetics & Deep Tech": [
        "QUANTUM", "CYBERNETICS", "NEURAL_NET", "METAVERSE"
    ]
}

# Cybernetic Hangman ASCII Visualizer Stages (0 to 6 errors)
CYBER_HANGMAN_STAGES = [
    """
  ╔═════════════════════════════════════╗
  ║ 🛡️ CORE CONTAINMENT: 100% (STABLE)  ║
  ║                                     ║
  ║      ┌───────────────┐              ║
  ║      │  [AI NEXUS]   │              ║
  ║      │  ALL SYSTEMS  │              ║
  ║      │    OPTIMAL    │              ║
  ║      └───────┬───────┘              ║
  ║              │                      ║
  ║         ○────┴────○                 ║
  ║         │  READY  │                 ║
  ║         ○─────────○                 ║
  ╚═════════════════════════════════════╝
    """,
    """
  ╔═════════════════════════════════════╗
  ║ ⚠️ WARNING: CONTAINMENT AT 83%      ║
  ║                                     ║
  ║      ┌───────────────┐              ║
  ║      │  CORE WARNING │              ║
  ║      │  FIREWALL -1  │              ║
  ║      └───────┬───────┘              ║
  ║              │                      ║
  ║           [ 0 _ 0 ]   <-- Anomaly   ║
  ║                                     ║
  ║                                     ║
  ╚═════════════════════════════════════╝
    """,
    """
  ╔═════════════════════════════════════╗
  ║ ⚠️ ALERT: CONTAINMENT AT 66%        ║
  ║                                     ║
  ║      ┌───────────────┐              ║
  ║      │  SUBROUTINE   │              ║
  ║      │  BREACHED     │              ║
  ║      └───────┬───────┘              ║
  ║              │                      ║
  ║           [ X _ O ]                 ║
  ║              │                      ║
  ║              │                      ║
  ╚═════════════════════════════════════╝
    """,
    """
  ╔═════════════════════════════════════╗
  ║ ⚡ DANGER: CONTAINMENT AT 50%       ║
  ║                                     ║
  ║      ┌───────────────┐              ║
  ║      │  HEURISTIC    │              ║
  ║      │  FAULT ACTIVE │              ║
  ║      └───────┬───────┘              ║
  ║              │                      ║
  ║           [ X _ X ]                 ║
  ║             /│                      ║
  ║            / │                      ║
  ╚═════════════════════════════════════╝
    """,
    """
  ╔═════════════════════════════════════╗
  ║ 🚨 CRITICAL: CONTAINMENT AT 33%     ║
  ║                                     ║
  ║      ┌───────────────┐              ║
  ║      │  POWER CORE   │              ║
  ║      │  DESTABILIZED │              ║
  ║      └───────┬───────┘              ║
  ║              │                      ║
  ║           [ ! _ ! ]                 ║
  ║             /│\\                    ║
  ║            / │ \\                   ║
  ╚═════════════════════════════════════╝
    """,
    """
  ╔═════════════════════════════════════╗
  ║ 🔥 CODE RED: CONTAINMENT AT 16%     ║
  ║                                     ║
  ║      ┌───────────────┐              ║
  ║      │ EMERGENCY PROTOCOL           ║
  ║      │ 1 CHANCE REMAINS             ║
  ║      └───────┬───────┘              ║
  ║              │                      ║
  ║           [ 💀_💀 ]                 ║
  ║             /│\\                    ║
  ║             /                       ║
  ╚═════════════════════════════════════╝
    """,
    """
  ╔═════════════════════════════════════╗
  ║ 💀 BREACH COMPLETE: MAINFRAME LOST  ║
  ║                                     ║
  ║      ┌───────────────┐              ║
  ║      │ CRITICAL FAIL │              ║
  ║      │ SYSTEM PURGED │              ║
  ║      └───────┬───────┘              ║
  ║              │                      ║
  ║           [ ✖ _ ✖ ]                 ║
  ║             /│\\                    ║
  ║             / \\                     ║
  ╚═════════════════════════════════════╝
    """
]

# Initialize Nexus Agent Instance
if "agent_instance" not in st.session_state:
    st.session_state.agent_instance = NexusAgent(
        developer_name="Sain Bux (Hadi Seelro)",
        contact_email="contact.sainbux@gmail.com"
    )

# Initialize Session State Variables
if "selected_category" not in st.session_state:
    st.session_state.selected_category = "Agentic AI & LLMs"

if "max_tries" not in st.session_state:
    st.session_state.max_tries = 6

if "stats" not in st.session_state:
    st.session_state.stats = {
        "played": 0,
        "won": 0,
        "streak": 0,
        "best_streak": 0
    }

if "chat_history" not in st.session_state:
    st.session_state.chat_history = [
        {"role": "assistant", "content": st.session_state.agent_instance.get_greeting()}
    ]

def start_new_game(category: str = None):
    """Resets the game state cleanly with a new word."""
    cat = category or st.session_state.selected_category
    st.session_state.selected_category = cat
    words = WORD_DATABASE.get(cat, WORD_DATABASE["Agentic AI & LLMs"])
    
    # Pick a new word different from previous if possible
    prev_word = getattr(st.session_state, "word", "")
    available_words = [w for w in words if w != prev_word] or words
    
    st.session_state.word = random.choice(available_words).upper()
    st.session_state.guessed = []
    st.session_state.tries = st.session_state.max_tries
    st.session_state.status = "playing"
    st.session_state.feedback_msg = None
    st.session_state.feedback_type = "info"

# Trigger initial game setup if not present
if "word" not in st.session_state:
    start_new_game()

def get_display_word() -> str:
    """Returns the formatted masked word with guessed characters."""
    return " ".join([ch if ch in st.session_state.guessed else "_" for ch in st.session_state.word])

def is_word_decrypted() -> bool:
    """Checks if all letters of secret word have been guessed."""
    return all(ch in st.session_state.guessed for ch in st.session_state.word)

def submit_guess(letter: str):
    """Processes a single character guess."""
    char = letter.strip().upper()
    
    if st.session_state.status != "playing":
        return

    if not char.isalpha() or len(char) != 1:
        st.session_state.feedback_msg = "⚠️ Input error: Enter a single alphabetic character."
        st.session_state.feedback_type = "warning"
        return

    if char in st.session_state.guessed:
        st.session_state.feedback_msg = f"ℹ️ Signal repeated: Letter '{char}' has already been scanned!"
        st.session_state.feedback_type = "info"
        return

    st.session_state.guessed.append(char)

    if char in st.session_state.word:
        st.session_state.feedback_msg = f"✅ Signal match! '{char}' is part of the encryption key."
        st.session_state.feedback_type = "success"
        
        if is_word_decrypted():
            st.session_state.status = "won"
            st.session_state.stats["played"] += 1
            st.session_state.stats["won"] += 1
            st.session_state.stats["streak"] += 1
            if st.session_state.stats["streak"] > st.session_state.stats["best_streak"]:
                st.session_state.stats["best_streak"] = st.session_state.stats["streak"]
            
            # Agent congrats message in chat
            st.session_state.chat_history.append({
                "role": "assistant",
                "content": f"🎉 **SYSTEM DECRYPTED!** Outstanding work, Operative. The target sequence was **{st.session_state.word}**!\n\n"
                           f"Current winning streak: **{st.session_state.stats['streak']}**."
            })
    else:
        st.session_state.tries -= 1
        st.session_state.feedback_msg = f"❌ Signal rejected! '{char}' is NOT in the target sequence."
        st.session_state.feedback_type = "error"
        
        if st.session_state.tries <= 0:
            st.session_state.status = "lost"
            st.session_state.stats["played"] += 1
            st.session_state.stats["streak"] = 0
            
            # Agent alert message in chat
            st.session_state.chat_history.append({
                "role": "assistant",
                "content": f"💀 **CONTAINMENT BREACHED!** The encrypted word was **{st.session_state.word}**.\n\n"
                           f"Ready to reboot the mainframe and try again?"
            })

# ----------------- SIDEBAR: 24/7 AGENT NEXUS-7 CONSOLE -----------------
with st.sidebar:
    st.markdown("""
        <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:12px;">
            <span style="font-family:'Orbitron', sans-serif; font-size:1.15rem; font-weight:800; color:#00f0ff;">
                🤖 NEXUS-7 AI
            </span>
            <div class="agent-pill">
                <div class="agent-pulse"></div> 24/7 LIVE
            </div>
        </div>
    """, unsafe_allow_html=True)

    st.caption("Autonomous Agentic Assistant for Game Strategy & Portfolio Intelligence.")

    # Quick Action Buttons for Visitors
    st.markdown("**⚡ Instant Agent Commands:**")
    col_a1, col_a2 = st.columns(2)
    with col_a1:
        if st.button("💡 Get Hint", use_container_width=True):
            game_ctx = {
                "word": st.session_state.word,
                "guessed": st.session_state.guessed,
                "tries": st.session_state.tries,
                "status": st.session_state.status
            }
            hint_reply = st.session_state.agent_instance.process_message("hint", game_ctx)
            st.session_state.chat_history.append({"role": "user", "content": "Requesting tactical decryption hint."})
            st.session_state.chat_history.append({"role": "assistant", "content": hint_reply})
            st.rerun()

    with col_a2:
        if st.button("👨‍💻 Portfolio", use_container_width=True):
            profile_reply = st.session_state.agent_instance.process_message("developer info")
            st.session_state.chat_history.append({"role": "user", "content": "Show developer portfolio details."})
            st.session_state.chat_history.append({"role": "assistant", "content": profile_reply})
            st.rerun()

    col_b1, col_b2 = st.columns(2)
    with col_b1:
        if st.button("🚀 Hire/Contact", use_container_width=True):
            hire_reply = st.session_state.agent_instance.process_message("hire developer")
            st.session_state.chat_history.append({"role": "user", "content": "How can I hire or contact the developer?"})
            st.session_state.chat_history.append({"role": "assistant", "content": hire_reply})
            st.rerun()

    with col_b2:
        if st.button("🧹 Clear Chat", use_container_width=True):
            st.session_state.chat_history = [
                {"role": "assistant", "content": st.session_state.agent_instance.get_greeting()}
            ]
            st.rerun()

    # Chat Scroll Area
    chat_container = st.container(height=360)
    with chat_container:
        for msg in st.session_state.chat_history:
            with st.chat_message(msg["role"]):
                st.markdown(msg["content"])

    # Chat Input Box
    user_query = st.chat_input("Ask NEXUS-7 anything (hints, portfolio, specs)...")
    if user_query:
        st.session_state.chat_history.append({"role": "user", "content": user_query})
        game_ctx = {
            "word": st.session_state.word,
            "guessed": st.session_state.guessed,
            "tries": st.session_state.tries,
            "status": st.session_state.status
        }
        agent_resp = st.session_state.agent_instance.process_message(user_query, game_ctx)
        st.session_state.chat_history.append({"role": "assistant", "content": agent_resp})
        st.rerun()

    st.markdown("---")
    
    # Portfolio Link & Contact Badge
    st.markdown("""
        <div style="font-size:0.8rem; color:#94a3b8; text-align:center;">
            ⚡ <b>Architected with Pride</b><br/>
            Engineered by an <b style="color:#00f0ff;">Agentic AI Developer</b><br/>
            💼 <i>Open for AI Agent & Full-Stack Contracts</i>
        </div>
    """, unsafe_allow_html=True)


# ----------------- MAIN TERMINAL INTERFACE -----------------

# Header Section
st.markdown('<div class="cyber-title">⚡ NEXUS // HANGMAN TERMINAL ⚡</div>', unsafe_allow_html=True)
st.markdown('<div class="cyber-subtitle">Autonomous Agentic AI Edition • Quantum Heuristic Decryption</div>', unsafe_allow_html=True)

# Top Control & Stats Bar
metric_col1, metric_col2, metric_col3, metric_col4 = st.columns(4)

win_rate = (st.session_state.stats["won"] / st.session_state.stats["played"] * 100) if st.session_state.stats["played"] > 0 else 0.0

with metric_col1:
    st.metric("Containment Integrity", f"{int((st.session_state.tries / st.session_state.max_tries) * 100)}%", delta=f"{st.session_state.tries} Tries Left")
with metric_col2:
    st.metric("Win Streak", f"{st.session_state.stats['streak']} 🔥", delta=f"Best: {st.session_state.stats['best_streak']}")
with metric_col3:
    st.metric("Decryption Rate", f"{win_rate:.0f}%", delta=f"{st.session_state.stats['won']}/{st.session_state.stats['played']} Won")
with metric_col4:
    selected_cat = st.selectbox(
        "Mission Vector (Category)",
        options=list(WORD_DATABASE.keys()),
        index=list(WORD_DATABASE.keys()).index(st.session_state.selected_category),
        key="cat_selector"
    )
    if selected_cat != st.session_state.selected_category:
        start_new_game(selected_cat)
        st.rerun()

st.markdown("<br/>", unsafe_allow_html=True)

# Two-column Gameplay Layout
col_visualizer, col_gameplay = st.columns([1, 1.2], gap="medium")

# 1. Visualizer Column: Cyber ASCII Mainframe
with col_visualizer:
    st.markdown("### 🖥️ Mainframe Core Status")
    
    stage_idx = min(6, st.session_state.max_tries - st.session_state.tries)
    ascii_stage = CYBER_HANGMAN_STAGES[stage_idx]
    
    st.markdown(f'<div class="terminal-stage-box">{ascii_stage}</div>', unsafe_allow_html=True)
    
    # Progress Bar with dynamic warning color
    health_ratio = st.session_state.tries / st.session_state.max_tries
    st.progress(health_ratio, text=f"Core Containment: {int(health_ratio * 100)}%")

# 2. Gameplay Column: Target Word, Virtual Cyber Keyboard, and Controls
with col_gameplay:
    st.markdown("### 🎯 Decryption Target")
    
    # Render Hidden/Decrypted Word
    display_str = get_display_word()
    st.markdown(f"""
        <div class="word-display-box">
            <div class="word-display-text">{display_str}</div>
            <div style="font-size:0.8rem; color:#64748b; margin-top:8px;">
                SECURITY HASH: <code>{len(st.session_state.word)} CHARACTERS</code> • CATEGORY: <code>{st.session_state.selected_category.upper()}</code>
            </div>
        </div>
    """, unsafe_allow_html=True)

    # Feedback Alert Banner
    if st.session_state.feedback_msg:
        if st.session_state.feedback_type == "success":
            st.success(st.session_state.feedback_msg)
        elif st.session_state.feedback_type == "error":
            st.error(st.session_state.feedback_msg)
        elif st.session_state.feedback_type == "warning":
            st.warning(st.session_state.feedback_msg)
        else:
            st.info(st.session_state.feedback_msg)

    # Game State Outcome Banners
    if st.session_state.status == "won":
        st.balloons()
        st.markdown(f"""
            <div style="background:rgba(0, 255, 102, 0.15); border:2px solid #00ff66; border-radius:12px; padding:16px; text-align:center; margin-bottom:14px;">
                <h2 style="color:#00ff66; margin:0;">🎉 SEQUENCE DECRYPTED SUCCESSFULLY!</h2>
                <p style="margin:6px 0 0 0; color:#e2e8f0;">Target Identity: <b style="color:#00f0ff; letter-spacing:2px;">{st.session_state.word}</b></p>
            </div>
        """, unsafe_allow_html=True)
    elif st.session_state.status == "lost":
        st.markdown(f"""
            <div style="background:rgba(255, 51, 68, 0.15); border:2px solid #ff3344; border-radius:12px; padding:16px; text-align:center; margin-bottom:14px;">
                <h2 style="color:#ff3344; margin:0;">💀 CONTAINMENT FAILURE - SYSTEM PURGED</h2>
                <p style="margin:6px 0 0 0; color:#e2e8f0;">Classified Keyword Was: <b style="color:#ff007f; letter-spacing:2px;">{st.session_state.word}</b></p>
            </div>
        """, unsafe_allow_html=True)

    # Virtual Cyber Keyboard (A-Z)
    st.markdown("**🔠 Virtual Cyber Decryption Keypad:**")
    
    keyboard_rows = [
        list("QWERTYUIOP"),
        list("ASDFGHJKL"),
        list("ZXCVBNM")
    ]
    
    for row in keyboard_rows:
        row_cols = st.columns(len(row))
        for idx, key_char in enumerate(row):
            with row_cols[idx]:
                is_guessed = key_char in st.session_state.guessed
                is_correct = is_guessed and (key_char in st.session_state.word)
                is_wrong = is_guessed and (key_char not in st.session_state.word)
                
                # Dynamic button label & state
                if is_correct:
                    btn_label = f"✓ {key_char}"
                elif is_wrong:
                    btn_label = f"✗ {key_char}"
                else:
                    btn_label = key_char
                
                if st.button(
                    btn_label,
                    key=f"btn_{key_char}",
                    disabled=is_guessed or (st.session_state.status != "playing"),
                    use_container_width=True
                ):
                    submit_guess(key_char)
                    st.rerun()

    st.markdown("<br/>", unsafe_allow_html=True)

    # Quick Manual Input & Action Bar
    ctrl_col1, ctrl_col2 = st.columns([1.5, 1])
    
    with ctrl_col1:
        with st.form("manual_guess_form", clear_on_submit=True):
            input_col1, input_col2 = st.columns([2, 1])
            with input_col1:
                manual_letter = st.text_input(
                    "Manual Signal Input:",
                    max_chars=1,
                    placeholder="Type key...",
                    label_visibility="collapsed",
                    disabled=(st.session_state.status != "playing")
                )
            with input_col2:
                submitted = st.form_submit_tag = st.form_submit_button("Transmit ⚡", use_container_width=True, disabled=(st.session_state.status != "playing"))
                if submitted and manual_letter:
                    submit_guess(manual_letter)
                    st.rerun()

    with ctrl_col2:
        if st.button("🔄 Reboot Terminal", use_container_width=True, type="primary"):
            start_new_game()
            st.rerun()

# Footer Information
st.markdown("---")
footer_col1, footer_col2, footer_col3 = st.columns([1, 1, 1])
with footer_col1:
    st.caption("🛡️ **System Architecture**: Modular Reactive Streamlit + AI State Engine")
with footer_col2:
    st.caption("🤖 **AI Agent**: NEXUS-7 Live (Zero-Downtime Autonomous Support)")
with footer_col3:
    st.caption("🚀 **Portfolio Edition**: Built for Enterprise & AI Demonstrations")
