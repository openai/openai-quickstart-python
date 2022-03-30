import os

import openai
from flask import Flask, redirect, render_template, request, url_for, jsonify
# from flask_cors import CORS, cross_origin

app = Flask(__name__)
openai.api_key = os.getenv("OPENAI_API_KEY")
# cors = CORS(app)
# app.config['CORS_HEADERS'] = 'Content-Type'

@app.route('/')
def hello():
    return "asdjfklasdj"

@app.after_request # blueprint can also be app~~
def after_request(response):
    header = response.headers
    header['Access-Control-Allow-Origin'] = '*'
    # Other headers can be added here if required
    return response

@app.route("/todo", methods=("GET", "POST"))
def todo():
    # if request.method == "POST" :
    # animal = request.get_json(force=True)
    animal = request.args.get('text')
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=generate_prompt(animal + '\ngenerate action items:'),
        temperature=0.6,
        max_tokens=500,
    )
    return response.choices[0].text

        # return redirect(url_for("index", result=response.choices[0].text))

    # result = request.args.get("result")
    # print(result)
    # return render_template("index.html", result=result)
    # return result


def generate_prompt(animal):
    return animal