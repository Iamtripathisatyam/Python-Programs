import datetime
from datetime import date
import wikipedia
import smtplib
import webbrowser
import os
import random
dict={"aditya":"usersemailgmail.com","satyam":"useremails@gmail.com"}
def speak(str):
 from win32com.client import Dispatch
 speak=Dispatch("SAPI.SpVoice")
 speak.Speak(str)
def wishme():
    hour=int(datetime.datetime.now().hour)
    if hour>=5 and hour<12:
        print("\n\t\tGood Morning My Dear")
        speak("Good Morning My Dear")
    elif hour>=12 and hour<17:
        print("\n\t\tGood Afternoon My  Dear")
        speak("Good Afternoon my Dear")
    else:
        print("\n\t\tGood Evening My Dear")
        speak("Good Evening my Dear")
    speak("This Assistant is Made by satyam Tripathi and Company")
    speak("I am your Personal assistant please tell me how may i help you")
def gjb(ema):
    a=dict[ema]
    return a

if __name__ == '__main__':
    # wishme()
    conn=smtplib.SMTP("smtp.gmail.com",587)
    conn.ehlo()
    conn.starttls()
    conn.login("youremail@gmail.com","Yourpassword")
    while 1:
     query = input("\nWhat do you want to do : ").lower()
     if query.isnumeric():
         raise Exception("Here Numbers are not Allowed !!")
     elif 'wiki' in query:
        print("Searching...")
        speak("According to wikipedia")
        result=wikipedia.summary(query,sentences=2)
        print(result)
        speak(result)
     elif 'google' in query:
        speak("opening google")
        webbrowser.open("https://www.google.com")
     elif 'youtube' in query:
        speak("Opening Youtube")
        # webbrowser.open("youtube.com")
        webbrowser.open('https://www.youtube.com'
     elif 'time' in query:
        a=datetime.datetime.now().strftime("%H:%M:%S")
        print(f"Time is : {a}")
        speak(f"time is {a}")
     elif 'date' in query:
        today=date.today()
        a = today.strftime('%B %d ,%y')
        print(f"Date is : {a}")
        speak(f"Todays date is {a}")
     elif 'song' in query:
        mus="C:\\Users\\Dell\\Desktop\\Musics & Videos\\Mp3 Musics"
        song=os.listdir(mus)
        os.startfile(os.path.join(mus, song[random.randint(1,247)]))
     elif 'dev' in query:
         url="C:\\Program Files\\Dev-Cpp\\devcpp.exe"
         speak("Opening DEV CPP")
         os.startfile(url)
     elif 'whatsapp' in query:
         path="C:\\Users\\Dell\\AppData\\Local\\WhatsApp\\WhatsApp.exe"
         speak("opening whatsapp")
         os.startfile(path)
     elif 'git' in query:
         speak('opening github')
         url='https://github.com'
         webbrowser.open(url)
     elif 'lin' in query:
         speak('opening linkdin')
         url = 'https://www.linkedin.com'
         webbrowser.open(url)
     elif 'thank' in query:
         speak("Thanks for using me  Good Luck ")
         exit()
     elif 'dhan' in query:
         speak("Aapka bhi dhanyavaad namaste")
         exit()
     elif 'mail' in query:
         send=input("Please enter the Name of the Person : ")
         sub=input("Write a Message : ")
         conn.sendmail("youremail@gmail.com",f"{gjb(send)}",f"Subject : {sub}")
         print("Successfully Sent...")
         conn.quit()


