import os
from openai import OpenAI
from flask import Flask, redirect, render_template, request, url_for

client = OpenAI()

app = Flask(__name__)

chat_history = [
    {"role": "system", "content": "You are a helpful assistant."},
]


@app.route("/", methods=("GET", "POST"))
def index():
    if request.method == "POST":
        user_message = request.form["message"]
        chat_history.append({"role": "user", "content": user_message})

        completion = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=chat_history,
        )
        chat_history.append(
            {"role": "assistant", "content": completion.choices[0].message.content}
        )
        return redirect(url_for("index"))

    return render_template("index.html", chat_history=chat_history)
