import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import random
import smtplib

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices[0].id)
engine.setProperty('voice',voices[0].id)
def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour= int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
         speak("good morning!")

    elif hour>=12 and hour<18:
        speak("good afternoon!")
    else:
        speak("good evening!")

    speak("I am Jarvis. How may I help you")
def takeCommand():
    #it takes microphone input from user and return string output
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio,language='en-in')
        print(f"User said:{query}\n")
    
    except Exception as e:
        #print(e)
        print("Say it again please...")
        return "None"
    return query
def sendEmail(to,content):
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('youremail.gmail.com','your.password-here') 
    server.sendmail('yourmail.gmail.com',to,content)
    server.close()   


if __name__ == "__main__":
    #speak("hi priya")
    wishMe()
    #if 1:
    while True:
        query=takeCommand().lower()
        #Logic for executing tasks based on query
        if 'wikipedia' in query:
            speak("Searching Wikipedia...")
            query = query.replace("wikipedia","")
            results = wikipedia.summary(query,sentences=2)
            speak("According to wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
        elif 'open google' in query:
            webbrowser.open("google.com")
        elif 'open github' in query:
            webbrowser.open("github.com")
        elif 'play music' in query:
            music_dir='C:\\Users\\Dell\\Music\\fav'
            songs = os.listdir(music_dir)
            os.startfile(os.path.join(music_dir,songs[random.randint(0,7)]))

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"the time is:{strTime}")
        elif 'open code' in query:
            codePath= "C:\\Users\\Dell\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)
        elif 'quit jarvis' in query:
            speak("exit terminal")
            quit()
        #elif 'email to priya' in query:
            #use dictionary for it
            #try:
                #speak("what should i say?")
                #content=takeCommand()
                #to="email@gmail.com"#enable less secure apps for this
                #sendEmail(to,content)#features at its cost.
                #speak("Email has been sent!")
            #except Exception as e:
                #print(e)
                #speak("Email not sent!")
        

        



            



        
             

        


