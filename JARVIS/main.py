import speech_recognition as sr
import webbrowser
import pyttsx3

recognizer = sr.Recognizer()
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def processCommand(c):
    if "Open google" in c.lower:
        webbrowser.open("google.com")  
    elif "Open facebook"  in c.lower:
        webbrowser.open("facebook.com") 
    elif "Open youtube" in c.lower:
        webbrowser.open("youtube.com")      


if __name__ == "__main__":
    speak("Initializing Raamu....")
    # LISTEN FOR THE WAKE WORD JARVIS
    while True:
        r = sr.Recognizer()
       
        print("recognizing...")
    # recognize speech 
        try:
            with sr.Microphone() as source:
                print("Listening...")
                audio = r.listen(source, timeout=2, phrase_time_limit=1)
                word= r.recognize_google(audio)
            if(word.lower()=="raamu"):
                speak("Ya")
                with sr.Microphone() as source:
                    print("Raamu jaaaagg gya ...")
                    audio = r.listen(source)
                    command = r.recognize_google(audio)

                    processCommand(command)
        except Exception as e:
            print("Error; {0}".format(e))
           