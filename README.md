# OpenAI API Python playground

This isa playground for the OpenAI API, adapted from the [quickstart tutorial](https://beta.openai.com/docs/quickstart). The pet name generator uses the [Flask](https://flask.palletsprojects.com/en/2.0.x/) web framework. 

## Setup

1. If you don’t have Python installed, [install it from here](https://www.python.org/downloads/).

2. Clone this repository.

3. Navigate into the project directory:

   ```bash
   $ cd openai-playground
   ```

4. Create a new virtual environment:

   ```bash
   $ python -m venv .venv
   $ . .venv/bin/activate
   ```

5. Install the requirements:

   ```bash
   $ pip install -r requirements.txt
   ```

The two directories of interest are `playground` and `pet_gen_template`. 

To run the apps in the `playground` directory, continue with the following steps:

6. Make a copy of the example secrets file:

   ```bash
   $ cp secrets_example.py secrets.py
   ```

7. Add your [API key](https://beta.openai.com/account/api-keys) to the newly created `secrets.py` file

8. Run the app:

   ```bash
   $ python play.py
   ```

To run the flask app within the `pet_gen_template` directory, continue with the following steps:

6. Make a copy of the example environment variables file:

   ```bash
   $ cp .env.example .env
   ```

7. Add your [API key](https://beta.openai.com/account/api-keys) to the newly created `.env` file

8. Run the app:

   ```bash
   $ flask run
   ```

You should now be able to access the app at [http://localhost:5000](http://localhost:5000).