import os
import openai

openai.api_key = os.getenv("OPENAI_API_KEY")

def translate_text(text, from_lang, to_lang):
    model_engine = "text-davinci-003"
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
