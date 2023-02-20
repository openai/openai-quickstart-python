import os, openai, secrets


def main():
  # Loads API key from secrets.py
  openai.api_key = secrets.api_key  
  response = openai.Completion.create(model="text-davinci-003", prompt="Say this is a test", temperature=0, max_tokens=7)
  print(response.choices[0].text)

if __name__ == "__main__":
  main()