import pyttsx3
import speech_recognition as sr
import wikipedia
import pyjokes
import random
import requests
import datetime
import os

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def command():
    r = sr.Recognizer()
    while True:
        with sr.Microphone() as source:
            print("Alex: Listening...")
            audio = r.listen(source)
            try:
                query = r.recognize_google(audio)
                print(f"master:{query}")
                return query
                break
            except:
                print("Try Again")


while True:
    query = command().lower()  # takes user command

    if 'name' in query:
        speak("Hello! My  Name is Alex")
    elif 'are you single' in query:
        answers = ['I am in a relationship with wifi',
                   'No, I love spending time thinking about my crush wifi']
        speak(random.choice(answers))
    elif 'hate' in query:
        speak("I hate when people called me a machine")
    elif 'love' in query:
        speak("I loves to chat with machines like you")
    # time
    elif 'time' in query:
        time = datetime.datetime.now().strftime('%I:%M %p')
        speak(f"It's {time} ")

    # celebrity
    elif 'who is' in query:
        query = query.replace('who is', "")
        speak(wikipedia.summary(query, 2))

    # Joke
    elif 'joke' in query:
        speak(pyjokes.get_joke())

    # news
    elif 'news' in query:
        def trndnews():
            url = "http://newsapi.org/v2/top-headlines?country=in&apiKey=59ff055b7c754a10a1f8afb4583ef1ab"
            page = requests.get(url).json()
            article = page["articles"]
            results = []
            for ar in article:
                results.append(ar["title"])
            for i in range(len(results)):
                print(i + 1, results[i])
            speak("here are the top trending news....!!")
            speak("Do yo want me to read!!!")
            reply = command().lower()
            reply = str(reply)
            if reply == "yes":
                speak(results)
            else:
                speak('ok!!!!')
                pass
        trndnews()

    # music
    elif 'music' in query:
        music_dir = 'E:\\music'
        songs = os.listdir(music_dir)
        song = random.randint(0, len(songs)-1)
        print(songs[song])
        speak(f"playing{songs[song]}")
        os.startfile(os.path.join(music_dir, songs[0]))

    elif "bye" in query:
        speak("Have a nice day ! ")
        break
    else:
        speak("I don't understand what you are saying")
