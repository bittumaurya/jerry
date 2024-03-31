import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
import geopy
from newsapi import NewsApiClient
import webbrowser as we
import requests
from time import sleep
import pyautogui
import clipboard


engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


def talk(text):
    engine.say(text)
    engine.runAndWait()

def Hello():
    print("hello sir I am your desktop assistant .Tell me how may I help you")
    talk("hello sir I am your desktop assistant .Tell me how may I help you")


def news(): #this function is for getting news
    newsapi = NewsApiClient(api_key='5840b303fbf949c9985f0e1016fc1155')
    print("What topic you need the news about")
    talk("What topic you need the news about")
    topic = take_command()
    data = newsapi.get_top_headlines(
        q=topic, language="en", page_size=5)
    newsData = data["articles"]
    for y in newsData:
        print(y["description"])
        talk(y["description"])

def sendWhatMsg():
    user_name = {
        'didi': '+91 8958325877 '
    }
    try:
        talk("To whom you want to send the message?")
        name = take_command()
        talk("What is the message")
        we.open("https://web.whatsapp.com/send?phone=" +
                user_name[name]+'&text='+take_command())
        sleep(6)
        pyautogui.press('enter')
        talk("Message sent")
    except Exception as e:
        print(e)
        talk("Unable to send the Message")
       



def weather():
    
    city = "greater noida"
    res = requests.get(
        f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid=16f0afad2fd9e18b7aee9582e8ce650b&units=metric").json()
    temp1 = res["weather"][0]["description"]
    temp2 = res["main"]["temp"]
    talk(
        f"Temperature is {format(temp2)} degree Celsius \nWeather is {format(temp1)}")


def take_command():
    
    #this function is to take the command
    listener = sr.Recognizer()
    with sr.Microphone() as source:
        print('listening...')
        listener.pause_threshold = 1
        voice = listener.listen(source)
    try:
        print("Recognizing...")
        command = listener.recognize_google(voice,language="en-in")
            # if 'jerry' in command:
            #     command = command.replace('jerry', '')
            #     print(command)
        print(f":Your Command : {command}\n")
    except:
        return ""
    return command.lower()


def tellDay():
     
    # This function is for telling the day
    day = datetime.datetime.today().weekday() + 1
    Day_dict = {1: 'Monday', 2: 'Tuesday',
                3: 'Wednesday', 4: 'Thursday',
                5: 'Friday', 6: 'Saturday',
                7: 'Sunday'}
     
    if day in Day_dict.keys():
        day_of_the_week = Day_dict[day]
        print(day_of_the_week)
        talk("The day is " + day_of_the_week)  
 

def location(): #this function is for getting current location 

    from geopy.geocoders import Nominatim
    loc = Nominatim(user_agent="GetLoc")
    getLoc = loc.geocode("greater noida")
    print(getLoc.address)
    talk(getLoc.address)
    print("Latitude = ", getLoc.latitude, "\n")
    print("Longitude = ", getLoc.longitude)   


def run_jerry():
    Hello()
    while True:
        command = take_command()
    # print(command)
        if 'play' in command:
            song = command.replace('play', '')
            talk('playing ' + song)
            pywhatkit.playonyt(song)
        elif 'time' in command:
            time = datetime.datetime.now().strftime('%I:%M %p')
            talk('Current time is ' + time)
            print(time)
        elif " which day it is" in command:
            tellDay()
            continue
        elif 'what is my location' in command:
            location()
            continue
        elif 'wikipedia ' in command:
            person = command.replace('wikipedia', '')
            info = wikipedia.summary(person, 1)
            print(info)
            talk(info)
        elif 'news' in command:
            news()
            continue 
        elif 'open whatsapp' in command:
            sendWhatMsg()
            continue
        elif 'weather condition' in command:
            weather()
            continue
        elif "search" in command:
            print("what you want to search?")
            talk("what you want to search?")
            we.open("https://www.google.com/search?q="+take_command())
        elif "youtube" in command:
            print("What you want to search on Youtube?")
            talk("What you want to search on Youtube?")
            pywhatkit.playonyt(take_command())
        elif ' tell me a joke' in command:
            print(pyjokes.get_joke())
            talk(pyjokes.get_joke())
        elif 'tell me your name' in command:
            print("I am Jerry. Your  Assistant")
            talk("I am Jerry. Your  Assistant")
        elif 'what is my name' in command:
            print("sir your name is Abhishek Maurya")
            talk("sir your name is Abhishek Maurya")
        elif 'bye' in command:
            talk("ok bye sir.Have a nice daY")
            print("Ok bye sir.Have a nice daY")
            exit()
        else:
            print('Please say the command again.I cannot understand')
            talk('Please say the command again.I cannot understand')


run_jerry()



