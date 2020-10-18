import requests
import json
import time
from plyer import notification
def speak(str):
 from win32com.client import Dispatch
 speak=Dispatch("SAPI.SpVoice")
 speak.Speak(str)
if __name__ == '__main__':
    speak('Hi How are you ')
    speak("This notification system made by satyam tripathi")
    speak('I am your Personal news reader')
    speak('now i am going to start Today News')
    url="https://newsapi.org/v2/top-headlines?sources=the-times-of-india&apiKey=0864a52124954666bb3e1fd0f7fbb1e6"
    a=requests.get(url).text
    b=json.loads(a)
    c=b['articles']
    for article in c:
            notification.notify(title="Today's News Headlines --> @Satyam Tripathi", message=article['title'],
                                  app_icon="C:/Users"
                                         "/Dell/Downloads/news.ico", timeout=5)
            time.sleep(5)
            speak("Next")

    speak("Thank you so much for using me ")
