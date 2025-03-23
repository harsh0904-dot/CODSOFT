from flask import Flask, request, jsonify, render_template
from fuzzywuzzy import process  # Import fuzzy matching

app = Flask(__name__)

# Predefined chatbot responses
responses = {
    "hello": "Hello! How can I assist you today?",
    "hi": "Hi there! How can I help?",
    "how are you": "I'm a bot, but I'm doing great! What about you?",
    "bye": "Goodbye! Have a great day!",
    "thank you": "You're welcome! 😊",
    "who created you": "I was created using Python and Flask.",
    "what is AI": "Artificial Intelligence (AI) enables machines to mimic human intelligence.",
    "what is machine learning": "Machine Learning is a subset of AI that allows computers to learn from data.",
    "tell me a joke": "Why don’t scientists trust atoms? Because they make up everything! 😂",
    "who is Elon Musk": "Elon Musk is the CEO of Tesla and SpaceX."
}

# Function to get chatbot response using fuzzy matching
def chatbot_response(user_input):
    user_input = user_input.lower()
    
    # Find the best match from the responses dictionary
    best_match, score = process.extractOne(user_input, responses.keys())

    # If match score is above 60%, return the matched response
    if score > 60:
        return responses[best_match]
    else:
        return "Sorry, I don't understand that. Can you rephrase?"

# Serve the homepage (index.html)
@app.route("/")
def home():
    return render_template("index.html")  # Loads the chat interface

# Chatbot API endpoint
@app.route("/chat", methods=["POST"])
def chat():
    user_message = request.json.get("message")
    bot_reply = chatbot_response(user_message)
    return jsonify({"reply": bot_reply})

if __name__ == "__main__":
    app.run(debug=True)
