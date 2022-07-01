import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib

# print("loading Vineela")

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)
CREATOR="Bhargav"
def speak(text):
    engine.say(text)
    engine.runAndWait()

def wishme():
    hour = int(datetime.datetime.now().hour)
    print(hour)

    if hour>=0 and hour<12:
            speak("good morning sir ")
    elif hour>=12 and hour<18:
            speak("good afternoon sir")
    elif hour>=18 and hour<23:
            speak("good evening sir")
    speak("i am veeneeela. how can i help you sir ")

#main program starts
def takeCommand():
    #It takes microphone input from the user and returns string output
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("TELL ME SIR...")
        r.pause_thresold = 1.5
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query=r.recognize_google(audio, language = 'en-in')
        print(f"using said: {query}\n")

    except Exception as e:
        print("say it again please")
        query= None
    return query
speak("loading veeneeela...")

wishme()
while True:
  
    query = takeCommand()

        # Logic for executing tasks based on query
    if 'wikipedia'in query.lower():
        speak('Searching Wikipedia...')
        query = query.replace("wikipedia", "")
        results = wikipedia.summary(query, sentences =2)
        speak("According to Wikipedia")
        print(results)
        speak(results)
    elif 'open youtube' in query.lower():
        url="youtube.com"
        chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
        webbrowser.get(chrome_path).open(url)
    elif 'play movies' in query.lower():
        movies_dir ="C:\\Users\\vinay\\Videos\\movies"
        movies = os.listdir(movies_dir)
        print(movies)
        os.startfile(os.path.join(movies_dir,movies[0]))
    elif 'favourite movie' in query.lower():
        movies_dir ="C:\\Users\\vinay\\Videos\\movies"
        movies = os.listdir(movies_dir)
        print(movies)
        os.startfile(os.path.join(movies_dir,movies[7]))
    elif 'play music' in query.lower():
        songs_dir ="C:\\Users\\vinay\\Music"
        songs = os.listdir(songs_dir)
        print(songs)
        os.startfile(os.path.join(songs_dir,songs[0]))
    elif 'stop'in query.lower():
        break
