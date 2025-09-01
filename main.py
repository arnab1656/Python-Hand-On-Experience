print("name of the moduole = ",__name__)

import speech_recognition as sr
import pyttsx3
import webbrowser

r = sr.Recognizer()
engine = pyttsx3.init()


def speak(text):
  engine.say(text)
  engine.runAndWait()

def openCommand(command):

  if(command.lower() == "open google"):
    webbrowser.open("google.com")
  if(command.lower() == "open linkedin"):
    webbrowser.open("linkedin.com")  
  else:
    print("Else Command")  


if __name__ == "__main__":

     r = sr.Recognizer()
     
     for index, name in enumerate(sr.Microphone.list_microphone_names()):
       print(f"Device {index} : {name}")

     while True:

      try:

        with sr.Microphone(device_index=17) as source:
          print("I am Listening...")
          print("Speak something to catch in MircroPhone...")

          audio = r.listen(source, timeout=5, phrase_time_limit=5) 
          word = r.recognize_google(audio)

        if word:

          if "jarvis" in word.lower():

            speak("Jarvis Activated")
            print("Jarvis Activated")
            
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

      