import os
import openai
from flask import Flask, redirect, render_template, request, url_for

app = Flask(__name__)
openai.api_key = os.getenv("OPENAI_API_KEY")


@app.route("/", methods=("GET", "POST"))
def index():
    if request.method == "POST":
        animal = request.form["animal"]
        text_response = openai.Completion.create(
            model="text-davinci-003",
            prompt=generate_text_prompt(animal),
            temperature=0.6,
        )
        image_response = openai.Image.create(
            prompt=text_response.choices[0].text,
            size="256x256",
            n=1
        )
        image_url = image_response.data[0].url

        return redirect(url_for("index", text_result=text_response.choices[0].text, image_result=image_url))

    text_result = request.args.get("text_result")
    image_result = request.args.get("image_result")
    return render_template("index.html", text_result=text_result, image_result=image_result)


def generate_text_prompt(animal):
    return """Suggest three names for an animal that is a superhero.

Animal: Cat
Names: Captain Sharpclaw, Agent Fluffball, The Incredible Feline
Animal: Dog
Names: Ruff the Protector, Wonder Canine, Sir Barks-a-Lot
Animal: {}
Names:""".format(
        animal.capitalize()
    )

# def generate_image_prompt(text_result):
#     return (image_result)

def generate_image_prompt(text_result):
    image_response = openai.Image.create(
        prompt=text_result,
        size="256x256",
        n=1
    )
    return image_response.data[0].url
