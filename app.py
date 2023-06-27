import openai
from flask import Flask, redirect, render_template, request, url_for
from functions import *
app = Flask(__name__)
openai.api_key = os.getenv("OPENAI_API_KEY")

question = "Question"
@app.route("/", methods=("GET", "POST"))
def index():

    if request.method == "POST":
        Question = request.form["Question"]
        Sample_Answer = request.form["Correct Answer"]
        User_answer = request.form["Student's Answer"]
        Command = request.form["Command"]
        Temperature = request.form["Temperature"]
        GPT_model = request.form["model"]
        Transcript_path = "./history/transcript.csv"
        Prompt="{}, {}, {}, {}, {}".format(Question,Sample_Answer,User_answer,Command,Temperature,Transcript_path)
        
        #load transcript file
        trans_DF, session_DF = get_trans(Transcript_path)

        # return redirect(url_for("index", result=response.choices[0].text))
        
        if GPT_model != "gpt-3.5-turbo" and GPT_model != "gpt-4":
            Prompt = makeDavinciPrompt(Question,Sample_Answer,Command,User_answer)
            Response = askDavinci(Prompt,GPT_model,Temperature)
        else:
            Prompt = makeGPTPromt(Question,Sample_Answer,Command,User_answer)
            # Response,Prompt = fakeAI(Prompt)
            Response = askGPT(Prompt,GPT_model)

        # print(Response['choices'][0]['message']['content']+"\n\n")
        # Write to transcript
        Trans_line = {'Question': Question, 'Sample Answer': Sample_Answer, 'Command':Command, 'User Answer': User_answer,'Temperature' :Temperature, 'Model': GPT_model, 'Response': Response['choices'][0]['message']['content'], "Prompt Tokens":Response['usage']['prompt_tokens'], 'Completion Tokens':Response['usage']['completion_tokens'] }
        trans_DF, session_DF = write_trans(Transcript_path,Trans_line, trans_DF, session_DF)
        return redirect(url_for("index", result=Response['choices'][0]['message']['content']))

    result = request.args.get("result")

    return render_template("GPT_interface.html", result=result)
