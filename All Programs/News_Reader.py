import requests
import json
def speak(str):
 from win32com.client import Dispatch
 speak=Dispatch("SAPI.SpVoice")
 speak.Speak(str)
if __name__ == '__main__':
    speak("Today News")
    url="https://newsapi.org/v2/top-headlines?sources=bbc-news&apiKey=0864a52124954666bb3e1fd0f7fbb1e6"
    a=requests.get(url).text
    b=json.loads(a)
    c=b['articles']
    for article in c:
        print(article['title'])
        speak(article['title'])
        speak("Next")

    speak("Thank you Satyam Tripathi")
