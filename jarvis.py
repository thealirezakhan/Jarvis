import pyttsx3
import os
import wikipedia
import webbrowser
import datetime
import speech_recognition as sr

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[0].id)
engine.setProperty('voice', voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")

    else:
        speak("Good Evening!") 
    speak("I am Jarvis , How may i help you")    



    
def takeCommand():
    # It takes microphone input from the user and returns string output
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.adjust_for_ambient_noise(source)
        audio = r.listen(source)
        r.pause_threshold = 1  
            
            

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language= 'en-in')  
        print(f"User said: {query}\n")    

    except Exception as e:
        print(e)

        print("Say that again please...")
        return "None"
    return query    


if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand().lower()

        if 'wikipedia' in query:
            speak("Searching Wikikpedia....Please wait")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=1)
            speak("According to wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")
                
        elif 'open instagram' in query:
            webbrowser.open("instagram.com")

        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S") 
            speak(f"Sir, the time is {strTime}")   

        elif 'open code' in query:
            codePath = "C:\\Users\\AliAbbas\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)

        elif 'open steam' in query:
            code_Path= "C:\\Program Files (x86)\\Steam\\steam.exe"

        elif 'how are you' in query:
            speak("I am totally fine  sir")

        elif 'quit' or 'exit' in query:
            break
            
            

            
            

    

