from win32com.client import Dispatch
import datetime
import speech_recognition as sr
import smtplib
import wikipedia
import webbrowser
import os
import random



#FOR voice this is made
def speak(audio):
    speak=Dispatch('SAPI.Spvoice')
    speak.speak(audio)

#for greetings this is made
def sendmail(to,contnt):
    server = smtplib.SMPT('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('mail','pass')#i have to pass real mail and pass to this to get it work
    server.sendmail('mail',to,content)
    server.close()
    
def greet():
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good morning sir")
    
    elif hour>=12 and hour<16:
        speak("Good afternoon Sir")
    
    else:
        speak("Good evening sir")
    
    speak("I am jarvis how may i help you sir")

#To carry out tasks tk command is made to hear
def tk_cmd():
    
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("\nListening .....")
        #To capture pause while speaking r.pause_threshold() is used
        r.pause_threshold = 1
        audio=r.listen(source)
    
    #To handle any kind of mess like exception try is being used like not heard
    
    try:
        print("\nRecognizing.....")
        #recognize_google() is used for search engine
        query=r.recognize_google(audio, language="en-IN")
        print(query,"\n")
        
    except Exception as e:
        
        
        speak("Please repeat again sir")
        return "none"
    return query
        
        


if __name__=='__main__':
    greet()
    query=tk_cmd().lower()
    if ' in wikipedia' in query:
        speak("Searching sir")
        query=query.replace("in wikipedia"," ")
        results=wikipedia.summary(query,sentences=3)
        speak("According to wikipedia")
        speak(results)
        
    elif 'open youtube' in query:
        webbrowser.open('youtube.com')
    elif 'open google' in query:
        webbrowser.open('google.com')
    
    elif 'play music' in query:
        music_dir=' ' 
        songs=os.listdir(music_dir)
        os.startfile(os.path.join(music_dir,random.choice(songs)))
        x=sr.Recognizer()
        with sr.Microphone() as source:
            print("Please tell when to stop")
            adio=x.listen(source)
            stopper=x.recognize_google(adio, language="en-IN")
            if 'stop music' in stopper:
                os.system('TASKKILL /F /IM ') #after im you have to give
                #player extension which you can check by open and close syntax file
                
    elif 'time' in query:
        stime=datetime.datetime.now().strftime("%H:%M:%S")
        speak(f"Sir the time is {stime}")
    
    elif 'send mail' in query:
        try:
            speak("The whom you want to send sir")
            to=tk_cmd()
            speak("ok sir now what should be there in it")
            content=tk_cmd()
            sendmail(to,content)
            speak("Successfully sent ")
        
        except Exception as e:
            print(e)
            speak("Sorry sir failed to send")    
