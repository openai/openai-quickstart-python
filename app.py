import os

import openai
from flask import Flask, redirect, render_template, request, url_for

app = Flask(__name__)
openai.api_key = os.getenv("OPENAI_API_KEY")


@app.route("/", methods=("GET", "POST"))
def index():
    if request.method == "POST":
        ingredient1 = request.form["ingredient1"]
        ingredient2 = request.form["ingredient2"]
        ingredeint3 = request.form["ingredient3"]
        response = openai.Completion.create(
            model="text-davinci-002",
            prompt=generate_prompt(ingredient1, ingredient2, ingredient3),
            temperature=0.6,
        )
        return redirect(url_for("index", result=response.choices[0].text))

    result = request.args.get("result")
    return render_template("index.html", result=result)


def generate_prompt(ingredient1, ingredient2, ingredient3):
    return """Create a recipe for a fancy, Michelin-starred dish using {ingredient1}, {ingredient2}, & {ingredient3}. Please include both a list of ingredients and the procedure"""
    )
