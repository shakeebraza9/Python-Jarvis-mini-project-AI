
import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import smtplib

engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice',voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishme():
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")
    elif hour>=12 and hour<18:
        speak("Good Afternoon")
    else:
        speak("Good Evening")
    speak("i am shakeeb. Please tell me how may i help you")

def takeCommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in') #Using google for voice recognition.
        print(f"User said: {query}\n")  #User query will be printed.

    except Exception as e:
        # print(e)    
        print("Say that again please...")   #Say that again will be printed in case of improper voice 
        return "None" #None string will be returned
    return query
def sendemail(to,content):
    server=smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('man411210@gmail.com','Bhailog00')
    server.sendmail('man411210@gmail.com',to,content)
    server.close()
if __name__=="__main__":
    wishme()
    while True:
        query=takeCommand().lower()
    # logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('Searching wikipedia...')
            query=query.replace("Wikipedia","")
            results=wikipedia.summary(query,sentences=2)
            speak("According to the Wikipedia")
            print(results)
            speak(results)
        elif 'open youtube' in query:
            webbrowser.open("Youtube.com")
        elif 'open Whatsapp' in query:
            webbrowser.open("web.whatsapp.com")
        elif 'open facebook' in query:
            webbrowser.open("facebook.com")
        elif 'open snapchat' in query:
            webbrowser.open("web.snapchat.com")
        elif 'open stack overflow' in query:
            webbrowser.open("stackoverflow.com")
        elif 'play music' in query:
            music_dir='D:\docoment shakeeb\song'
            songs=os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir,songs[0]))
        elif 'the time' in query:
            strtime=datetime.datetime.now().strftime("%H:%M:%S")
            print(strtime)
            speak(f"sir, The date and time is now  {strtime}")
        elif 'open code' in query:
            codepath="C:\\Users\\AL JOUZ\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codepath)
        elif 'email to harry' in query:
            try:
                speak("What should i say?")
                content=takeCommand()
                to="supermanman0300@gmail.com"
                sendemail(to,content)
                speak("Email has been send")
            except Exception as e:
                print(e)
                speak("Sorry sir dont not understand.....")
        elif 'open messenger' in query:
            meg="C:\\Users\\AL JOUZ\\AppData\\Local\\Programs\\Messenger\\Messenger.exe"
            os.startfile(meg)
        elif 'open harry' in query:
            webbrowser.open("https://www.youtube.com/watch?v=Lp9Ftuq2sVI&t=769s")
        elif 'my love' in query:
            image='D:\\docoment shakeeb\\Images'
            # image='G:\\mobile data\\Snapchat'
            song=os.listdir(image)
            print(song)
            os.startfile(os.path.join(image,song[0]))
            speak("I ,love, u, javeria")
        elif 'quit' in query:
            exit()
            



