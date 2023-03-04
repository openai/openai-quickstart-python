import json
import os
import secrets
from datetime import datetime

import requests
from flask import Flask, render_template, request, make_response
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///chatbot.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(app)

SESSION_EXPIRATION_TIME = 10 * 60


class Session(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    session_id = db.Column(db.String(50), unique=True, nullable=False)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    def __repr__(self):
        return '<User %r>' % self.username


class ChatLog(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    session_id = db.Column(db.String(32), nullable=False)
    create_dt = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    messages = db.Column(db.Text, nullable=False)


# chatgpt官方api调用
def chatgpt35_api(data):
    """official api"""
    headers = {
        "content-type": "application/json",
        'Authorization': "Bearer " + os.getenv("OPENAI_API_KEY")
    }
    try:
        response = requests.post(url="https://api.openai.com/v1/chat/completions", headers=headers, json=data)
        answer = [elem["message"] for elem in response.json()['choices']]
        return answer[0]
    except KeyError:
        return {'role': 'assistant',
                'content': '不好意思，好像哪里出了点问题，你可以换个问法或者待会再试试'}


def generate_session_id():
    """
    生成session_id
    :return:
    """
    session_id = secrets.token_urlsafe(16)
    return session_id


@app.route("/", methods=("GET", "POST"))
def index():
    if request.method == "POST":
        session_id = request.cookies.get('session_id')
        if session_id is None:
            session_id = generate_session_id()  # 生成一个新的会话 ID
            db.session.add(Session(session_id=session_id))
            db.session.commit()
        else:
            # 在数据库中查找该会话 ID，并检查是否过期
            session = Session.query.filter_by(session_id=session_id).first()
            if session is None or (datetime.utcnow() - session.created_at).total_seconds() > SESSION_EXPIRATION_TIME:
                session_id = generate_session_id()  # 生成一个新的会话 ID
                db.session.add(Session(session_id=session_id))
                db.session.commit()
        input_text = request.get_json()['msg']
        message = {"role": "user", "content": input_text}
        request_data = {
            "messages": [],
            "max_tokens": 1024,
            "model": "gpt-3.5-turbo",
            "top_p": 1,
            "temperature": 0.2,
            "n": 3,
        }
        chat = ChatLog.query.filter_by(session_id=session_id).first()
        if chat is None:
            request_data['messages'].append(message)
        else:
            request_data['messages'] = json.loads(chat.messages)
            if len(request_data['messages']) == 4:
                request_data['messages'].pop(0)
            request_data['messages'].append(message)
        answer = chatgpt35_api(request_data)
        request_data['messages'].append(answer)
        db.session.add(ChatLog(session_id=session_id, messages=json.dumps(request_data['messages'])))
        db.session.commit()
        response = make_response(answer['content'])
        response.set_cookie('session_id', session_id)
        return response

    result = request.args.get("result")
    return render_template("index.html", result=result)


if __name__ == '__main__':
    app.run("0.0.0.0", debug=True)
