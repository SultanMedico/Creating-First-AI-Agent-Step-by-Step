from flask import Flask, render_template, request, jsonify
import random

app = Flask(__name__)

class SimpleAgent:
    def __init__(self):
        self.responses = {
            "greeting": ["Hello!", "Hi there!", "Greetings!"],
            "farewell": ["Goodbye!", "See you later!", "Bye!"],
            "default": ["I'm not sure I understand.", "Could you rephrase that?", "Interesting!"]
        }
    
    def respond(self, message):
        message = message.lower()
        if any(word in message for word in ["hi", "hello", "hey"]):
            return random.choice(self.responses["greeting"])
        elif any(word in message for word in ["bye", "goodbye"]):
            return random.choice(self.responses["farewell"])
        else:
            return random.choice(self.responses["default"])

agent = SimpleAgent()

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get_response", methods=["POST"])
def get_response():
    user_message = request.form["message"]
    return jsonify({"response": agent.respond(user_message)})

if __name__ == "__main__":
    app.run(debug=True)