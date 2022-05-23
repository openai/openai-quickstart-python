import os, openai, csv, pandas as pd, json

openai.api_key = "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"

df = pd.read_csv(r'data/Clinical_Trials_industry_sponsors.csv')

intro_text = 'a list of companies, stock symbols and exchanges:\nBiogen: BIIB|NASDAQ\nApple: APPL|NASDAQ\n'
test_list = ['Hoffmann-La Roche','Takeda Pharmaceuticals North America, Inc.','Merck Sharp & Dohme LLC','Sanofi']

def make_prompt(rownums):
#    return(intro_text + ":\n".join(df.iloc[rownums]["name"].tolist()) + '\n')
    return(intro_text + ":\n".join(test_list) + ':\n')

def summarize_rows(rownums):
    result = openai.Completion.create(
        engine="text-davinci-002",
        prompt=make_prompt(rownums),
        temperature=0,
        max_tokens=3500,
        top_p=1.0,
        frequency_penalty=0.0,
        presence_penalty=0.0)
    return(result)

output = summarize_rows(range(0,6))

print(output)
