# OpenAI API Quickstart - Python example app

This is an example chat app intended to get you started with your first OpenAI API project. It uses the [Chat Completions API](https://platform.openai.com/docs/api-reference/chat) to create a simple general purpose chat app with streaming.

## Basic request

To send your first API request with the OpenAI Python SDK, make sure you have the right [dependacies installed](https://platform.openai.com/docs/quickstart?context=python) and then run the following code:

```python
from openai import OpenAI
client = OpenAI()

completion = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "system", "content": "You are a helpful assistant."},
    {"role": "user", "content": "Hello!"}
  ]
)

print(completion.choices[0].message)
```

This quickstart app builds on top of the example code above, with additional features like streaming.

## Setup

1. If you don’t have Python installed, install it [from Python.org](https://www.python.org/downloads/).

2. Clone this repository.

3. Navigate into the project directory:

   ```bash
   $ cd openai-quickstart-python
   ```

4. Create a new virtual environment:

   ```bash
   $ python -m venv venv
   $ . venv/bin/activate
   ```

5. Install the requirements:

   ```bash
   $ pip install -r requirements.txt
   ```

6. Make a copy of the example environment variables file:

   ```bash
   $ cp .env.example .env
   ```

7. Add your [API key](https://platform.openai.com/api-keys) to the newly created `.env` file.

8. Run the app:

   ```bash
   $ flask run
   ```

You should now be able to access the app from your browser at the following URL: [http://localhost:5000](http://localhost:5000)!
