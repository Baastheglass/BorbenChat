from flask import Flask, render_template, request
from chatbot import chatBot

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def chat():
    bot = chatBot(api_key="YOUR_API_KEY")  # Replace with your actual API key
    conversation_history = []  # Store chat history

    if request.method == "POST":
        user_prompt = request.form["prompt"]
        response = bot.send_Prompt(prompt=user_prompt)
        conversation_history.append({"user": user_prompt, "bot": response.text})

    return render_template("chat.html", conversation=conversation_history)
