import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os

engine = pyttsx3.init('sapi5')
voices = engine.getproperty('voice')

engine.setproperty('voice', voices[1].id)

def speak(audio):
    engine.Say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)

if hour>=0 and hour<12:
    speak("Good morning smartboy")
elif hour>=12 and hour<4:
    speak("Good Afternoon smartboy")
else:
    speak("Good evening smartboy")
    
speak("I am your Assistant")

def takecommand():
    # takes my command from microphone and gives text
    r = sr.recognizer
    with sr.microphone() as source:
        print("listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("recognizing...")
        query = r.recognize_google(audio, language ="en-in")
        print("user said : ", query)
    except Exception as e:
        print("e")
        speak("sorry smartboy can you repeat that again?")
        return "None"
    return query

if __name__ == "__main__":
    wishMe()
    while True:
        speak("How can i help you?")
        query = takecommand().lower()
        if 'wikipedia' in query:
            speak("searching in wikipedia")
            query = query.replace("wikipedia", "")
            result = wikipedia.summary(query, sentences = 2)
            speak("According to wikipedia")
            print(results)
            speak(results)

elif 'open youtube' in query:
    webbrowser.open("youtube.com")
    speak("youtube is opened")
elif 'open google' in query:
    webbrowser.open("google.com")
    speak("google is opened")
elif 'open gmail' in query:
    webbrowser.open("gmail.com")
    speak("gmail is opened")
elif 'open play music' in query:
    music_dir = 'D:\\music'
    songs = os.listdir(music_dir)
    print(songs)
    os.startfile(os.path.join(music_dir, songs[0]))
    speak("music is being played")
elif 'time' in query:
    strtime = datetime.datetime.now().strftime("%H:%M:%S")
    speak(f"The time is (strftime)")
elif 'stop' in query:
    speak("see you soon smartboy")
    exit()  
