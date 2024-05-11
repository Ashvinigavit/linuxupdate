# import re

# # Define refined patterns and corresponding responses
# refined_patterns = [
#     (r'.*buy.*book.*', "Sure! Let me assist you with purchasing a book. Do you have a specific title in mind?"),
#     (r'.*track.*order.*', "Of course! To track your order, please provide your order number."),
#     (r'.*cancel.*order.*', "I can help you cancel your order. Could you please provide the order number?"),
#     (r'.*return.*book.*', "To initiate a return, we'll need the order number and reason for return. Could you provide those details?"),
#     (r'.*delivery.*time.*', "Our standard delivery time is 3-5 business days. Would you like to track your order?"),
#     (r'.*book.*availability.*', "Sure! Let me check the availability of that book for you. What's the title of the book?"),
#     (r'.*help.*', "How can I assist you today?"),
#     (r'.*thank you.*', "You're welcome! If you need further assistance, feel free to ask."),
#     (r'.*', "I'm sorry, I didn't understand. Can you please rephrase?")
# ]

# # Compile refined patterns
# refined_pattern_responses = [(re.compile(pattern, re.IGNORECASE), response) for pattern, response in refined_patterns]

# def recognize_refined_pattern(sentence):
#     for pattern, response in refined_pattern_responses:
#         if pattern.match(sentence):
#             return response
#     return None

# # Main loop to interact with the user
# def chat():
#     print("Welcome! How can I assist you today?")
#     while True:
#         user_input = input("You: ")
#         if user_input.lower() == 'quit':
#             print("Goodbye!")
#             break
#         response = recognize_refined_pattern(user_input)
#         if response:
#             print("Bot:", response)
#         else:
#             print("Bot: I'm sorry, I didn't understand. Can you please rephrase?")

# # Run the chatbot
# if __name__ == "__main__":
#     chat()



import nltk
from nltk.tokenize import word_tokenize
from nltk import pos_tag
from nltk.corpus import wordnet

# Download NLTK resources
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
nltk.download('wordnet')

# Define patterns and corresponding responses
patterns = [
    (r'.*buy.*book.*', "Sure! Let me assist you with purchasing a book."),
    (r'.*track.*order.*', "Please provide your order number so that I can track it for you."),
    (r'.*cancel.*order.*', "I can help you cancel your order. Please provide the order details."),
    (r'.*return.*book.*', "To initiate a return, please provide the order number."),
    (r'.*help.*', "How can I assist you today?"),
    (r'.*thank you.*', "You're welcome! If you need further assistance, feel free to ask."),
    (r'.*', "I'm sorry, I didn't understand. Can you please rephrase?")
]

# Compile patterns
pattern_responses = [(re.compile(pattern, re.IGNORECASE), response) for pattern, response in patterns]

def recognize_pattern(sentence):
    for pattern, response in pattern_responses:
        if pattern.match(sentence):
            return response
    return None

# Main loop to interact with the user
def chat():
    print("Welcome! How can I assist you today?")
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'quit':
            print("Goodbye!")
            break
        response = recognize_pattern(user_input)
        if response:
            print("Bot:", response)
        else:
            print("Bot: I'm sorry, I didn't understand. Can you please rephrase?")

# Run the chatbot
if __name__ == "__main__":
    chat()
