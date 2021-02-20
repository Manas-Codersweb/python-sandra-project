import pyttsx3 #pip install pyttsx3
import speech_recognition as sr #pip install speechRecognition
import datetime #pip install datetime
import wikipedia #pip install wikipedia
import webbrowser #pip install webbrowser
import os #pip install os
import smtplib #pip install stmplib

#setting the voice of sandra
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
print(voices[1].id)
engine.setProperty('voice', voices[1].id) #voices[1].id is for female voices

def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    speak("Hi Manas, Sandr ahere...How can I help you?")

    hour = int(datetime.datetime.now().hour)
    if hour>=22 and hour<4:
        speak("Good Night!")

    elif hour>=4 and hour<10:
        speak("Good Morning!")   

    elif hour>=10 and hour<12:
        speak("Good Day!")

    elif hour>=12 and hour<16:
        speak("Good Afternoon!")

    else:
        speak("Good evening!")

def takeCommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        speak("Listening...")
        r.pause_threshold = 2
        audio = r.listen(source)

    try:
        print("Recognizing...")  
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)    
        print("Say that again please...")
        speak("Say that again please...")
        return "None"
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('manas.sarwade09@gmail.com', '')
    server.sendmail('adisarwade7@gmail.com', to, content)
    server.close()

if __name__ == "__main__":
    wishMe()
    while True:
    # if 1:
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

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")   

        elif 'typing practise' in query:
            webbrowser.open("https://www.typing.com/student/lesson/361/d-e-and-i-keys")

        elif 'open my site' in query:
            webbrowser.open("manassarwade.epizy.com")

        elif 'open harry' or 'harrybhai!' in query:
            webbrowser.open("codewithharry.com")

        elif 'Host a domain' in query:
            webbrowser.open("freenom.com")

        elif 'Host a site' in query:
            webbrowser.open("infinityfree.net")

        elif 'mail' in query:
            webbrowser.open("mail.google.com")

        elif 'Twitter' in query:
            webbrowser.open("twitter.com")

        elif 'Facebook' in query:
            webbrowser.open("facebook.com")

        elif 'Instagram' in query:
            webbrowser.open("instagram.com")

        elif 'my blog' in query:
            webbrowser.open("violinistmanassarwade.blogspot.com")

        elif 'messages in instagram' in query:
            webbrowser.open("instagram.com/direct/inbox/")

        elif 'whatsapp' in query:
            webbrowser.open("web.whatsapp.com")

        elif 'how are you' in query:
            speak("I'm fine! what should I do?")
            print("captain:")
            print("I'm fine! what should I do?")

        elif 'play music' in query:
            music_dir = 'D:\\Non Critical\\songs\\Favorite Songs2'
            songs = os.listdir(music_dir)
            print(songs)    
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Manas, the time is {strTime}")

        elif 'open sublime text' in query:
            codePath = "C:\\Sublime Text 3\\sublime_text.exe"
            os.startfile(codePath)

        elif 'open powerpoint' in query:
            codePath1 = "C:\\Users\\Lenovo\\3D Objects\\Apps\\Office new\\PowerPoint.Ink"
            os.startfile(codePath1)

        elif 'open word' in query:
            codePath2 = "C:\\Users\\Lenovo\\3D Objects\\Apps\\Office new\\Word.Ink"
            os.startfile(codePath2)

        elif 'open excel' in query:
            codePath3 = "C:\\Users\\Lenovo\\3D Objects\\Apps\\Office new\\Excel.Ink"
            os.startfile(codePath3)

        elif 'exit' or 'quit' in query:
            speak("Thanks for using me, Manas... Have a great Day")
            print("Sandra:")
            print("Thanks for using me, Manas... Have a great Day")
            exit()