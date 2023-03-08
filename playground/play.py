from __future__ import print_function

import os.path

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

import openai, secrets

# Da-Vinci Model
def main_davinci():
  # Loads API key from secrets.py
  openai.api_key = secrets.api_key  
  response = openai.Completion.create(model="text-davinci-003", prompt="Say this is a test", temperature=0, max_tokens=100)
  print(response.choices[0].text)

# ChatGPT Model
def main_chat():
  # Loads API key from secrets.py
  openai.api_key = secrets.api_key

  prompt = "Hello!"
  response = openai.ChatCompletion.create(model="gpt-3.5-turbo",messages=[{"role": "user","content":prompt}],max_tokens=1000,n=1)
  print(response.choices[0].message.content)

if __name__ == "__main__":
  main_chat()
