
import pyttsx3  # pip install pyttsx3
import speech_recognition as sr  # pip install speechRecognition
import datetime
import wikipedia  # pip install wikipedia
import webbrowser
import os
import smtplib
import cv2
import random
from requests import get
import smtplib

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning!")

    elif hour >= 12 and hour < 18:
        speak("Good Afternoon!")

    else:
        speak("Good Evening!")

    speak("I am Jarvis Sir. Please tell me how may I help you")


def takeCommand():
    # It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)
        print("Say that again please...")
        return "None"
    return query


def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('priyanshusingh0000@gmial.com', 'ishu@123')
    server.sendmail('brijbhansingh195@gmail.com', to, content)
    server.close()


if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand().lower()
        # Logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        # elif 'play music' in query:
        #     music_dir = 'D:\\Non Critical\\songs\\Favorite Songs2'
        #     songs = os.listdir(music_dir)
        #     rd = random.choice(songs)
        #     for song in songs:
        #         if song.endswith('.mp3'):
        #             os.startfile(os.path.join(music_dir, song))

        elif "ip address" in query:
            ip = get('https://api.ipify.org').text
            speak(f"your IP address is{ip}")

        elif 'hello' in query:
            speak("Hello sir How can help you")

        elif 'nothing' in query:
            speak("Ok sir ")

        elif 'how are you jarvis' in query:
            speak("I am fine Sir")

        elif 'time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")

        elif 'open vs code' in query:
            codePath = "C:\\Users\\HP\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)

        elif 'open telegram' in query:
            teleGram = "C:\\Users\\HP\\AppData\\Roaming\\Telegram Desktop\\Telegram.exe"
            os.startfile(teleGram)

        elif 'open notepad' in query:
            notepad = "C:\\Windows\\system32"
            os.startfile(notepad)

        elif 'open microsoft edge' in query:
            edge = "C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe"
            os.startfile(edge)

        elif 'open chrome' in query:
            ChromeSearch = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
            os.startfile(ChromeSearch)

        elif "youtube search" in query:
            Query = query.replace("jarvis", "")
            query = Query.replace("youtube search", "")
            from Features import YouTubeSearch
            YouTubeSearch(query)

        elif "search" in query:
            Query = query.replace("jarvis", "")
            query = Query.replace(" search", "")
            from Features import Search
            Search(query)

        elif "open google" in query:
            speak("Sir, what should I search on google")
            cm = takeCommand().lower()
            webbrowser.open(f"{cm}")

        elif "open camera" in query:
            cap = cv2.VideoCapture(0)
            while True:
                ret, img = cap.read()
                cv2.imshow('webcam', img)
                if cv2.waitKey(1) & 0xff == ord('c'):
                    break
            cap.release()
            cv2.destroyAllWindows()

        elif 'open command prompt' in query:
            os.system("start cmd")

        elif 'email to priyanshu' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "priyanshusingh00004@gmail.com"
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry my friend priyanshu bhai. I am not able to send this email")
