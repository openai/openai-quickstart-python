import openai
openai.api_key = "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"

def translate_message(message, source_language, target_language):
    response = openai.Completion.create(
        engine="davinci",
        prompt=f"Translate '{message}' from {source_language} to {target_language}",
        temperature=0.5,
        max_tokens=1024,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )

    translated_text = response.choices[0].text.strip()
    return translated_text
