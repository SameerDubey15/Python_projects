# IMPORT SECTION
from http import server
from turtle import pen
import speech_recognition as sr
from datetime import datetime
import pyttsx3
import wikipedia
import webbrowser
import os
import random
import pyjokes
import smtplib

# GETTING VOICE
javis = pyttsx3.init('sapi5')
voices = javis.getProperty('voices')
javis.setProperty('voice', voices[0].id)


def speak(audio):
    '''
    function for speaking 
    '''
    javis.say(audio)
    javis.runAndWait()


def wishme():
    '''
    function for wishing user
    '''
    hour = int(datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Hii\nGood Morning")
    elif hour >= 12 and hour < 18:
        speak("Hii\nGood Afternoon")
    else:
        speak("Hii\nGood Evening")
    speak("Myself Javis, How may i help you?")


def takecommand():
    '''
    It take input from user as voice and return string
    '''
    r = sr.Recognizer()
    with sr.Microphone() as m:
        print("Listening.......")
        r.pause_threshold = 2
        r.energy_threshold = 100
        r.phrase_threshold = 0.5
        audio = r.listen(m)
    try:
        print("Recognizing....")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")
    except Exception as e:
        # print(e)
        print("Say that again please")
        return "None"
    return query


def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login("email id of self", "my password")
    server.sendmail("id of another", to, content)


if __name__ == "__main__":
    wishme()
    while True:
        query = takecommand().lower()
        if 'wikipedia' in query:
            speak('Searching in Wikipedia...')
            results = wikipedia.summary(query, sentences=2)
            speak("According to wikipedia")
            print(results)
            speak(results)
        elif 'open' in query:
            if 'youtube' in query:
                webbrowser.open("youtube.com")
            elif 'google' in query:
                webbrowser.open("google.com")
            elif 'facebook' in query:
                webbrowser.open("facebook.com")
            elif 'twitter' in query:
                webbrowser.open("twitter.com")
            elif 'wikipedia' in query:
                webbrowser.open("wikipedia.com")
            elif 'instagram' in query:
                webbrowser.open("instagram.com")
            else:
                print("Sorry, I am still learning")
        elif 'play' in query:
            if 'music' in query:
                music_dir = "path to music directory"
                songs = os.listdir(music_dir)
                os.system('xdg-open ' + os.path.join(music_dir,
                          songs[random.randint(0, len(songs)-1)]))
        elif 'take notes' in query:
            speak('What should I write?')
            note_text = takecommand()
            if(note_text != None):
                f = open('notes.txt', 'a')
                timestamp = datetime.now().strftime("%H:%M:%S")
                f.write(timestamp + '\n')
                note = note_text + '\n\n'
                f.write(note)
                f.close()
        elif 'time' in query:
            time = datetime.now().strftime("%H:%M:%S")
            speak(f"The time is {time}")
        elif 'joke' in query:
            joke = pyjokes.get_joke()
            speak(joke)
        elif 'send email' in query:
            try:
                speak('What should i write?')
                content = takecommand()
                to = "to sent"
                sendEmail(to, content)
                speak("email has been sent")
            except Exception as e:
                speak("sorry can;t able to send email")
        elif 'stop' or 'quit' in query:
            speak("ok, Have a nice day")
            break
        else:
            print("Sorry, I am still learning")
