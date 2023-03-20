# OpenAI API Quickstart - Python example app

This is an example pet name generator app used in the OpenAI API [quickstart tutorial](https://beta.openai.com/docs/quickstart). It uses the [Flask](https://flask.palletsprojects.com/en/2.0.x/) web framework. Check out the tutorial or follow the instructions below to get set up.

## Setup

1. If you don’t have Python installed, [install it from here](https://www.python.org/downloads/).

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

7. Add your [API key](https://beta.openai.com/account/api-keys) to the newly created `.env` file.

8. Run the app:

   ```bash
   $ flask run
   ```

You should now be able to access the app at [http://localhost:5000](http://localhost:5000)! For the full context behind this example app, check out the [tutorial](https://beta.openai.com/docs/quickstart).

--------------

## Dockerized Python app

This repository allows you to run a dockerized version of the Python [OpenAI Quick Start Guide for ChatGPT](https://platform.openai.com/docs/quickstart/build-your-application).

### Requirements
Before you begin, make sure that you have the following software installed on your system:

* Docker
* Git

### Installation

To get started, clone the repo on your local machine:

```
git clone https://github.com/schererjulie/openai-quickstart-docker.git
cd openai-quickstart-docker
```

Next, copy and paste `.env.example` to `.env` and then add your API key.

```
cp .env.example .env
vim .env
```

## Running Docker

Build the Docker image and run the container using the command below:

`make up`

This will:
1. Stop any running containers called `openai` as a precaution.
2. Create a Docker image called `openai` that contains all the dependencies required to run the OpenAI Quick Start Guide.
3. Start the Docker container, mapping the container port 5000 to port 5000 on your local machine.

You can then access the app by going to [http://127.0.0.1:5000/](http://127.0.0.1:5000/).

### Cleaning Up 

To free up system resources once you're done, use the following command to stop and remove the Docker container and image.

`make down`

This command will take care of stopping and removing any running containers with the name `openai`, as well as deleting the Docker image called `openai`.

## Acknowledgments
This repo was created OpenAI and modified by Julie Scherer. 

Thanks to OpenAI for providing the Quick Start Guide, Docker for making containerization easy, and chatGPT for helping me update this README :-D