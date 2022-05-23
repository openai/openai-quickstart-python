import os, openai, csv, pandas as pd, json

openai.api_key = "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"

df = pd.read_csv(r'data/NASH_Clinical_Trials.csv')

intro_text = 'A table summarizing clinical trials:\n'
table_stub = '|drug|disease|'

def summarize_rows(rownums):
    result = openai.Completion.create(
        engine="text-davinci-002",
        prompt=intro_text + "\n".join(df.iloc[rownums]["official_title"].tolist()) + '\n' + table_stub,
        temperature=0.4,
        max_tokens=3500,
        top_p=1.0,
        frequency_penalty=0.0,
        presence_penalty=0.0)
    return(result)

def process_results(result):
    result = table_stub + result['choices'][0]['text']
    lines = result.split('\n')
    df = pd.DataFrame([x.split('|') for x in lines])
    df = df.iloc[:, 1:-1]
    new_header = df.iloc[0].to_list()
    df = df[2:]
    df.columns = new_header
    return(df[['drug','disease']])

output = summarize_rows(range(0,6))
df = process_results(output)