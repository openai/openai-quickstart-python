import os
import openai
from flask import Flask, redirect, render_template, request, url_for

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Set a secret key for session management
openai.api_key = os.getenv("OPENAI_API_KEY")

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        animal = request.form["animal"]
        response = openai.Completion.create(
            model="text-davinci-003",
            prompt=generate_prompt(animal),
            temperature=0.6,
            n=3  # Generate 3 superhero names
        )
        names = [choice.text.strip() for choice in response.choices]
        return redirect(url_for("index", result=names))

    result = request.args.get("result")
    return render_template("index.html", result=result)

def generate_prompt(animal):
    return f"Suggest three names for an animal that is a superhero.\n\nAnimal: {animal.capitalize()}\nNames:"


if __name__ == "__main__":
    app.run(debug=True)
