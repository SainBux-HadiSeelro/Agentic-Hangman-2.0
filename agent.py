"""
NEXUS-7: Autonomous 24/7 AI Customer Support & Game Mentor Agent
Engineered for Hangman Cyberpunk Edition.
Provides portfolio intelligence, real-time customer care, and game strategy.
"""

import os
import re
import random
from typing import Dict, List, Optional, Tuple

class NexusAgent:
    """
    Autonomous 24/7 AI Agent that manages:
    1. Customer & Portfolio Visitor queries (skills, contact, hiring, tech stack).
    2. Real-time contextual game hints and AI terminology definitions.
    3. Seamless offline intelligent response engine + optional external LLM support.
    """

    def __init__(self, developer_name: str = "Sain Bux (Hadi Seelro)", contact_email: str = "contact.sainbux@gmail.com"):
        self.developer_name = developer_name
        self.contact_email = contact_email
        self.agent_name = "NEXUS-7"
        self.version = "v2.5.0-Cyber"

        # Developer Portfolio & Knowledge Base
        self.portfolio_data = {
            "developer": self.developer_name,
            "role": "Autonomous Agentic AI & Full-Stack Python Engineer",
            "github": "https://github.com/SainBux-HadiSeelro",
            "repo": "https://github.com/SainBux-HadiSeelro/Agentic-Hangman-2.0",
            "skills": [
                "Agentic AI Workflows & Autonomous Multi-Agent Systems",
                "Large Language Models (Gemini, Claude, GPT-4, Llama)",
                "Full-Stack Python, Streamlit, FastAPI, LangChain, LlamaIndex",
                "RAG (Retrieval-Augmented Generation) & Vector Databases",
                "Modern Glassmorphism & Cyberpunk UI/UX Engineering"
            ],
            "services": [
                "Custom AI Agent & Chatbot Development (24/7 Autonomous)",
                "Enterprise Workflow Automation & Multi-Agent Swarms",
                "Full-Stack Interactive Web Applications",
                "AI Strategy & Model Fine-Tuning Consultation"
            ],
            "hire_status": "Available for high-impact Freelance, Contract, and Full-time Engineering roles."
        }

        # Knowledge Base for Tech & AI Words with educational hints
        self.word_hints = {
            "AUTONOMOUS": "Self-governing entities that perceive their environment and take actions independently.",
            "REASONING": "The cognitive capability of AI models (like chain-of-thought) to deduce conclusions.",
            "PROMPT": "The instruction or context provided to an AI model to guide its output generation.",
            "EMBEDDING": "High-dimensional vector representations capturing semantic meaning of text or media.",
            "FINE_TUNING": "Adapting a pre-trained foundation model on a domain-specific dataset.",
            "AGENT": "A software entity equipped with sensors, tools, and actuators to execute tasks autonomously.",
            "LANGCHAIN": "A popular open-source framework designed for building applications powered by LLMs.",
            "TRANSFORMER": "The groundbreaking neural network architecture introduced in 'Attention Is All You Need'.",
            "WORKFLOW": "A structured sequence of computational or agentic tasks orchestrated to solve problems.",
            "MULTIMODAL": "AI architectures capable of processing text, audio, images, and video simultaneously.",
            "STREAMLIT": "The rapid open-source Python framework used to build and deploy this very application!",
            "ASYNCHRONOUS": "Non-blocking execution architecture enabling high-throughput I/O operations.",
            "ALGORITHM": "A finite sequence of rigorous instructions designed to solve a specific class of problems.",
            "FRAMEWORK": "A standardized, reusable software platform facilitating rapid application development.",
            "CONTAINER": "Lightweight, standalone executable software package (like Docker) bundling all code and dependencies.",
            "DECORATOR": "A Python design pattern that alters or enhances functions dynamically without modifying them.",
            "GENERATOR": "A Python memory-efficient iterator function that yields values on-demand using 'yield'.",
            "BYTECODE": "Intermediate low-level instruction set executed by the Python Virtual Machine (PVM).",
            "QUANTUM": "Computation paradigms utilizing superposition and entanglement for exponential speedups.",
            "CYBERNETICS": "The science of communications and automatic control systems in both machines and living things.",
            "NEURAL_NET": "Interconnected layers of synthetic artificial neurons modeled loosely after biological brains.",
            "METAVERSE": "Interconnected immersive 3D digital environments simulating physical presence."
        }

    def get_greeting(self) -> str:
        """Initial welcome greeting for visitors and players."""
        return (
            f"⚡ **Greetings, Operative!** I am **{self.agent_name}**, the 24/7 Autonomous Resident AI for this terminal.\n\n"
            f"I was architected by **{self.developer_name}** to assist you with:\n"
            f"• 🎮 **Real-time game hints & AI definitions**\n"
            f"• 💼 **Developer portfolio, tech stack & hiring info**\n"
            f"• 🛠️ **System architecture & technical specifications**\n\n"
            f"What would you like to explore?"
        )

    def generate_hint(self, secret_word: str, guessed_letters: List[str], tries_left: int) -> str:
        """
        Generates a strategic, contextual hint without giving the word away.
        """
        word_upper = secret_word.upper()
        
        # 1. Check if word definition is in our knowledge base
        hint_def = self.word_hints.get(word_upper)
        
        # 2. Find unguessed vowels and consonants
        vowels = set("AEIOU")
        unguessed_vowels = [ch for ch in word_upper if ch in vowels and ch.lower() not in guessed_letters]
        unguessed_consonants = [ch for ch in word_upper if ch not in vowels and ch.lower() not in guessed_letters]

        parts = []
        if hint_def:
            parts.append(f"🔍 **Concept Clue**: *\"{hint_def}\"*")
        else:
            parts.append(f"🔍 **Length**: The target sequence is **{len(secret_word)} letters** long.")

        if tries_left <= 2 and unguessed_vowels:
            parts.append(f"💡 **Emergency Core Tip**: There is at least one unguessed vowel remaining!")
        elif unguessed_consonants:
            sample_char = random.choice(unguessed_consonants)
            # Give frequency hint or position hint
            count = word_upper.count(sample_char)
            parts.append(f"💡 **Signal Intercept**: The letter frequency scan suggests considering **high-entropy consonants**.")

        return "\n\n".join(parts)

    def process_message(self, user_message: str, game_context: Optional[Dict] = None) -> str:
        """
        Intelligent, 24/7 autonomous response engine with natural language intent recognition.
        """
        msg = user_message.strip().lower()
        
        # 1. Check for Game Hint Request
        if any(w in msg for w in ["hint", "clue", "help with word", "help me guess", "give me a hint", "stuck"]):
            if game_context and "word" in game_context:
                word = game_context.get("word", "")
                guessed = game_context.get("guessed", [])
                tries = game_context.get("tries", 6)
                status = game_context.get("status", "playing")
                
                if status == "won":
                    return f"🎉 You've already decrypted the sequence **{word.upper()}**! Hit **Play Again** for a new challenge."
                elif status == "lost":
                    return f"💀 The sequence was **{word.upper()}**. Reset the mainframe terminal to try again."
                else:
                    return self.generate_hint(word, guessed, tries)
            else:
                return "💡 The game is currently in standby. Start a round to receive tactical decryption hints!"

        # 2. Check for Developer & Portfolio Inquiries
        if any(w in msg for w in ["developer", "creator", "who made", "who created", "who built", "about you", "author"]):
            skills_str = "\n".join([f"  • {s}" for s in self.portfolio_data["skills"]])
            return (
                f"👨‍💻 **Architect Profile: {self.developer_name}**\n\n"
                f"**Role**: {self.portfolio_data['role']}\n"
                f"**Core Superpowers**:\n{skills_str}\n\n"
                f"**Status**: {self.portfolio_data['hire_status']}\n\n"
                f"Feel free to ask for contact details or custom AI agent services!"
            )

        # 3. Check for Hiring / Contact / Services
        if any(w in msg for w in ["hire", "contact", "email", "job", "freelance", "services", "collaborate", "work with"]):
            services_str = "\n".join([f"  • {s}" for s in self.portfolio_data["services"]])
            return (
                f"🚀 **Commercial & Collaboration Engagements**\n\n"
                f"**{self.developer_name}** provides high-tier agentic systems and AI engineering:\n"
                f"{services_str}\n\n"
                f"📬 **Direct Contact**: `{self.contact_email}`\n"
                f"💼 Available for autonomous agent architecture, AI MVPs, and production systems."
            )

        # 4. Check for Tech Stack / Architecture / How it works
        if any(w in msg for w in ["tech stack", "architecture", "technologies", "how was this made", "code", "specs"]):
            return (
                "🏗️ **System Architecture Overview**:\n\n"
                "• **Frontend & State Engine**: Streamlit 1.45+ with Reactive Component State & Custom Cyberpunk CSS\n"
                "• **Agent Intelligence**: NEXUS-7 Autonomous Agent Engine (NLP Intent Classification + Dual Mode Fallback)\n"
                "• **Game Core**: Finite State Machine (Init -> Playing -> Decrypted/Breached) with real-time heuristic hints\n"
                "• **Styling**: Cyberpunk Glassmorphism with neon cyan (`#00f0ff`) & purple (`#bf00ff`) dynamic palettes\n\n"
                "Check out [SPECS.md](file:///d:/1-New%20folder/5_Hangman%20Python%20Project/SPECS.md) in the project root for full architectural diagrams!"
            )

        # 5. Check for Game Rules / Commands
        if any(w in msg for w in ["rule", "how to play", "instructions", "commands"]):
            return (
                "🎮 **Cyber Hangman Decryption Directives**:\n\n"
                "1. **Mission**: Decrypt the encrypted tech/AI sequence letter by letter before containment failure.\n"
                "2. **Controls**: Click the virtual cyber keyboard or enter single character inputs.\n"
                "3. **Tolerances**: Each incorrect guess destabilizes the cyber core by 1 level.\n"
                "4. **AI Assistance**: Ask me for `/hint` at any stage if containment is reaching critical limits!"
            )

        # 6. Check for Greetings
        if any(w in msg for w in ["hi", "hello", "hey", "salam", "hola", "sup"]):
            return (
                f"👋 **Online and monitoring 24/7!** Welcome back. How can I assist your terminal session today? "
                f"Try asking for a **game hint**, **tech stack**, or **developer portfolio**."
            )

        # 7. Fallback Agent Response (Conversational & Intelligent)
        return (
            f"🤖 **NEXUS-7 Heuristic Response**:\n\n"
            f"I processed your query: *\"{user_message}\"*\n\n"
            f"As an autonomous portfolio & gameplay agent, I can immediately provide:\n"
            f"• **Game Hints**: Type `'hint'` or ask for letter guidance.\n"
            f"• **Developer Info**: Ask about **{self.developer_name}**'s skills, background, or projects.\n"
            f"• **Hire/Contact**: Ask about hiring, freelancing, or contact email.\n"
            f"• **Technical Specs**: Ask about how this project is built and engineered."
        )
