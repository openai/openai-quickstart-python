import os
from flask import Blueprint, request, jsonify, render_template
from ..services.translation import translate_text

translation_views = Blueprint("translation_views", __name__)

@translation_views.route('/translate')
def translate():
    return render_template('index.html')

@translation_views.route('/translate-to-korean', methods=['POST'])
def translate_to_korean():
    data = request.get_json()
    input_text = data['text']
    translated_text = translate_text(input_text, "English", "Korean")
    return jsonify(translated_text=translated_text)

@translation_views.route('/translate-to-english', methods=['POST'])
def translate_to_english():
    data = request.get_json()
    input_text = data['text']
    translated_text = translate_text(input_text, "Korean", "English")
    return jsonify(translated_text=translated_text)
