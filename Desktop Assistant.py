import pyttsx3
import speech_recognition as sr
import wikipedia
import datetime
import webbrowser
import os
import smtplib

engine = pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()
def wishme():
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good morning RamCharan,  murali, vamsi , Tanmaya")
    elif hour>=12 and hour<18:
        speak("Good afternoon,RamCharan, murali, vamsi, Tanmaya")
    else:
        speak("Good evening,RamCharan, murali, vamsi, Tanmaya")
    speak("Hey yo, itz meh, your max")
    speak("How can I help you ? What are you looking for?")
def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)

    try:
        print("Recognzing...")
        query=r.recognize_google(audio, language='en-in')
        print(f"Repeating: {query}\n")
    except Exception as e:
        print("Not able to understand...")
        return "None"

    return query
def sendEmail(to,content):
    server=smtplib.SMTP('vvvv@gmail.com')
    server.ehlo()
    server.starttls()
    server.login('xxxx@gmail.com', 'pppp')
    server.sendmail('xxxx@gmail.com',to,content)
    sever.close()
if _name_ == '_main_':
    wishme()
    while True:
        query=takecommand().lower()
        if 'open wikipedia' in query:
            speak("Searching wikipedia...")
            query=query.replace('wikipedia',"")
            results= wikipedia.summary(query,sentences=2)
            speak("According to wikipedia...")
            print(results)
            speak(results)
        elif 'open notepad' in query:
            npath='C:\\Windows\\system32\\notepad.exe'
            os.startfile(npath)
        elif 'open paint' in query:
            npath= "C:\\Windows\\system32\\mspaint.exe"
            os.startfile(npath)
        elif 'open youtube' in query:
            webbrowser.open('youtube.com')
        elif 'open google' in query:
            webbrowser.open('google.com')
        elif 'open spotify' in query:
            webbrowser.open('spotify.com')
        elif 'time' in query:
            strTime= datetime.datetime.now().strftime('%H:%M:%S')
            speak(f'The time is: {strTime}')
        elif 'open linkedin' in query:
            webbrowser.open('www.linkedin.com')
        elif 'emailing' in query:
            try:
                speak('What should I send: ')
                content = takecommand()
                to='dhtanmaya@gmail.com'
                sendEmail(to,content)
                speak("Youe email is sent successfully")
            except Exception as e:
                print(e)
                speak("I am unable to send the email")