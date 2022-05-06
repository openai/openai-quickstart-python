from asyncio import constants
import os

import openai
from flask import Flask, redirect, render_template, request, url_for, jsonify
# from flask_cors import CORS, cross_origin

# using SendGrid's Python Library
# https://github.com/sendgrid/sendgrid-python
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
from constants import ASSEMBO_CONTACT, sendgrid_templates

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

@app.route("/send_email", methods=("GET", "POST"))
def send_email():
    template_id = sendgrid_templates["POST_MEETING"]
    try:
        to_email = request.args.get('toEmail')
        notes = request.args.get('notes')
        sg = SendGridAPIClient(os.getenv("SENDGRID_API_KEY", default = None))
        data = {
            "personalizations": [{
                "to": [{
                    "email": to_email
                }],
                'dynamic_template_data': { "notes": notes }
            }],
            "from": {
                "email": ASSEMBO_CONTACT
            },
            "template_id": template_id
        }
        # response = sg.send(message)
        response = sg.client.mail.send.post(request_body=data)
        return "200"
    except Exception as e:
        print(e)
        return "sad"

def generate_prompt(animal):
    return animal