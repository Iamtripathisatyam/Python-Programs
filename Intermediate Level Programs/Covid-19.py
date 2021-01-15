from plyer import notification
import requests
import json
import time
if __name__ == '__main__':
    r=requests.get('https://coronavirus-19-api.herokuapp.com/countries').text
    data=json.loads(r)
    x=data[0]['cases']
    y=data[0]['deaths']
    z=data[0]['recovered']
    a=data[3]['cases']
    b=data[3]['todayCases']
    c=data[3]['deaths']
    d=data[3]['todayDeaths']
    e=data[3]['recovered']
    if 1:
       notification.notify(title="  Covid-19 Updates ------->>>> Made by : @Satyam Tripathi ",message=f"\t   WORLD "
       f"\nConfirmed Cases ----> {x}\nDeaths ----> {y}\nRecovered ----> {z}\n\n\t    INDIA\nConfirmed Cases ----> "
       f" {a}\nTotal Deaths ----> {c}\nTotal Recovered ----> {e}\nToday Cases ----> {b}\nToday Deaths ----> {d}"
                           ,app_icon="C:/Users/Dell/Downloads/vir.ico",  timeout=10)


       time.sleep(1800)
