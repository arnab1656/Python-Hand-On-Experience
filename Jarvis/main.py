print("name of the moduole = ",__name__)

import speech_recognition as sr
import pyttsx3
import webbrowser
from gtts import gTTS
import pygame
import os

r = sr.Recognizer()

def speak(text):
    tts = gTTS(text)
    tts.save('current_voice.mp3') 

    # Initialize Pygame mixer
    pygame.mixer.init()

    # Load the MP3 file
    pygame.mixer.music.load('current_voice.mp3')

    # Play the MP3 file
    pygame.mixer.music.play()

    # Keep the program running until the music stops playing
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)
    
    pygame.mixer.music.unload()
    os.remove("current_voice.mp3") 


def openCommand(command):

  if(command.lower() == "open google"):
    webbrowser.open("google.com")
    speak("Your Google is Opened Sir")

  if(command.lower() == "open linkedin"):
    webbrowser.open("linkedin.com")  
    speak("Your linkedin is Opened Sir")

  else:
    speak("Cannot understand the Command Sir")


if __name__ == "__main__":

     r = sr.Recognizer()
     
     for index, name in enumerate(sr.Microphone.list_microphone_names()):
       print(f"Device {index} : {name}")

     speak("Jarvis initailized")

     while True:

      try:

        with sr.Microphone(device_index=17) as source:

          print("Speak something to catch in MircroPhone...")

          audio = r.listen(source, timeout=5, phrase_time_limit=5) 
          word = r.recognize_google(audio)

        if word:

          if "jarvis" in word.lower():

            speak("Jarvis Activated, Give me the Command Sir")
            
            with sr.Microphone(device_index=17) as source:
              audio = r.listen(source, timeout=5, phrase_time_limit=5) 
              command = r.recognize_google(audio)

            #_Sending Command
            openCommand(command) 

          else:
            speak("No Jarvis in the Sentence, So no Jarvis Activation")  

      except sr.WaitTimeoutError:
          print("No speech detected in time — retrying...")
      except sr.UnknownValueError:
          print("Could not understand the audio")
      except sr.RequestError as e:
         print(f"🔌 Could not request results from Google; {e}")   
      except Exception as e:
        print(e)   

      