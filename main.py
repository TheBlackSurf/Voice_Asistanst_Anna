import random
import winsound
import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser
import os
import time
import pyautogui
import pogoda
import newsy
import psutil


engine = pyttsx3.init()
engine.setProperty("rate", 170)
voices = engine.getProperty('voices')


def speak(text):
    engine.say(text)
    engine.runAndWait()


def wishMe():
    hour = datetime.datetime.now().hour
    if 8 <= hour < 18:
        speak("Jestem Anna, W czym mogę pomóc?")
    else:
        speak("Jestem Anna, W czym mogę pomóc?")
    

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
def cont():
    pass

def alarm():
    speak("Pamiętaj żeby mówić osiemnaście a nie osiemnasta")
    speak("Podaj godzinę")
    hour = takeCommand().lower()
    speak("Podaj minutę")
    minute = takeCommand().lower()
    now = datetime.datetime.now()
    alarm_time = datetime.datetime.combine(now.date(), datetime.time(int(hour), int(minute), 0))
    time.sleep((alarm_time - now).total_seconds())
    speak('Pora wstawać')
    def dzwonek():
        speak('Wstawaj!')
        winsound.PlaySound('alarm.wav', winsound.SND_FILENAME)
        speak('Powiedz już wstaję żeby wyłączyć budzik')
        wstane = takeCommand().lower()
        if 'już wstaję' in wstane:
            cont()
        else:
            winsound.PlaySound('alarm.wav', winsound.SND_FILENAME)
            dzwonek()

    dzwonek()
    
    


# speak("Asystent głosowy kalmus-boks 2048 ")
speak("Proszę czekać, ładuje systemy")
# speak("3")
# speak("2")
# speak("1")
winsound.PlaySound('start.wav', winsound.SND_FILENAME)
wishMe()

if __name__ == '__main__':
    while True:
        # speak("Jak ci moge pomóc?")
        statement = takeCommand().lower()
        if statement == 0:
            continue



        if "wyłącz się" in statement or "wyjdź" in statement or "koniec" in statement or "do widzenia" in statement \
            or 'wyłącz system' in statement:
            stMsgs = ['Okej, to pa', 'Trzymaj się, do usłyszenia!', 'Wyłączam się','Jestem pełna energii, no cóż. Do widzenia']
            speak(random.choice(stMsgs))
            winsound.PlaySound('Shut-down-sound-effect.wav', winsound.SND_FILENAME)
            break
        

#######*****ROZMOWA*****############
        if 'kocham cię' in statement:
            speak('To strasznie niezręczna sytuacja')

        if "co potrafisz" in statement or "potrzebuje pomocy" in statement:
            speak(
                'Mogę puścić muzykę, włączyć przeglądarkę zrobić screenshota, sprawdzić pogodę a nawet mogę opowiedzieć ci jakiś żart. Aby poznać wszyskie komendy zapytaj i wszystkie komendy')
        if 'opowiedz żart' in statement:
            speak('''
            Rozmawia dwóch kolegów:
            Żona nie mogła wybrać gdzie pojedziemy na wakacje po pandemii. Dałem jej mapę i lotkę i powiedziałem, że wakacje spędzi tam gdzie trafi.
            - I dokąd jedziecie?
            - Nie wiem gdzie ja pojadę - ale żona spędzi dwa tygodnie za lodówką. 
            ''')
        if "co słychać" in statement or 'co u ciebie' in statement or 'co tam' in statement:
            stMsgs = ['Wszystko dobrze', 'Jakoś Leci', 'Super!', 'Jestem pełna energii']
            speak(random.choice(stMsgs))


        if "anna" in statement or "hej anna" in statement or "jesteś tam anna" in statement or "jesteś" in statement:
            stMsgs = ['Jestem', 'No co tam?', 'w czym pomóc?']
            speak(random.choice(stMsgs))

        if "ile masz lat" in statement or "jaki twój wiek" in statement:
            speak('Jestem robotem stworzonym 12 października 2021.')

        if "kto cię stworzył" in statement or "kto jest twoim właścicielem" in statement:
            speak('Stworzył mnie Grzegorz władca piekieł!')
            print('koniec')


        if "dzięki" in statement or "dziękuję" in statement:
            stMsgs = ['Nie ma za co', 'No taka moja rola', 'Luzik', 'Jestem pełna energii, to żaden problem']
            speak(random.choice(stMsgs))

        if "kim jesteś" in statement or "jak masz na imię" in statement or "masz na imię" in statement:
            speak('Nie mam jeszcze imienia, więc możesz mi mówić Pani robotowa albo mister doktor')
            print('koniec')

#######*****INTERNET*****############

        elif 'otwórz github' in statement or "github" in statement:
            speak('Czego szukamy????')
            search = takeCommand().lower()
            speak('Okej, to szukam')
            webbrowser.open_new_tab('https://github.com/search?q=' + search)
            # time.sleep(5)

        elif 'otwórz facebook' in statement or "facebook" in statement:
            webbrowser.open_new_tab("https://www.facebook.com")
            speak("Otwieram facebooka")
            # time.sleep(5)
        

        elif 'otwórz google' in statement or "google" in statement:
            speak('Czego szukamy????')
            search = takeCommand().lower()
            speak('Okej, szukam')
            webbrowser.open_new_tab('https://www.google.com/search?q=' + search)


        elif 'otwórz gmail' in statement or "gmail" in statement:
            webbrowser.open_new_tab("gmail.com")
            speak("Otwieram gmail")
            # time.sleep(5)

        elif 'wyszukaj' in statement:
            statement = statement.replace("wyszukaj", "")
            webbrowser.open_new_tab(f"https://www.google.com/search?client=firefox-b-d&q={statement}")
            # time.sleep(5)

        elif 'co na ból głowy' in statement:
            speak('Zaparz sobię ciepłej herbatki i pod kocyk')

        elif 'jaka jest pogoda' in statement or 'sprawdź pogodę' in statement or 'pogoda' in statement or 'jak za oknem' in statement or 'sprawdzisz pogodę' in statement:
            pogoda.pogodaKonstancin()

        elif "słuchamy muzyki" in statement or "muzyka" in statement or "słuchamy czegoś" in statement or "puść coś" in statement or "puść muzykę" in statement or "włącz youtube" in statement:

            
            speak("Jasne, co dziś słuchamy?")
            searchyt = takeCommand().lower()
            speak("Dobra, odpalam")
            webbrowser.open(f"https://www.youtube.com/search?q={searchyt}")
            time.sleep(12)  
            pyautogui.keyDown('tab')
            pyautogui.keyDown('enter')


        elif 'zadzwoń do kamili' in statement or 'zadzwoń do kamy' in statement:
            speak('Jasne już dzwonimy')
            webbrowser.open(f"https://www.facebook.com/groupcall/ROOM:3215902341794669/?call_id=1602279847&users_to_ring[0]=100001531856448&has_video=false&initialize_video=false&nonce=9se211hbx3qy&thread_type=1")
            time.sleep(15)
            pyautogui.keyDown('tab')
            pyautogui.keyDown('enter')

        elif "puść playlistę" in statement or "playlista" in statement or "playliste" in statement: 
            speak("Jasne, co mam włączyć?")
            searchyt = takeCommand().lower()
            speak("Dobra, odpalam")
            webbrowser.open(f"https://www.youtube.com/search?q={searchyt}+playlista")
            time.sleep(12)
            pyautogui.keyDown('tab')
            pyautogui.keyDown('enter')


        elif "wiadomości" in statement or "newsy" in statement:
            newsy.news()

#######*****INNE*****############

        elif 'bateria' in statement:
            battery = psutil.sensors_battery()
            speak("Poziom bateri wynosi " + str(battery.percent) + " procent")
            
        elif 'procesor' in statement:
            usage = str(psutil.cpu_percent())
            speak('Zużycie procesora wynosi ' + usage + ' procent')
            print('CPU usage is at ' + usage)         

        elif 'zapamiętasz coś' in statement:
            speak('Co takiego???')
            memory = takeCommand()
            speak("Zapamiętałam" + memory)
            remember = open('memory.txt', 'w')
            remember.write(memory)
            remember.close()


        elif 'masz coś w pamięci' in statement or "pamiętasz o czymś" in statement:
            remember = open('memory.txt', 'r')
            speak("Już ci mówię co to było" + str(remember.read()))

#######*****KOMENDY WINDOWS*****############

        elif 'ustaw alarm' in statement:
            # speak("Potrzebuje informację o godzinie")
            # speak("Podaj godzinę")
            # hour = takeCommand().lower()
            # speak("Podaj minutę")
            # minute = takeCommand().lower()
            # now = datetime.datetime.now()
            # alarm_time = datetime.datetime.combine(now.date(), datetime.time(int(hour), int(minute), 0))
            # time.sleep((alarm_time - now).total_seconds())
            # speak('Pora wstawać')
            while True:
                try:
                    alarm()
                    break
                except:
                    speak('Coś poszło nie tak, spróbuj ponownie później')
                    break
            
        elif "przewiń do góry" in statement or "do góry" in statement:
            pyautogui.scroll(2000)

        elif "przewiń do dołu" in statement or "do dołu" in statement:
            pyautogui.scroll(-2000)


        elif "zrób screenshota" in statement or "zrobisz zrzut ekranu" in statement:
            speak("Jasne, jak nazwać plik")
            name = takeCommand().lower()
            speak("Czekaj, robię screenshota")
            time.sleep(2)
            img = pyautogui.screenshot()
            img.save(f"{name}.jpg")
            speak("Skończyłam, zrzut ekranu został zapisany w naszym głównym folderze")

        elif 'zamknij przeglądarkę' in statement or "zamknij to" in statement  or "zamknij karty" in statement or "wyłącz przeglądarkę" in statement or 'stop' in statement:
            os.system("taskkill /im firefox.exe /f")
            os.system("taskkill /im chrome.exe /f")
            os.system("taskkill /im edge.exe /f")
            speak("Zamykam okna przeglądania")
            # time.sleep(5)

        elif 'przycisz' in statement:
            speak('Przyciszam o 10')
            pyautogui.hotkey('volumedown')
            pyautogui.hotkey('volumedown')
            pyautogui.hotkey('volumedown')
            pyautogui.hotkey('volumedown')
            pyautogui.hotkey('volumedown')

        elif 'przygłoś' in statement:
            speak('Przygłaszam o 10')
            pyautogui.hotkey('volumeup')
            pyautogui.hotkey('volumeup')
            pyautogui.hotkey('volumeup')
            pyautogui.hotkey('volumeup')
            pyautogui.hotkey('volumeup')

        elif 'ktora jest godzina' in statement or "godzina" in statement:
            strTime = datetime.datetime.now().strftime("%H:%M")
            speak(f"Jest godzina {strTime}")

        elif 'jaki dziś dzień' in statement or 'co dziś mamy' \
             in statement or 'co dziś' in statement:
            today = datetime.date.today()
            speak(today)
        

        elif "wszystkie komendy" in statement or "komendy" in statement:
            speak("""
zadzwoń do kamili
wiadomości
wyłącz się
ustaw alarm
zrób screenshota
co słychać
anna
przewiń do góry
przewiń do dołu
otwórz github
otwórz facebook
zamknij przeglądarkę
otwórz google
otwórz gmail
ktora jest godzina
wyszukaj
zapamiętasz coś
masz coś w pamięci
jaka jest pogoda
słuchamy czegoś
puść playlistę
                """)



#######*****BETA TESTY*****##########

        # elif 'hide window' in statement or 'hide work' in statement or 'change window' in statement or 'minimise window' in statement:
        #     speak(random.choice(responses))
        #     Minimize = win32gui.GetForegroundWindow()
        #     win32gui.ShowWindow(Minimize, win32con.SW_MINIMIZE)

