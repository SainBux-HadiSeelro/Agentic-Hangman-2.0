"""
NEXUS AI: Friendly 24/7 AI Helper & Portfolio Assistant
Designed for Hangman Game. Simple, warm, and easy for everyone to understand.
"""

from typing import Dict, List, Optional

class NexusAgent:
    """
    Friendly AI Assistant that:
    1. Helps players with simple, easy-to-understand game hints.
    2. Answers questions about the developer (Sain Bux - Hadi Seelro).
    3. Explains how to play the game in plain English and Roman Urdu.
    """

    def __init__(self, developer_name: str = "Sain Bux (Hadi Seelro)", contact_email: str = "contact.sainbux@gmail.com"):
        self.developer_name = developer_name
        self.contact_email = contact_email
        self.agent_name = "NEXUS AI"

        # Simple and helpful clues for words
        self.simple_hints = {
            # Tech & AI
            "PYTHON": "A very popular and friendly programming language named after a snake!",
            "ROBOT": "A machine that can do tasks automatically or be controlled by AI.",
            "COMPUTER": "An electronic device we use every day for work, games, and internet.",
            "INTERNET": "The global network that connects everyone around the world.",
            "CHATBOT": "A computer program (like me!) designed to chat with people.",
            "LAPTOP": "A portable personal computer you can carry in a bag.",
            "CODING": "Writing instructions that tell computers what to do.",
            "SMARTPHONE": "The touchscreen phone in your pocket used for calls and apps.",
            
            # Animals
            "ELEPHANT": "The largest land animal on Earth with big ears and a long trunk!",
            "DOLPHIN": "A super smart and playful sea animal that loves jumping in the ocean.",
            "TIGER": "A big, powerful wild cat with beautiful orange and black stripes.",
            "GIRAFFE": "The tallest living animal in the world with a very long neck.",
            "PENGUIN": "A cute black-and-white bird that cannot fly but swims amazingly in cold ice.",
            "KANGAROO": "An Australian animal that carries its baby in a pouch and hops around.",
            "LION": "Known as the King of the Jungle with a majestic mane.",
            "MONKEY": "A playful animal that loves climbing trees and eating bananas.",

            # Countries
            "PAKISTAN": "A beautiful country in South Asia with majestic mountains like K2.",
            "TURKEY": "A historic country connecting Asia and Europe, famous for Istanbul.",
            "JAPAN": "The land of the rising sun, famous for Tokyo, cherry blossoms, and anime.",
            "CANADA": "A large country in North America famous for maple syrup and cold winters.",
            "BRAZIL": "The largest country in South America, famous for football and Amazon rainforest.",
            "GERMANY": "A European country known for engineering, fast cars, and castles.",
            "EGYPT": "An ancient land in Africa famous for the Great Pyramids and the Nile river.",
            "FRANCE": "A romantic European country famous for the Eiffel Tower and delicious pastries.",

            # Movies & Fun
            "AVATAR": "A famous sci-fi movie set on the blue alien planet of Pandora.",
            "TITANIC": "A legendary romance movie about the famous ship that hit an iceberg.",
            "INCEPTION": "A mind-bending movie about dreams within dreams starring Leonardo DiCaprio.",
            "GLADIATOR": "An epic action movie about a Roman general who fights in the Colosseum.",
            "FROZEN": "A Disney animated movie with Queen Elsa and the song 'Let It Go'!",
            "BATMAN": "The superhero vigilante who protects Gotham City at night.",
            "SPIDERMAN": "A friendly neighborhood superhero who climbs walls and shoots webs."
        }

    def get_greeting(self) -> str:
        """Friendly welcome message for any visitor."""
        return (
            f"👋 **Hi there! I am {self.agent_name}**, your friendly game buddy!\n\n"
            f"I was created by **{self.developer_name}** to help you:\n"
            f"• 💡 **Get easy hints** if you are stuck\n"
            f"• 🎮 **Learn how to play** the game\n"
            f"• 👨‍💻 **Learn about the developer** & how to hire him\n\n"
            f"Feel free to ask me anything or click one of the buttons above!"
        )

    def generate_hint(self, secret_word: str, guessed_letters: List[str], tries_left: int) -> str:
        """Returns a simple, easy-to-understand clue."""
        word_upper = secret_word.upper()
        
        # 1. Check if we have an easy clue
        clue = self.simple_hints.get(word_upper)
        vowels = [ch for ch in "AEIOU" if ch in word_upper and ch not in guessed_letters]
        
        parts = []
        if clue:
            parts.append(f"💡 **Clue**: *{clue}*")
        else:
            parts.append(f"💡 **Word Length**: This word has **{len(secret_word)} letters**.")

        if tries_left <= 2 and vowels:
            parts.append(f"✨ **Bonus Tip**: Try guessing a vowel like **'{vowels[0]}'**!")
        elif tries_left <= 3:
            unguessed = [ch for ch in word_upper if ch not in guessed_letters]
            if unguessed:
                parts.append("✨ **Tip**: Look at the letters you haven't tried yet!")

        return "\n\n".join(parts)

    def process_message(self, user_message: str, game_context: Optional[Dict] = None) -> str:
        """Friendly, easy-to-understand response engine."""
        msg = user_message.strip().lower()

        # 1. Hint requests
        if any(w in msg for w in ["hint", "clue", "help", "stuck", "btao", "madad"]):
            if game_context and "word" in game_context:
                word = game_context.get("word", "")
                guessed = game_context.get("guessed", [])
                tries = game_context.get("tries", 6)
                status = game_context.get("status", "playing")

                if status == "won":
                    return f"🎉 You already guessed it! The word was **{word.upper()}**! Click 'Play Again' for a new round."
                elif status == "lost":
                    return f"The word was **{word.upper()}**. Don't worry, click 'Play Again' and try another one!"
                else:
                    return self.generate_hint(word, guessed, tries)
            return "💡 Start a game and I will be happy to give you a hint!"

        # 2. Who is the developer?
        if any(w in msg for w in ["developer", "creator", "who made", "who built", "author", "kisne banaya"]):
            return (
                f"👨‍💻 **Meet the Developer: {self.developer_name}**\n\n"
                f"He is a talented **Full-Stack Python & AI Developer** who builds smart AI applications, "
                f"chatbots, and modern web apps.\n\n"
                f"• **GitHub**: [github.com/SainBux-HadiSeelro](https://github.com/SainBux-HadiSeelro)\n"
                f"• **Email**: `{self.contact_email}`\n\n"
                f"He is available for projects and full-time work!"
            )

        # 3. How to hire / Contact
        if any(w in msg for w in ["hire", "contact", "email", "job", "freelance", "work", "rabta"]):
            return (
                f"🤝 **Want to work with {self.developer_name}?**\n\n"
                f"You can reach out directly via email:\n"
                f"📧 **`{self.contact_email}`**\n\n"
                f"He creates custom AI chatbots, web applications, and automation systems for clients!"
            )

        # 4. How to play
        if any(w in msg for w in ["rule", "how to play", "kese khelein", "instructions", "game"]):
            return (
                "🎮 **How to Play Hangman (Super Easy!)**:\n\n"
                "1. A secret word is hidden behind blank lines (`_ _ _`).\n"
                "2. Click any letter on the on-screen keyboard to guess.\n"
                "3. If the letter is right, it shows up in **green**! ✅\n"
                "4. If it's wrong, you lose 1 heart ❤️ and a part of the hangman appears.\n"
                "5. Guess the whole word before you run out of 6 hearts to win!"
            )

        # 5. Greetings
        if any(w in msg for w in ["hi", "hello", "hey", "salam", "assalam", "kese ho"]):
            return (
                f"😊 **Hello! / Salam!** Glad to see you here!\n\n"
                f"I am ready to help you play Hangman or answer any questions about this project. "
                f"Just click **'Get a Hint'** if you need a clue!"
            )

        # 6. Fallback
        return (
            f"🤖 I'm here to help! You can ask me:\n"
            f"• *'Give me a hint'* for a clue about the word.\n"
            f"• *'How to play'* for simple game rules.\n"
            f"• *'Who is the developer?'* to learn about {self.developer_name}."
        )
