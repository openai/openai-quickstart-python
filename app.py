import os

import openai
from flask import Flask, redirect, render_template, request, url_for

app = Flask(__name__)
openai.api_key = os.getenv("OPENAI_API_KEY")

@app.route("/", methods=("GET", "POST"))
def index():
    if request.method == "POST":
        team = request.form["team"]
        response = openai.Completion.create(
            model="text-davinci-003",
            prompt=generate_prompt(team),
            temperature=1.25,
        )
        return redirect(url_for("index", result=response.choices[0].text))

    result = request.args.get("result")
    return render_template("index.html", result=result)


def generate_prompt(team):
    return """Suggest three names for an NFL fantasy football team given an input of players on the roster. Scan the internet and use other fantasy team names as inspiration. Use the inputted player names to come up with the name if applicable.

Team: A team that has CeeDee Lamb and Justin Fields
Names: CeeDeez Nuts, Head Receiver, Fields of Dreams
Team: A team that has Griffin Adduci
Names: G-Unit, Griff Missiles, The real slim shady
Team: I just want a generic fantasy football team name
Names: Game of Throws, G-Unit, Go Luck Yourself
Team: {}
Names:""".format(
        team.capitalize()
    )


