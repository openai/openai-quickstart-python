import os

import openai
from flask import Flask, redirect, render_template, request, url_for

app = Flask(__name__)
openai.api_key = "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"
"""os.getenv("OPENAI_API_KEY")"""


@app.route("/", methods=("GET", "POST"))
def index():
    if request.method == "POST":
        cronjob = request.form["cronjob"]
        response = openai.Completion.create(
            model="text-davinci-003",
            prompt=generate_prompt(cronjob),
            temperature=0.6,
            max_tokens=1024
        )
        return redirect(url_for("index", result=response.choices[0].text))

    result = request.args.get("result")
    return render_template("index.html", result=result)


def generate_prompt(cronjob):
    return """Suggest the schedule time in the easiest way
Cronjob: * * * * *
schedule interval: every minute
cronjob: 0 1 * * *
schedule: every day at 01:00
Cronjob: {}
schedule:""".format(
        cronjob.capitalize()
    )
