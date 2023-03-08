from googleapiclient.errors import HttpError

from google_auth import get_service, read_structural_elements
import openai, secrets

# ChatGPT Model
def get_feedback():
  # Loads API key from secrets.py
  openai.api_key = secrets.api_key

  rubric_docId = "1d9ihn_EfBpyircGwLQbXjwfSyVIEXJuYNWLp-eVIX2M"
  submission_docId = "1qaM-8-rijJrpZs3SWPV5G8RSnB75GnArq8pD4LqNRac"
  
  doc_service = get_service('docs','v1')   

  rubric_doc = doc_service.documents().get(documentId=rubric_docId).execute()
  submission_doc = doc_service.documents().get(documentId=rubric_docId).execute()

  rubric = read_structural_elements(rubric_doc.get('body').get('content')).strip()
  submission = read_structural_elements(submission_doc.get('body').get('content')).strip()

  prompt = f"Use the rubric: {rubric} to decide whether the criteria P1, P2, P3, M1 and D1 have been met in the following: {submission}. Respond only with whether or not the criteria has been met."
  response = openai.ChatCompletion.create(model="gpt-3.5-turbo",messages=[{"role": "user","content":prompt}],max_tokens=1000,n=1)
  comment_content = {
    'content' : response.choices[0].message.content
  }

  drive_service = get_service('drive','v2')
  try:
    #response = drive_service.comments().batchUpdate(documentId=submission_docId, body={'requests': comment_content}).execute()
    drive_service.comments().insert(fileId=submission_docId,body=comment_content).execute()
  except HttpError as err:
    print(err)

if __name__ == "__main__":
  get_feedback()