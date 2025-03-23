📜 README.md 

Rule-Based Chatbot Web App

This is a simple rule-based chatbot built using Python (Flask), HTML, CSS, and JavaScript. The chatbot responds to predefined queries based on fuzzy matching.  


Features

✅ Predefined responses using a dictionary  
✅ Smart response matching using `fuzzywuzzy` for flexible inputs  
✅ Interactive web-based UI with chat bubbles 
✅ AJAX-based real-time messaging  
✅ Customizable chatbot responses  
✅ Easy to deploy on Heroku/Render 

🛠 Tech Stack

| Component | Technology Used |
|--------------|--------------------|
| Backend | Flask (Python) |
| Frontend | HTML, CSS, JavaScript |
| Chatbot Logic| Rule-Based (`fuzzywuzzy`) |
| Web Server | Flask |
| Communication | AJAX (Fetch API) |



📂 Project Structure

chatbot_webapp/ │── app.py # Flask Backend (Chatbot Logic) │── requirements.txt # Dependencies for installation │── Procfile # For deployment (Heroku) │── templates/ │ └── index.html # Frontend (Chat Interface) │── static/ │ ├── style.css# CSS for Styling │ └── script.js # JavaScript for Chat Functionality └── README.md # Documentation

# Installation & Setup

1️ Clone the Repository
```bash
git clone https://github.com/harsh0904-dot/chatbot_webapp.git
cd chatbot_webapp

2️ Create a Virtual Environment (Optional)

python -m venv venv
source venv/bin/activate   # On macOS/Linux
venv\Scripts\activate      # On Windows

3️ Install Dependencies

pip install -r requirements.txt

4️ Run the Flask Server

python app.py
✅ The server will start on http://127.0.0.1:5000/.
✅ Open the link in your browser to start chatting with the bot.


Usage
1️ Open http://127.0.0.1:5000/ in a browser.
2️ Type a message in the input box and click "Send".
3️ The chatbot will respond based on predefined answers.
4️ If the input doesn’t match exactly, the chatbot will use fuzzy matching to find the best possible response.

Deployment (Make Your Chatbot Public)
Deploy on Render
1.  Go to Render.com.
2.  Click New Web Service → Connect your GitHub repository.
3.  Set Start Command as: 
4.  python app.py
5.  Click Deploy. 

Deploy on Heroku
1.  Install Heroku CLI.
2.  Login to Heroku: 
3.  heroku login
4.  Create a Heroku app: 
5.  heroku create chatbot-webapp
6.  Add build files: 
7.  echo "web: python app.py" > Procfile
8.  Deploy: 
9.  git add .
10. git commit -m "Deploy chatbot"
11. git push heroku main
12. Open the app: 
13. heroku open
✅ Your chatbot is now live online! 

Customizing the Chatbot
Want to add more responses? Modify app.py and update the responses dictionary:
responses = {
    "hello": "Hello! How can I assist you today?",
    "hi": "Hi there! How can I help?",
    "how are you": "I'm doing great! What about you?",
    "bye": "Goodbye! Have a great day!",
    "thank you": "You're welcome! 😊",
    "what is AI": "Artificial Intelligence enables machines to mimic human intelligence.",
    "tell me a joke": "Why don’t scientists trust atoms? Because they make up everything! 😂"
}

Restart the Flask server after making changes:
python app.py
Contributing
1.  Fork this repository.
2.  Clone your forked repo: 
3.  git clone https://github.com/harsh0904-dot/chatbot_webapp.git
4.  Create a new branch for modifications: 
5.  git checkout -b feature-name
6.  Commit your changes: 
7.  git add .
8.  git commit -m "Added new chatbot responses"
9.  Push and open a pull request: 
10. git push origin feature-name

📄 License
This project is open-source and available under the MIT License.

📧 Contact
📩 Have questions? Reach out to me:
•   📧 Email: singhharshvardhan178@gmail.com



