# def takeCommand():
#     r = sr.Recognizer()
#     with sr.Microphone() as source:
#         r.pause_threshold = 1
#         audio = r.listen(source)
#         query = r.recognize_google(audio, language ="en-in")
#         print(f"User said : {query}")
#         return query


# import win32com.client

# speaker = win32com.client.Dispatch("SAPI.SpVoice")
# speaker.Speak("Hello, I am Viro AI")

# print('Listening.....')
# text = takeCommand()
# speaker(text)



import speech_recognition as sr
import win32com.client
import webbrowser
# import openai
import os
import datetime

# Initialize the speaker
speaker = win32com.client.Dispatch("SAPI.SpVoice")

# Define speak function
def say(text):
    speaker.Speak(text)

# Define listen to user
def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.pause_threshold = 0.8
        audio = r.listen(source)
        try:
            query = r.recognize_google(audio, language="en-in")
            print(f"User said: {query}")
            return query
        except Exception as e:
           return "Some error Occured. sorry from Viro AI"

# Speak initial message
print("Hello, I am Viro AI")
say("Hello, I am Viro AI")
print('Listening.....')
# text = takeCommand()
# speaker(text)

# Take voice input and respond
while True:
  print("Listening...")
  query = takeCommand()
  print("Recognizing....")

  # webbrowser define
  sites = [["youtube", "https://www.youtube.com"], ["wikipedia", "https://www.wikipedia.com"], ["google", "https://www.google.com"],["instagram", "https://www.instagram.com"],["whatsapp", "https://web.whatsapp.com"], ]
  for site in sites:
     if f"Open {site[0]}".lower() in query.lower():
        say(f"Opening {site[0]} sir...")
        webbrowser.open(site[1])

    # music define    
  if "open music" in query:
        musicPath = (r"C:\Users\vk010\OneDrive\Desktop\ViroAI\test song.mp3")
        say(f"Opening music sir...")
        os.startfile(musicPath)

    # Date&time define
  if "the time" in query:
        strfTime = datetime.datetime.now().strftime("%H:%M:%S")
        say(f"Sir, the time is {strfTime}")

