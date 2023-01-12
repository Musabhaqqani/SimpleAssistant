import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia as w
import pywhatkit
import webbrowser
import os
import pyjokes
import time

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def speak(audio):
    rate = engine.getProperty('rate')
    engine.setProperty('rate', rate)
    engine.say(audio)
    engine.runAndWait()


def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour > 0 and hour < 12:
        speak("Good morning!")
    elif hour >= 12 and hour < 18:
        speak("Good afternoon!")
    else:
        speak("Good evening!")


def takeCommand():
    # taking voice command and returning string...
        listener = sr.Recognizer()
        # with sr.Microphone() as source:
        #     r.pause_threshold=1
        #     audio=r.listen(source)

        try:
            with sr.Microphone() as source:
                print("Im listening .....\n\n***********************")
                voice = listener.listen(source)
            # print("Recognizing...")
            query = listener.recognize_google(voice, language='en-in')
            print(f"*************************\n\nducky..did u say.... {query}?\n")

        except:
            speak("I'm sorry i did not catch that...")
            print("\n\nI'm sorry i did not catch that...")
            return "None"
            # pass
        return query


if __name__ == "__main__":
    # speak("hyoo duckyy!")
    wishme()
    speak("......I am your customized assistant..You may call me Lexi.... my mission is to serve you till the day i draw my last input...")
    speak("How can i help you?")

    while True:
        query = takeCommand().lower()
        if query==0:
            continue

        if 'thank you' in query or 'sleep' in query:
                    speak("...I understand........it was a pleasure serving you.....Goodbye")
                    print("\n\nI understand..it was a pleasure serving you.....Goodbye\n\n")
                    break

        # if 'wikipedia' or "search" or 'who is' or 'what is' in query:
        if 'wikipedia' in query:
                    query = query.replace("wikipedia", "")
                    speak("browsing...")
                    results = w.summary(query, sentences=2)
                    speak("According to my search,")
                    print(results)
                    speak(results)
        elif 'search' in query:
                    query = query.replace("search", "")
                    speak("browsing...")
                    results = w.summary(query, sentences=2)
                    speak("According to my search,")
                    print(results)
                    speak(results)
        elif 'what is' in query:
                    query = query.replace("what is", "")
                    speak("browsing...")
                    results = w.summary(query, sentences=2)
                    speak("According to my search,")
                    print(results)
                    speak(results)
        elif 'who is' in query:
                    query = query.replace("who is", "")
                    speak("browsing...")
                    results = w.summary(query, sentences=2)
                    speak("According to my search,")
                    print(results)
                    speak(results)

        elif 'open youtube' in query:
                    bravedir="C:/Program Files/BraveSoftware/Brave-Browser/Application/brave.exe %s"
                    webbrowser.get(bravedir).open('youtube.com')
                    speak('Opening youtube')
                    time.sleep(5)
        elif 'open google' in query:
                    bravedir="C:/Program Files/BraveSoftware/Brave-Browser/Application/brave.exe %s"
                    webbrowser.get(bravedir).open('google.com')
                    speak('Opening google')
                    time.sleep(5)
        elif 'open gmail' in query:
                    bravedir="C:/Program Files/BraveSoftware/Brave-Browser/Application/brave.exe %s"
                    webbrowser.get(bravedir).open('gmail.com')
                    speak('Opening gmail')
                    time.sleep(5)
        elif 'open anime' in query:
                    bravedir="C:/Program Files/BraveSoftware/Brave-Browser/Application/brave.exe %s"
                    webbrowser.get(bravedir).open('9anime.gs')
                    speak('Opening the anime homepage')
                    time.sleep(5)
        elif 'play songs from laptop' in query:
                    mus_dir='Music'
                    songs=os.listdir(mus_dir)
                    print(songs)
                    os.startfile(os.path.join(mus_dir,songs[0]))
                    time.sleep(5)
        elif 'play' in query:
                    song=query.replace('play','')
                    speak('Now playing '+song)
                    pywhatkit.playonyt(song)
                    time.sleep(5)
        elif 'the time' in query:
                    strTime=datetime.datetime.now().strftime("%H:%M:%S")
                    speak("the time is "+strTime)
                    print("The time is "+strTime)
        elif 'funny' in query:
                    str=pyjokes.get_joke()
                    speak(str)
                    print("\n"+str+"\n")
        elif 'who are you' in query:
                    speak('Im your personel assistant')
                    speak('lexi')
        elif 'how are you' in query:
                    speak('Im doing great')
                    speak('what about you?')
        
        