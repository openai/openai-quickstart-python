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
            max_tokens=256
        )
        return redirect(url_for("index", result=response.choices[0].text))

    result = request.args.get("result")
    return render_template("index.html", result=result)

def generate_prompt(animal):
    return """What is a lesson plan idea for a topic

Topic: Fractions
Lesson Plan: "Introduction to Fractions": In this lesson, students will learn about the basics of fractions, including what fractions are, how to write them, and how to compare them. The lesson could include activities such as identifying fractions on a number line,
Topic: Circles
Lesson Plan: "Exploring Circles": In this lesson, students will learn about the properties of circles and how to calculate various measures for circles, such as circumference and area. The lesson could include activities such as constructing circles using a variety of methods, measuring and comparing the circumference and diameter of different circles, and using formulas to calculate the area of circles. Other activities could include solving word problems involving circles and creating their own problems for their classmates to solve.
Topic: {}
Fraction:""".format(
        animal.capitalize()
    )
