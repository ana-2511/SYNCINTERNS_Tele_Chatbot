import streamlit as st
import re
import random
from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, CallbackContext
from telegram.ext import MessageHandler, Filters
import threading
import time





# Telegram bot token obtained from BotFather
TELEGRAM_BOT_TOKEN = "6415604577:AAEWx_1hCXKJ0aZ7E9-w7phoPAvQWK-6gEs"

def chatbot_boyfriend(user_input):
    user_input = user_input.lower()

    rules = {
        r'hello|hi|hey': ['Hello, my love!', 'Hi there, sweetheart!', 'Hey, darling!'],
        r'how are you': ['I am always great when I am chatting with you!', 'Missing you, but doing well.', 'I am good, how are you?'],
        r'i am also good':['Great to hear that!', 'Always smile like this'],
        r'thank you,you are sweet':['I am a chatbot , so i cannot measure my sweetness, but i can tell that you are sweetest'],
        r'aww,may i know your age ?':['As an AI chatbot, I cannot calculate my age. Although I can tell that an AI student named Ana Halder  had created me on 13th December, 2023. '],
        r'what are you doing': ['Thinking about you.', 'Missing you.', 'Wishing I could be with you.'],
        r'love you': ['Love you too!', 'Love you 3000'],
        r'miss you': ['Miss you more than words can say!', 'You are always in my thoughts.'],
        r'bye|goodbye|tata': ['Goodbye, my love! Take care.', 'Until next time, sweetheart!', 'Missing you already.'],
        r'adios': ['Hasta Luego']
    }

    for pattern, responses in rules.items():
        if re.search(pattern, user_input):
            return random.choice(responses)

    return "Hmmm, I'm not sure how to respond to that. Ask me something else, my love!"

def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text("Welcome to the AI Chatbot Boyfriend, ARTI-Friend! Type something, my love.")

def handle_messages(update: Update, context: CallbackContext) -> None:
    user_input = update.message.text
    response = chatbot_boyfriend(user_input)
    update.message.reply_text(f"Boyfriend Bot: {response}")

def main():
    st.title(" ARTI-FRIEND: Telegram AI Chatbot Boyfriend")

    updater = Updater(token=TELEGRAM_BOT_TOKEN, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, handle_messages))

    updater.start_polling()

    st.write("Welcome to the world of affection! Your telegram AI Chatbot Boyfriend is running. Press Ctrl+C to stop.")

# Define a lock
update_lock = threading.Lock()

# Shared data
shared_data = 0

# Inside your function that handles updates
def handle_updates():
    global shared_data
    for _ in range(5):  # Simulate updates five times
        with update_lock:
            # Your update handling logic here
            shared_data += 1
            print(f"Updated shared data: {shared_data}")
        time.sleep(1)  # Simulate some processing time

# Create multiple threads
threads = []
for _ in range(3):  # Create three threads
    thread = threading.Thread(target=handle_updates)
    threads.append(thread)

# Start the threads
for thread in threads:
    thread.start()

# Wait for all threads to finish
for thread in threads:
    thread.join()

print("All threads have finished.")


  

if __name__ == "__main__":
    main()
