import nltk
from nltk.chat.util import Chat, reflections

nltk.download('punkt')

# Define patterns and responses for the chatbot
pairs = [

      
    ("hi|hello|hey", ["Hello!", "Hi there!", "Hey!"]),
    ("how are you?", ["I'm good, What about you?", "superb, you?", "I'm doing well, how are you?."]),
    ("your name?", ["I am a chatbot.", "You can call me Chatbot."]),
    ("i am good", ["good to hear"]),
    ("what is your purpose?", ["I'm here to assist you and have conversations."]),
    ("bye|goodbye", ["Goodbye!", "See you later.", "Bye!"]),
    ("what can you do?", ["I can answer your questions, provide information, or just have a chat with you."]),
    ("tell me a joke", ["Why don't scientists trust atoms? Because they make up everything!"]),
    ("how old are you?", ["I'm just a program, so I don't have an age!"]),
    ("where are you from?", ["I exist in the digital realm, but you can think of me as being from the internet!"]),
    ("do you have any hobbies?", ["I don't have hobbies in the way humans do, but I enjoy processing information and helping users like you!"]),
    ("can you help me with something?", ["Of course! Just let me know what you need assistance with."])
   ]



# Create a Chat object
chatbot = Chat(pairs, reflections)

# Start chatting
print("Hello! I'm a simple chatbot.")
while True:
    user_input = input("You: ")
    if user_input.lower() == 'bye':
        print("Chatbot: Goodbye!")
        break
    response = chatbot.respond(user_input)
    print("Chatbot:", response)