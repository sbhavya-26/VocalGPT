import google.generativeai as genai
import speech_recognition as sr
import pyttsx3

genai.configure(api_key = "AIzaSyDpMCKtlGufhsoPnYNZOkbQ1QtGasqaiHI")

mymodel = genai.GenerativeModel('gemini-1.5-flash')
chat = mymodel.start_chat()

r = sr.Recognizer()
engine = pyttsx3.init()
while True:
       try:
            with sr.Microphone() as source:
                print("hey say something:\n")
                audio = r.listen(source)
                
            question = r.recognize_google(audio)

            if 'stop' in question:
                break

            print("you asked:" + question)
            response = chat.send_message(question)
            print("GEMINI :",response.text)
            engine.say(response.text)
            engine.runAndWait()
       except:
                print("problem with getting audio input")