"""
Install the Google AI Python SDK

$ pip install google-generativeai

See the getting started guide for more information:
https://ai.google.dev/gemini-api/docs/get-started/python
"""


#do dieu kien chua cho phep nen em chi moi lam voi gemini thoi nen thay va cac anh thong cam dum em nhe

import os
import google.generativeai as genai
from dotenv import load_dotenv
import pyttsx3

load_dotenv()

def SpeakText(command):
    engine = pyttsx3.init()
    engine.say(command)
    engine.runAndWait()


genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# Create the model
# See https://ai.google.dev/api/python/google/generativeai/GenerativeModel

# Create the model
generation_config = {
  "temperature": 1,
  "top_p": 0.95,
  "top_k": 40,
  "max_output_tokens": 8192,
  "response_mime_type": "text/plain",
}

model = genai.GenerativeModel(
  model_name="gemini-2.0-flash",
  generation_config=generation_config,
)


chat_session = model.start_chat(
    history=[]
)

stops = ["stop", "bye", "tam biet", "bye bye", "bai bai"]

print("Bot: Hello, how can I help you?")
print()

while True:

    user_input = input("You: ")
    print()

    if user_input.lower() in stops:
        break
    response = chat_session.send_message(user_input)

    model_response = response.text.lower()

    print(f'Bot: {model_response}')
    SpeakText(model_response)
    print()

    chat_session.history.append({"role": "user", "parts": [user_input]})
    chat_session.history.append({"role": "model", "parts": [model_response]})