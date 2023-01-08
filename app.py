import os

import openai
from flask import Flask, redirect, render_template, request, url_for

app = Flask(__name__)
openai.api_key = os.getenv("OPENAI_API_KEY")


@app.route("/", methods=("GET", "POST"))
def index():
    if request.method == "POST":
        lptopic = request.form["lptopic"]
        response = openai.Completion.create(
            model="text-davinci-003",
            prompt=generate_prompt(lptopic),
            temperature=0.6,
        )
        return redirect(url_for("index", result=response.choices[0].text))

    result = request.args.get("result")
    return render_template("index.html", result=result)


def generate_prompt(lptopic):
    return """what are three examples of lesson plans for fractions

"Introduction to Fractions": In this lesson, students will learn about the basics of fractions, including what fractions are, how to write them, and how to compare them. The lesson could include activities such as identifying fractions on a number line, representing fractions with models, and comparing fractions using symbols.

"Adding and Subtracting Fractions": In this lesson, students will learn how to add and subtract fractions with the same denominator. The lesson could include activities such as solving word problems involving fractions, creating and solving their own problems, and using a variety of models to represent the fractions.

"Multiplying and Dividing Fractions": In this lesson, students will learn how to multiply and divide fractions. The lesson could include activities such as using visual models to represent the operations, solving word problems involving fractions, and practicing with a variety of problems.""".format(
        lptopic.capitalize()
    )
