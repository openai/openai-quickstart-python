import os

import openai
from flask import Flask, render_template, request

app = Flask(__name__)
openai.api_key = os.getenv("OPENAI_API_KEY")


@app.route("/", methods=("GET", "POST"))
def index():
    if request.method == "POST":
        input_text = request.get_json()['msg']
        response = openai.Completion.create(
            model="text-davinci-003",
            prompt=input_text,
            temperature=0.7,
            max_tokens=1024,
            top_p=1.0,
            frequency_penalty=0.0,
            presence_penalty=0.0
        )
        return response.choices[0].text

    result = request.args.get("result")
    return render_template("index.html", result=result)
