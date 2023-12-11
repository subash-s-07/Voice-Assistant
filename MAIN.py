from tkinter import *
from PIL import ImageTk,Image
import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
import smtplib
import webbrowser
import os
def main():
    print("Say Something .... ")
    listener = sr.Recognizer()
    engine=pyttsx3.init()
    voices=engine.getProperty('voices')
    engine.setProperty('voice',voices[1].id)
    def talk(text):
        engine.say(text)
        engine.runAndWait()
    def take_command():
        try:
            with sr.Microphone() as source:
                print('Listening.......')
                talk("LISTENING........")
                voice=listener.listen(source)
                command=listener.recognize_google(voice)
                command=command.lower()
                if 'alexa' in command:
                    command=command.replace('alexa','')
                    print(command)
        except:
            pass
        return command
    def sendEmail(to, content):
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.ehlo()
        server.starttls()
        server.login('21pd36@psgtech.ac.in', '*******')
        server.sendmail('21pd36@psgtech.ac.in', to, content)
        server.close()
    def run_alexa():
        command = take_command()
        print(command)
        if 'play' in command:
            song= command.replace('play','')
            talk('playing'+song)
            pywhatkit.playonyt(song)
        elif 'time' in command:
            time =datetime.datetime.now().strftime('%I:%M %p')
            print (time)
            talk('Current time is '+time)
        elif 'search' in command:
            search = command.replace("search",'')
            info = wikipedia.summary(search,1)
            print(info)
            talk(info)
        elif 'joke' in command:
            joke=pyjokes.get_joke()
            print(joke)
            talk(joke)
        elif 'send a mail' in command:
                try:
                    talk("What should I say?")
                    content = take_command()
                    talk("whome should i send")
                    to = input()  
                    sendEmail(to, content)
                    talk("Email has been sent !")
                except Exception as e:
                    print(e)
                    talk("I am not able to send this email")
        elif 'how are you' in command:
            talk("I am fine, Thank you")
            talk("How are you, Sir")
            take_command()
           
     
        elif 'fine' in command or "good" in command:
            talk("It's good to know that your fine")
     
        elif "change my name to" in command:
            command = command.replace("change my name to", "")
            assname = command
     
        elif "change name" in command:
                talk("What would you like to call me, Sir ")
                assname = take_command()
                talk("Thanks for naming me")
     
        elif "what's your name" in command or "What is your name" in command:
                talk("My friends call me")
                talk("SREE")
                #print("My friends call me", assname)
     
        elif 'exit' in command:
                talk("Thanks for giving me your time")
                exit()
     
        elif "who made you" in command or "who created you" in command:
                talk("I have been created by SREE.")
        elif 'open youtube' in command:
                talk("Here you go to Youtube\n")
                webbrowser.open("youtube.com")
     
        elif 'open google' in command:
                talk("Here you go to Google\n")
                webbrowser.open("google.com")
        elif 'word' in command:
                os.startfile("winword")
        elif 'powerpoint' in command:
                os.startfile("powerpnt")
        elif 'excel' in command:
                os.startfile("excel")
        elif 'notepad' in command:
                 os.startfile("notepad")
        elif 'paint' in command:
                 os.startfile("paint")
        """"elif 'text' or 'message' in command:
            number=input("ENTER MOBILE NUMBER")
            message=input("ENTER THE MESSAGE")
            datetime.datetime.now()
            pywhatkit.sendwhatmsg(number, message ,datetime.datetime.hour() ,datetime.datetime.minute())"""
       
    run_alexa()
s=Tk()
s.title("")
s.geometry("520x320")

"""i=ImageTk.PhotoImage(Image.open("MIC1.gif"))
p=Label(s,image=i)
p.pack(side='right',fill='both',expand='no')"""

utext=StringVar()
utext.set("Your Voice Assisstant")
uframe=LabelFrame(s,text="SREE",font=('Railways',24,'bold'))
uframe.pack(fill='both',expand='yes')

r=Message(uframe,textvariable=utext,bg='light blue',fg='black')
r.config(font=("Century Gothic",30,'bold'))
r.pack(side='top',fill='both',expand='yes')

b=Button(s,text='Run',font=('railways',18,'bold'),bg='red',fg='black',command=main).pack(fill='x',expand='no')
b2=Button(s,text='Close',font=('railways',18,'bold'),bg='yellow',fg='black',command=s.destroy).pack(fill='x',expand='no')
s.mainloop()