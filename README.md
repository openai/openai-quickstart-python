# OpenAI API Quickstart - Python

This repository hosts multiple quickstart apps for different OpenAI API endpoints (chat, assistants, etc). Check out the `examples` folder to try out different examples and get started using the OpenAI API.

## Basic request

To send your first API request with the [OpenAI Python SDK](https://github.com/openai/openai-python), make sure you have the right [dependencies installed](https://platform.openai.com/docs/quickstart?context=python) and then run the following code:

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

## Setup

1. If you don’t have Python installed, install it [from Python.org](https://www.python.org/downloads/).

2. [Clone](https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository) this repository.

3. Navigate into the project directory:

   ```bash
   $ cd openai-quickstart-python
   ```

4. Create a new virtual environment:

   - macOS:

     ```bash
     $ python -m venv venv
     $ . venv/bin/activate
     ```

   - Windows:
     ```cmd
     > python -m venv venv
     > .\venv\Scripts\activate
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

This step depends on the app itself. If the code uses flask (like the chat-basic example), you can run:

```bash
$ flask run
```

You should now be able to access the app from your browser at the following URL: [http://localhost:5000](http://localhost:5000)!

If the code is just a simple Python script, you can run it with:

```bash
$ python my_file.py
```
