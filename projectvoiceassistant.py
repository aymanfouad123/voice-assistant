import pyttsx3
import datetime
import speech_recognition as sprec
import webbrowser
import os


engine = pyttsx3.init("sapi5")
voices = engine.getProperty('voices')



def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def welcome():
    time_hour = int(datetime.datetime.now().hour)

    if time_hour >= 0 and time_hour <= 12:
        speak("Good Morning Sir") 
    elif time_hour >= 12 and time_hour <= 17:
        speak("Good Afternoon Sir")
    else:
        speak("Good Evening Sir")

    speak("How may i help you today sir?")

def recieveOrder():
    r = sprec.Recognizer()
    with sprec.Microphone() as source:
        print("I am listening...") 
        r.pause_threshold = 1.2
        stranscript = r.listen(source)
    
    try:
        print("Recognizing...")
        query = r.recognize_google(stranscript , language='en')
        print('You said - ',query)
    except LookupError:                     
        print("I could'nt understand you sir. Say that again please")
        return "None"
    return query

if __name__ == '__main__':
    welcome()

    while True:
        order = recieveOrder().lower()
        '''
        if 'wikipedia' in order:
            speak('Searching...')
            order.replace("wikipedia","")
            results = wikipedia.summary(order , sentences = 3)
            print(results)
            speak("According to Wikipedia")
            speak(results)
        '''
        if 'open youtube' in order:
            webbrowser.open("youtube.com")

        elif 'open google' in order:
            webbrowser.open("google.com")
        
        elif 'open instagram' in order:
            webbrowser.open("instagram.com")
        
        elif 'open facebook' in order:
            webbrowser.open("facebook.com")

        elif 'open gmail' in order:
            webbrowser.open("gmail.com")
        
        elif 'what is the time' in order:
            timenow = datetime.datetime.now().strftime("%H :%M :%S")
            print(timenow)
            speak("The time is")
            speak(str(timenow))
        elif 'quit' in order:
            print("Quitting...")
            speak('Have a great day sir')
            break
        '''
        elif 'send email' in order:
            speak('Whats the message?')
            content = recieveOrder()
            to = "randommail@gmail.com" 
            sendEmail(to,content)
            print('Email sent successfully ')
            speak("The email is sent")
        '''