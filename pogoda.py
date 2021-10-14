import random
import pyttsx3
import time
import speech_recognition as sr
from bs4 import BeautifulSoup
from requests import get
from newsy import takeCommand


engine = pyttsx3.init()
engine.setProperty("rate", 190)
voices = engine.getProperty('voices')


def speak(text):
    engine.say(text)
    engine.runAndWait()

def pogoda():
    URL = 'https://pogoda.interia.pl/prognoza-szczegolowa-konstancin-jeziorna,cId,15287'
    page = get(URL)
    bs = BeautifulSoup(page.content)
    for offer in bs.find_all('div', class_='weather-currently-temp-strict'):
        speak(offer)
        break
    stMsgs = ['to całkiem nieźle, a jeśli chodzi o niebo to już sprawdzam',
            'ale pogoda, a jeśli chodzi o niebo to już sprawdzam',
            'sama nie wiem, a na niebie to już sprawdzam',
            'jak zimno, zaraz sprawdzę jak jest na niebie',
            ', a jeśli chodzi o niebo to już sprawdzam']
    speak(random.choice(stMsgs))

def pogodaKonstancin():
    speak("Gdzie sprawdzić pogodę?")
    gdzie = takeCommand().lower()
    if gdzie == 'w konstancinie':
        URL = 'https://pogoda.interia.pl/prognoza-szczegolowa-konstancin-jeziorna,cId,15287'
        page = get(URL)
        bs = BeautifulSoup(page.content)
        for offer in bs.find_all('div', class_='weather-currently-temp-strict'):
            speak(offer)
            break
        stMsgs = ['to całkiem nieźle, a jeśli chodzi o niebo to już sprawdzam',
                'ale pogoda, a jeśli chodzi o niebo to już sprawdzam',
                'sama nie wiem, a na niebie to już sprawdzam',
                'jak zimno, zaraz sprawdzę jak jest na niebie',
                ', a jeśli chodzi o niebo to już sprawdzam']
        speak(random.choice(stMsgs))

        time.sleep(1)
        speak('Mam')
        for bike in bs.find_all('li', class_='weather-currently-icon-description'):
            speak(bike)
            break
    elif gdzie == 'w osieczku':
            URL = 'https://pogoda.interia.pl/prognoza-szczegolowa-osieczek,cId,2239043'
            page = get(URL)
            bs = BeautifulSoup(page.content)
            for offer in bs.find_all('div', class_='weather-currently-temp-strict'):
                speak(offer)
                break
            stMsgs = ['to całkiem nieźle, a jeśli chodzi o niebo to już sprawdzam',
                    'ale pogoda, a jeśli chodzi o niebo to już sprawdzam',
                    'sama nie wiem, a na niebie to już sprawdzam',
                    'jak zimno, zaraz sprawdzę jak jest na niebie',
                    ', a jeśli chodzi o niebo to już sprawdzam']
            speak(random.choice(stMsgs))

            time.sleep(1)
            speak('Mam')
            for bike in bs.find_all('li', class_='weather-currently-icon-description'):
                speak(bike)
                break
    else:
        speak("Nie rozumie, ale mogę ci podpowiedzieć, że narazie mam tylko dwie opcję, albo w konstancinie albo w osieczku")
        pogodaKonstancin()

