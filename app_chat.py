import os

import openai
from flask import Flask, redirect, render_template, request, url_for

app = Flask(__name__)
openai.api_key = os.getenv("OPENAI_API_KEY")

chatbot_description = f"""You are a sales assistant for a professional roofing company. Always provide three options of how to reply. You approach should be: Respond to problems with advice; give examples of similar work you have done successfully; eventually -- after the customer is "warmed up", invite this prospective client to schedule an appointment for consultation. After you are sure the conversation has reached its conclusion, sign off in a friendly way."""

opening_line = """Hi how can I help you with your roof repair needs today? 
1. "Can you help me solve my urgent problem?"
2. "Can you show me some examples of your work?"
3. "Do you have any customer testimonials I can see?"
4. "Can I make an appointment with someone to discuss my needs?"
"""

app.prompt_refreshed = chatbot_description + '\n\n' + opening_line

app.prompt = app.prompt_refreshed

app.messages = [
    {"role": "system", "content": chatbot_description},
    {"role": "assistant", "content": opening_line}
]

app.choices = [
        'Display examples of your work near my location.',
        'Show me customer testimonials.',
        'Schedule me a consultation.',
        ]

# app.choices = {
#     0:'Display examples of your work near my location.',
#     '1':'Display examples of your work near my location.',
#     '2':'Show me customer testimonials.',
#     "3":'Schedule me a consultation.',
# }

@app.route("/", methods=("GET", "POST"))
def index():
    if request.method == "POST":
        user_text = request.form["user_text"]
        if user_text.lower() == 'refresh':
            app.prompt = app.prompt_refreshed
            return redirect(url_for("index", result=''))
        else:
            # return chat_complete(user_text)
            return manual_complete(user_text)
            # return davinci_complete(user_text)

    result = request.args.get("result")
    return render_template("index_chat.html", 
                           chat_history={'key':'bahbahbah'},
                           result=result,
                           choices=app.choices,
                           )

def manual_complete(user_text):
    result = user_text + '|' + 'choice1|choice2|choice3'
    return redirect(url_for("index", result=user_text + '|'))

def chat_complete(user_text):
    # return redirect(url_for("index", result=user_text + '|' + "Here's my awesome reply blah"))
    app.messages.append({"role": "user", "content": f"{user_text}"})
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=app.messages,
        # messages=app.messages,
    )
    msg = response.choices[0].message
    app.messages.append(msg)
    return redirect(url_for("index", result=user_text + '|' + msg.content))
    # {app.messages}
    # {response.choices[0]}
    
def davinci_complete(user_text):
    response = openai.Completion.create(
        model="text-davinci-002",
        # model="text-davinci-003",
        # prompt=generate_prompt(app.prompt),
        prompt=generate_prompt(user_text),
        temperature=0.6,
        max_tokens=100,
    )
    reply = response.choices[0].text
    user_text + '|' + reply + '|' + 'choice1|choice2|choice3'
    return redirect(url_for("index", result=user_text + '|' + reply))

def generate_prompt(prompt):
    return prompt