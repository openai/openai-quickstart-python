import os
import openai
from csv import DictWriter
import pandas as pd
# openai.api_key = ''

# ### mount google drive
# # Load the Drive helper and mount
# from google.colab import drive, auth
# # This will prompt for authorization.
# drive.mount('/content/drive/')


def makeDavinciPrompt(question,answer,command,user_answer):
  prompt = """Suggest three names for an animal that is a superhero.
Question: {}
answer: {}
Command: {}
user_answer: {} """.format(question,answer,command,user_answer)
  return prompt

def makeGPTPromt(question,answer,command,user_answer):
  state_question = 'The question is: \n' + question
  correct_answer = "The correct answer is :\n" + answer
  command_answer = command + "\n" + user_answer
  prompt=[
      {"role": "system", "content": "You are a helpful assistant."},
      # {"temperature": temp},
      {"role": "user", "content": state_question},
      {"role": "assistant", "content": correct_answer},
      {"role": "user", "content": command_answer}
      ]
  return prompt

def askDavinci(user_prompt,gpt_model,temp):
  response = openai.Completion.create(
    model=gpt_model,
    prompt=user_prompt,
    temperature=temp
    )
  print(response['choices'][0]['text'])
  return

def askGPT(prompt,gpt_model):
  response = openai.ChatCompletion.create(
  model=gpt_model,
  messages=prompt
  )
  # prompt.append({"role": "assistant", "content": response['choices'][0]['message']['content']})
  return response

def fakeAI(prompt):
  response="this is a good response"
  prompt.append({"role": "assistant", "content": response})
  return response, prompt

### Define transcript dataframe
def get_trans(t_path):
  # check for transcript file
  global dic_fields
  dic_fields = ['Question', 'Sample Answer', 'Command', 'User Answer','Temperature', 'Model', 'Response', "Prompt Tokens", 'Completion Tokens']
  dic_header = {'Question': [], 'Sample Answer': [], 'Command':[], 'User Answer': [],'Temperature' :[], 'Model': [], 'Response': [], "Prompt Tokens":[], 'Completion Tokens':[] }

  if os.path.isfile(t_path):
    trans_df = pd.read_csv(t_path,index_col=None, names=None)
  else:
    trans_df = pd.DataFrame(dic_header)
    pd.DataFrame.to_csv(trans_df, t_path, index=True)

  # Create session_df
  session_df = pd.DataFrame(dic_header)
  # display(trans_df)
  return trans_df, session_df
#
### Write line to transcript
def write_trans(t_path, trans_line, trans_df, session_df):

  # append df_dictionary to csv
  df_dictionary = pd.DataFrame([trans_line])
  trans_df = pd.concat([trans_df, df_dictionary], ignore_index=False)
  session_df = pd.concat([session_df, df_dictionary], ignore_index=False)

  with open(t_path, 'a') as transFile:
    dictwriter_trans = DictWriter(transFile, fieldnames=dic_fields)
    dictwriter_trans.writerow(trans_line)
    transFile.close()
  # display(trans_df, session_df)
  return trans_df, session_df
#
### Save Session Transcript
def save_trans(session_df, s_path):
  # write session_Df to csv
  pd.DataFrame.to_csv(session_df, s_path, index=True)
  return