import os
import openai
from flask import Flask, redirect, render_template, request, url_for, redirect, url_for

app = Flask(__name__)
openai.api_key = os.getenv("OPENAI_API_KEY")

@app.route("/", methods=("GET", "POST"))
def index():
    if request.method == "POST":
        priority = request.form["priority"]
        num_shots = request.form['action']
        response = openai.Completion.create(
            model="text-davinci-003",
            prompt=generate_prompt(priority=priority,num_shots=num_shots),
            temperature=0.6,
              max_tokens=256,
        )
        return redirect(url_for("index", result=response.choices[0].text))

    result = request.args.get("result")
    return render_template("index_bank.html", result=result)

def generate_prompt(priority,num_shots):
    example_shots_map = {
        'zero':'',
        'one':"""Priority: A national bank with good options for small business accounts.
Suggestion: Chase and Wells Fargo are both recommended.""",
        'few':"""Priority: A national bank with good options for small business accounts.
Suggestion: Chase and Wells Fargo are both recommended.
Priority: A high-interest checking account.
Suggestion: Fortune recommends the Wells Fargo Initiate Business Checking account.
Priority: Lower fees for things like wire transfers or foreign ATM transactions than traditional banks.
Suggestion: Forbes Advisor suggest online checking accounts.""",
    }
    examples = example_shots_map[num_shots]
    return f"""Recommend to my client the best bank, based on their priorities.
{examples}
Priority: {priority.capitalize()}.
Suggestion:"""