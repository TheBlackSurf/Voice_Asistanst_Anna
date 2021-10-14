import pyttsx3
from bs4 import BeautifulSoup
from requests import get
import speech_recognition as sr
import pyttsx3
import datetime

 
# class Speaker:
#     engine = pyttsx3.init()
#     engine.setProperty("rate", 190)
#     voices = engine.getProperty('voices')
 
engine = pyttsx3.init()
engine.setProperty("rate", 190)
voices = engine.getProperty('voices')


def speak(text):
    engine.say(text)
    engine.runAndWait()


def wishMe():
    hour = datetime.datetime.now().hour
    if 8 <= hour < 18:
        speak("W czym mogę pomóc?")
    else:
        speak("W czym mogę pomóc?")


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)

        try:
            statement = r.recognize_google(audio, language='pl-pl')
            print(f"Uzytkownik powiedział:{statement}\n")

        except Exception as e:
            # speak("Nie zrozumiałam, powtórz")
            return "None"
        return statement

 
__liczebniki = ["pierwszą", "drugą", "trzecią", "czwartą", "piątą", "szóstą", "siódmą", "ósmą", "dziewiątą", "dziesiątą"]
 
 
def news():
    speak('Ile wiadomości mam ci przeczytać')
    ile = takeCommand().lower()
    if ile == '1':
        URL = 'https://www.wprost.pl/wiadomosci'
        page = get(URL)
        bs = BeautifulSoup(page.content, 'html.parser')
        for number, news_piece in enumerate(bs.find_all('a', class_='news-title')[:1]):
            speak(f"Podaję {__liczebniki[number]} wiadomość.")
            speak(news_piece.text)
    elif ile == '2':
        URL = 'https://www.wprost.pl/wiadomosci'
        page = get(URL)
        bs = BeautifulSoup(page.content, 'html.parser')
        for number, news_piece in enumerate(bs.find_all('a', class_='news-title')[:2]):
            speak(f"Podaję {__liczebniki[number]} wiadomość.")
            speak(news_piece.text)
 
    elif ile == '3':
        URL = 'https://www.wprost.pl/wiadomosci'
        page = get(URL)
        bs = BeautifulSoup(page.content, 'html.parser')
        for number, news_piece in enumerate(bs.find_all('a', class_='news-title')[:3]):
            speak(f"Podaję {__liczebniki[number]} wiadomość.")
            speak(news_piece.text)
 
    elif ile == '4':
        URL = 'https://www.wprost.pl/wiadomosci'
        page = get(URL)
        bs = BeautifulSoup(page.content, 'html.parser')
        for number, news_piece in enumerate(bs.find_all('a', class_='news-title')[:4]):
            speak(f"Podaję {__liczebniki[number]} wiadomość.")
            speak(news_piece.text)
 
    elif ile == '5':
        URL = 'https://www.wprost.pl/wiadomosci'
        page = get(URL)
        bs = BeautifulSoup(page.content, 'html.parser')
        for number, news_piece in enumerate(bs.find_all('a', class_='news-title')[:5]):
            speak(f"Podaję {__liczebniki[number]} wiadomość.")
            speak(news_piece.text)
 
    elif ile == '6':
        URL = 'https://www.wprost.pl/wiadomosci'
        page = get(URL)
        bs = BeautifulSoup(page.content, 'html.parser')
        for number, news_piece in enumerate(bs.find_all('a', class_='news-title')[:6]):
            speak(f"Podaję {__liczebniki[number]} wiadomość.")
            speak(news_piece.text)
 
    elif ile == '7':
        URL = 'https://www.wprost.pl/wiadomosci'
        page = get(URL)
        bs = BeautifulSoup(page.content, 'html.parser')
        for number, news_piece in enumerate(bs.find_all('a', class_='news-title')[:7]):
            speak(f"Podaję {__liczebniki[number]} wiadomość.")
            speak(news_piece.text)
 
    elif ile == '8':
        URL = 'https://www.wprost.pl/wiadomosci'
        page = get(URL)
        bs = BeautifulSoup(page.content, 'html.parser')
        for number, news_piece in enumerate(bs.find_all('a', class_='news-title')[:8]):
            speak(f"Podaję {__liczebniki[number]} wiadomość.")
            speak(news_piece.text)
 
    elif ile == '9':
        URL = 'https://www.wprost.pl/wiadomosci'
        page = get(URL)
        bs = BeautifulSoup(page.content, 'html.parser')
        for number, news_piece in enumerate(bs.find_all('a', class_='news-title')[:9]):
            speak(f"Podaję {__liczebniki[number]} wiadomość.")
            speak(news_piece.text)
 
    elif ile == '10':
        URL = 'https://www.wprost.pl/wiadomosci'
        page = get(URL)
        bs = BeautifulSoup(page.content, 'html.parser')
        for number, news_piece in enumerate(bs.find_all('a', class_='news-title')[:10]):
            speak(f"Podaję {__liczebniki[number]} wiadomość.")
            speak(news_piece.text)
    else:
        speak('Nie wiem co to ma znaczyć, Powiedz ile wiadomości, po prostu od 1 do 10')
        news()
 

# if __name__ == '__main__':
#     news()
 