import os

import openai
from flask import Flask, redirect, render_template, request, url_for

app = Flask(__name__)
openai.api_key = os.getenv("OPENAI_API_KEY")


@app.route("/", methods=("GET", "POST"))
def index():
    if request.method == "POST":
        animal = request.form["animal"]
        response = openai.Completion.create(
            model="text-davinci-003",
            prompt=generate_prompt(animal),
            temperature=0.6,
        )
        return redirect(url_for("index", result=response.choices[0].text))

    result = request.args.get("result")
    return render_template("index.html", result=result)

# run on model gpt-3.5-turbo 
@app.route("/turbo", methods=("GET", "POST"))
def turbo():
    if request.method == "POST":
        animal = request.form["animal"]
        response = openai.ChatCompletion.create( #Needs OpenAI 0.27 above )
            model="gpt-3.5-turbo",
            messages=[
                        {"role": "system", "content": "You are a expert in zoology"},
                        {"role": "assistant", "content": "Suggest three names for an animal that is a superhero."},
                        {"role": "user", "content": "Cat"},
                        {"role": "assistant", "content": "Captain Sharpclaw, Agent Fluffball, The Incredible Feline"},
                        {"role": "user", "content": "Dog"},
                        {"role": "assistant", "content": "Ruff the Protector, Wonder Canine, Sir Barks-a-Lot"},
                        {"role": "user", "content": animal},
                    ]
        )
        return redirect(url_for("turbo", result=response['choices'][0]['message']['content']))

    result = request.args.get("result")
    return render_template("index-turbo.html", result=result)


def generate_prompt(animal):
    return """Suggest three names for an animal that is a superhero.

Animal: Cat
Names: Captain Sharpclaw, Agent Fluffball, The Incredible Feline
Animal: Dog
Names: Ruff the Protector, Wonder Canine, Sir Barks-a-Lot
Animal: {}
Names:""".format(
        animal.capitalize()
    )
