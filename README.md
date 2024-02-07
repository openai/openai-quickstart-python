# OpenAI API Quickstart - Python example app

This is an example chat app intended to get you started with your first OpenAI API project. It uses the [Chat Completions API](https://platform.openai.com/docs/api-reference/chat) to create a simple general purpose chat interface with streaming.

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

You should now be able to access the app at [http://localhost:5000](http://localhost:5000)!
