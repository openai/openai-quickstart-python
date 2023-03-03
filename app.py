import os

import openai
import requests
from flask import Flask, render_template, request

app = Flask(__name__)
openai.api_key = os.getenv("OPENAI_API_KEY")


# chatgpt官方api调用
def chatgpt35_api(data):
    """official api"""
    headers = {
        "content-type": "application/json",
        'Authorization': "Bearer " + os.getenv("OPENAI_API_KEY")
    }
    response = requests.post(url="https://api.openai.com/v1/chat/completions", headers=headers, json=data)
    answer = [elem["message"] for elem in response.json()['choices']]
    return answer[0]


request_data = {
    "messages": [],
    "max_tokens": 1024,
    "model": "gpt-3.5-turbo",
    "top_p": 1,
    "temperature": 0.3,
    "n": 3
}


@app.route("/", methods=("GET", "POST"))
def index():
    if request.method == "POST":
        input_text = request.get_json()['msg']
        message = {"role": "user", "content": input_text}
        if len(request_data['messages']) == 4:
            request_data['messages'].pop(0)
        request_data['messages'].append(message)
        answer = chatgpt35_api(request_data)
        request_data['messages'].append(answer)
        return answer['content']

    result = request.args.get("result")
    return render_template("index.html", result=result)
