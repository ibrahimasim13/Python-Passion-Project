import pyttsx3
import speech_recognition as sr 
import datetime
import wikipedia
import webbrowser
import os
import sys
import pyjokes
import cv2
import face_recognition as fr
import numpy as np
from tkinter import *
from bs4 import BeautifulSoup
from tkinter import Label
from tkinter import Tk
from PIL import ImageTk, Image
import requests
import pyfirmata
import calendar
from requests import get
import pywhatkit as kit
import pyautogui
import pyowm
from pygame import mixer
import random
import wolframalpha

#API:

try:
     owm = pyowm.OWM("8ebe2d99533e0547360ffdff6afb26be")
except Exception:
    print("some features are not working")

try:
    app = wolframalpha.Client("7W7PHW-QXRAHRVULA")
except Exception:
    print("some features are not working")

url = "https://weather.com/en-PK/weather/today/l/cf5522d2a67ba145bdaac907e186a9f94f0eb96047723746d0ffe6a138be77c2"

engine = pyttsx3.init ('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice',voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishme():
    nn = int(datetime.datetime.now().hour)
    if nn==7:
        speak("good morning abraham, it is 7 am right now")
        webbrowser.open("https://www.google.com/search?q=google+weather&oq=google+weather&aqs=chrome..69i57j69i64.6351j0j7&sourceid=chrome&ie=UTF-8")
        res = query.replace("how is the weather in lahore")
        print(next(res.results).text)
        speak(next(res.results).text)   
        board = pyfirmata.Arduino('COM8')
        board.digital[7].mode = pyfirmata.OUTPUT
        board.digital[7].write(1)
        board.digital[7].write(1) 

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("good morning ")

    elif hour>=12 and hour<18:
        speak("good afternoon ")

    else:
        speak("good evening ")
        
    now = datetime.datetime.now()
    #12 hour format
    speak("it is")
    speak(now.strftime('%Y/%m/%d %I:%M'))
    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser")
    temperature = soup.find('span',class_="CurrentConditions--tempValue--3KcTQ").text
    weatherPrediction = soup.find('div',class_="CurrentConditions--phraseValue--2xXSr").text
    speak("the temperature in lahore is")
    speak(temperature)
    speak("it will most probably be")
    speak(weatherPrediction)
    speak("can i do something for you")

def FaceRecognition():
    video_capture = cv2.VideoCapture(0)

    ibrahim_image = fr.load_image_file("face.jpg")
    ibrahim_face_encoding = fr.face_encodings(ibrahim_image)[0]

    known_face_encondings = [ibrahim_face_encoding]
    known_face_names = ["Ibrahim"]

    while True: 
        ret, frame = video_capture.read()

        rgb_frame = frame[:, :, ::-1]

        face_locations = fr.face_locations(rgb_frame)
        face_encodings = fr.face_encodings(rgb_frame, face_locations)

        for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):

            matches = fr.compare_faces(known_face_encondings, face_encoding)

            name = "Unknown"

            face_distances = fr.face_distance(known_face_encondings, face_encoding)

            best_match_index = np.argmin(face_distances)
            if matches[best_match_index]:
                name = known_face_names[best_match_index]
            
            cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)

            cv2.rectangle(frame, (left, bottom -35), (right, bottom), (0, 0, 255), cv2.FILLED)
            font = cv2.FONT_HERSHEY_SIMPLEX
            cv2.putText(frame, name, (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)

        cv2.imshow('Webcam_facerecognition', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break


    video_capture.release()
    cv2.destroyAllWindows()
 
def takeCommand():
    #it takes microphone input from the user and returns string output 

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("listening...")
        r.pause_threshold = 1 
        audio = r.listen(source)


        try:
            print("recognizing...")
            query = r.recognize_google(audio, language='en-uk')
            print(f"user said: {query}\n")

        except Exception as e:
            # print(e)
            print("can you say that again please")
            return "none"
        return query

def screenshot():
    img = pyautogui.screenshot()
    img.save("C:\\personal server\\TESS (ORIGINAL)\\screenshots.png")

if __name__ == "__main__":
    wishMe()
    wishme()
    while True:
        query = takeCommand().lower()

        # logic for executing tasks based on query 
        if 'who is' in query:
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=4)
            speak("according to the information i was able to gather")
            print(results)
            speak(results)

#CREATIVE SPEECH/BAISIC COMMUNICATION, WHAT REPLY YOU GET WHEN YOU ASK HER SOMETHING?
        if "hello" in query or "hi" in query or "hola" in query or "whatsup" in query or "whats up" in query or "hey" in query or "salam" in query:
            d = 'hello ', 'hi ', 'welcome back ', 'hello there', 'hi', "hello"
            speak(random.choice(d))

        if "goodmorning" in query or "morning tess" in query:
            V = "goodmorning ", "goodmorning , how are you today", "goodmorning"
            speak(random.choice(V))

        if 'you there' in query or 'you awake' in query:
            a = 'yes ', 'for you  always', 'up and ready for you ', 'always', "at your service "
            speak(random.choice(a))

        if "tired" in query or "exhausted" in query or "drained" in query or "drowsy" in query or "weary" in query:
            O = " you shall get some rest then", "then you shall take a brake ", " i think taking a little time off would be good for you", " you shall drink some coffe"
            speak(random.choice(O))

        if "im so happy" in query or "happy" in query:
            Q = "glad to hear that ", "thats great ", "happy to hear "
            speak(random.choice(Q))

        if "working" in query:
            H = "alright , ill be here if you need me", "alright ", "ill leave you to it "
            speak(random.choice(H))

        if "bored" in query:
            L = "what can i do for you ", "what do you want me to do ", "is there anyway i can help "
            speak(random.choice(L))

        if "goodnight" in query or "goodnight test" in query or "night test" in query or "night" in query:
            D =  "goodnight ", "goodnight  sleep well"
            speak(random.choice(D))

        if "say" in query:
            speak(f"{query}")

        if 'say my name' in query or "who am I" in query:
            R = " your name is Ibrahim", "you name is IBRAHAM asim"
            speak(random.choice(R))

        if "how are you" in query or "hru" in query or "how you doing" in query:
            J = "im good as usual ", "im fine "
            speak(random.choice(J))

        elif "open camera" in query or "camera" in query:
            speak("alright ")
            campath = "C:\\personal server\\TESS (ORIGINAL)\\cam.py"
            os.startfile(campath)
#ALL THE MAJOR COMMANDS

        elif ' open youtube' in query or  'youtube for me' in query:
            webbrowser.open("https://www.youtube.com/")

        elif ' open instagram' in query or 'open insta' in query:
            webbrowser.open("https://www.instagram.com/")  

        elif "what can you do" in query or "what are your capabilities" in query:
            A = "i can do many things", "i can do many things such as andvanced calculations and manage your room and computer all alone"
            speak(random.choice(A))

        elif ' messages' in query or 'messenger' in query or 'messenger messages' in query:
            webbrowser.open("https://www.messenger.com")

        elif 'discord' in query or 'disc' in query or 'discord messages' in query or 'discord for any new messages' in query:
            webbrowser.open("https://discord.com/channels/@me/778030403147268130")
            speak("seems like you are all caught up ")

        elif 'homework' in query or ' homework test' in query:
            webbrowser.open("https://classroom.google.com/u/0/h") 

        elif 'music' in query:
                music_dir = 'C:\\songs\\fav songs'
                songs = os.listdir(music_dir)
                print(songs)
                os.startfile(os.path.join(music_dir, songs[1]))

        elif 'something better' in query:
            speak('what about this then ')
            music_dir = 'C:\\songs\\better songs'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'play some drake' in query or 'drake' in query or 'test hit me with some drake' in query:
            speak('as you wish')
            music_dir = 'C:\\songs\\fav songs'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[2]))

        elif 'personal server' in query or 'personal folder' in query:
            speak('okay ')
            personalpath = 'C:\\personal server'
            os.startfile(personalpath)

        elif "type hi" in query:
            pyautogui.press("h")
            pyautogui.press("i")
            pyautogui.press("enter")

        elif 'time' in query:
            now = datetime.datetime.now()
            #24-hour format
            print(now.strftime('%Y/%m/%d %H:%M:%S'))
            #12-hour format
            speak(now.strftime('%Y/%m/%d %I:%M'))
            
        elif 'spotify' in query or 'open spotify' in query:
            spotifyPath = "C:\\Users\\Dell\\AppData\\Roaming\\Spotify\\Spotify.exe"
            os.startfile(spotifyPath)
        
        elif 'whatsapp' in query or 'open whatsapp' in query:
            whatsappPath = "C:\\Users\\Dell\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\WhatsApp\\whatsapp"
            speak('okay')
            os.startfile(whatsappPath)

        elif "wake up" in query or "wake up im back" in query:
            music_dir = 'C:\\songs\\better songs'
            songs = os.listdir(music_dir)
            os.startfile(os.path.join(music_dir, songs[0]))
            board = pyfirmata.Arduino('COM8')
            board.digital[6].mode = pyfirmata.OUTPUT
            board.digital[6].write(1)
            board.digital[6].write(1)
            board.digital[6].write(1)
            board.digital[7].mode = pyfirmata.OUTPUT
            board.digital[7].write(1)
            board.digital[7].write(1)
            board.digital[7].write(1)
            board.digital[5].mode = pyfirmata.OUTPUT
            board.digital[5].write(1)
            board.digital[5].write(1)
            board.digital[5].write(1)
            Z = "welcome back ", "welcome home "
            speak(random.choice(Z))
            

        elif 'remove background' in query or 'background' in query or "remove the background" in query:
            webbrowser.open("https://www.remove.bg/upload")


        elif 'network speed' in query or 'internet speed' in query or ' internet' in query or "network" in query:
            speak('checking')
            webbrowser.open("https://fast.com/")
            speak('here are the results')

        elif ' browser' in query or ' chrome' in query:
            chromepath = "C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\google chrome"
            os.startfile(chromepath)

        elif 'what is the temperature in lahore' in query:
            try:
                res = app.query(query)
                speak("the temperature is")
                print(next(res.results).text)
                speak(next(res.results).text)
            except:
                print("cant connect to the internet")

        elif  'weather' in query:
            try:
                res = app.query(query)
                speak("in lahore")
                print(next(res.results).text)
                speak(next(res.results).text)
            except:
                print("cannot connect to the internet")

        elif  'calculate' in query:
            try:
                res = app.query(query)
                speak("the answer is")
                query = query.replace("res", "")
                print(next(res.results).text)
                speak(next(res.results).text)
            except:
                print("cannot connect to the internet")     

        elif  'what' in query:
            try:
                res = app.query(query)
                query = query.replace("res", "")
                print(next(res.results).text)
                speak(next(res.results).text)
            except:
                print("cannot connect to the internet") 

        elif  'where' in query:
            try:
                res = app.query(query)
                query = query.replace("res", "")
                print(next(res.results).text)
                speak(next(res.results).text)
            except:
                print("cannot connect to the internet") 

        elif 'screenshot' in query:
            screenshot()

        elif 'pakistan on the world map' in query:
            speak("okay ")
            webbrowser.open('https://www.google.com/maps/@31.5175796,66.2833507,3273276m/data=!3m1!1e3')

        elif 'tess how much traffic do we have in lahore today' in query or 'tess show me the traffic in lahore' in query:
            speak('accessing live sattelite footage')
            webbrowser.open('https://www.google.com/maps/place/Lahore,+Punjab,+Pakistan/@31.4826352,74.0541994,98190m/data=!3m1!1e3!4m5!3m4!1s0x39190483e58107d9:0xc23abe6ccc7e2462!8m2!3d31.5203696!4d74.3587473!5m1!1e1')
    
        elif 'tess show me the earth' in query:
            speak("okay ")
            webbrowser.open('google.com/maps/@24.1625899,71.4337495,10539009m/data=!3m1!1e3!5m1!1e1')
        
        elif "joke" in query:
            P = "i've got one", "heres one", "i have a good joke in mind"
            speak(random.choice(p))
            speak(pyjokes.get_joke())

        elif 'test show me the north pole' in query:
            webbrowser.open('https://www.google.com/maps/place/North+Pole/@56.823374,-50.4944029,8114113m/data=!3m1!1e3!4m5!3m4!1s0x4f9344da9515b951:0x4518d0c4d5c68876!8m2!3d89.9999999!4d-135!5m1!1e1')

        elif 'test show me the sun' in query:
            speak('alright')
            webbrowser.open('https://www.google.com/maps/place/North+Pole/@43.3095607,-29.2089104,22957000m/data=!3m1!1e3!4m5!3m4!1s0x4f9344da9515b951:0x4518d0c4d5c68876!8m2!3d89.9999999!4d-135!5m1!1e1')

#IMPORTANT TASKS#
#CLOSING PROGRAMS AND KILLING ONGOING TASKS/SHUTTING DOWN OR RESTARTING THE SYSTEM


        elif 'close the browser' in query or 'test close the browser' in query:
            speak("okay abraham")
            os.system("TASKILL /f /im chrome.exe")

        elif 'close spotify' in query or 'test close spotify' in query:
            speak("okay abraham")
            os.system("TASKKILL /f /im spotify.exe")
        
        elif 'shutdown' in query:
            speak('shutting down')
            os.system("shutdown /s /t 5")

        elif 'restart' in query:
            speak('restarting the system')
            os.system("shutdown /r /t 5")

        elif 'switch the window' in query or 'test switch the window' in query:
            pyautogui.keyDown("alt")
            pyautogui.press("tab")
            pyautogui.keyUp("alt")

#music/play and pause music section

        elif "Play some Music", " Music " in query:
            speak('yes ')
            music_dir = 'C:\\songs\\fav songs'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))

        elif "a remix" in query:
            speak("i think you would like this ")
            music_dir = 'C:\\songs\\better songs'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[1]))


        elif "stop" in query:
             os.system("TASKKILL /f /im GROOVE.EXE")
        
        elif 'on youtube' in query:
            kit.playonyt(f"{query}")

        elif 'new folder' in query or ' new project' in query or 'new directory' in query or 'test open a new project on my personal server' in query:
            os.makekdir('new folder')
            speak('your folder has been made')


        elif 'delete this folder' in query or 'test delete the folder' in query:
            os.rmdir('new folder')
            speak('the folder has been deleted')

        elif 'play some strings' in query or 'test play my jam' in query:
                music_dir = 'C:\\songs\\fav songs'
                songs = os.listdir(music_dir)
                print(songs)
                os.startfile(os.path.join(music_dir, songs[4]))

#home automation system:
        elif "turn on the light" in query:
            speak("alright ")
            board = pyfirmata.Arduino('COM8')
            board.digital[7].mode = pyfirmata.OUTPUT
            board.digital[7].write(1)
            board.digital[7].write(1)

        elif "turn off the light" in query:
            speak("alright ")
            board = pyfirmata.Arduino('COM8')
            board.digital[7].mode = pyfirmata.OUTPUT
            board.digital[7].write(0)
            board.digital[7].write(0)
            board.digital[7].write(0)
        
        elif "turn off all the lights" in query:
            speak("alright ")
            board = pyfirmata.Arduino('COM8')
            board.digital[6].mode = pyfirmata.OUTPUT
            board.digital[6].write(0)
            board.digital[6].write(0)
            board.digital[6].write(0)
            board.digital[7].mode = pyfirmata.OUTPUT
            board.digital[7].write(0)
            board.digital[7].write(0)
            board.digital[7].write(0)
            board.digital[5].mode = pyfirmata.OUTPUT
            board.digital[5].write(0)
            board.digital[5].write(0)
            board.digital[5].write(0)

        elif "turn on all the lights" in query:
            board = pyfirmata.Arduino('COM8')
            board.digital[6].mode = pyfirmata.OUTPUT
            board.digital[6].write(1)
            board.digital[6].write(1)
            board.digital[6].write(1)
            board.digital[7].mode = pyfirmata.OUTPUT
            board.digital[7].write(1)
            board.digital[7].write(1)
            board.digital[7].write(1)
            board.digital[5].mode = pyfirmata.OUTPUT
            board.digital[5].write(1)
            board.digital[5].write(1)
            board.digital[5].write(1)
            speak("all lights have been turned on")
