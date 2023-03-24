import os
import openai
import socket


from flask import Flask, request, jsonify, render_template


app = Flask(__name__)


app = Flask(__name__)
openai.api_key = os.getenv("OPENAI_API_KEY")



def translate_text(text, from_lang, to_lang):
    model_engine = "text-davinci-002"
    prompt = f"Translate the following {from_lang} text to {to_lang}: {text}"

    response = openai.Completion.create(
        engine=model_engine,
        prompt=prompt,
        max_tokens=100,
        n=1,
        stop=None,
        temperature=0.5,
    )

    translated_text = response.choices[0].text.strip()
    return translated_text

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/translate-to-korean', methods=['POST'])
def translate_to_korean():
    data = request.get_json()
    input_text = data['text']
    translated_text = translate_text(input_text, "English", "Korean")
    return jsonify(translated_text=translated_text)

@app.route('/translate-to-english', methods=['POST'])
def translate_to_english():
    data = request.get_json()
    input_text = data['text']
    translated_text = translate_text(input_text, "Korean", "English")
    return jsonify(translated_text=translated_text)

print("After methods")

def find_available_port():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind(("", 0))
        return s.getsockname()[1]



if __name__ == '__main__':
    app.run(debug=True)




