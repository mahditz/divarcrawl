import requests
from bs4 import BeautifulSoup
from time import sleep

url = 'https://divar.ir/s/varamin/real-estate'
f = []
while True :
    x = requests.get(url)
    soup = BeautifulSoup(x.content,"html.parser")
    for file in soup.find_all(class_="waf972") :
        if file.find(class_='kt-post-card__title').text.find('فجر')!= -1 or file.find(class_='kt-post-card__title').text.find('بذر')!= -1 or file.find(class_='kt-post-card__title').text.find('ولیعصر')!= -1 :
            if file.find(class_='kt-post-card__title').text not in f :
                xx = requests.get("https://divar.ir"+file.find("a")["href"])
                soup2  = BeautifulSoup(xx.content,"html.parser")
                status = False
                for onefile in soup2.find_all(class_="kt-unexpandable-row__value") :
                    if onefile.text.find('شخصی') != -1 :
                        status = True
                        break
                if status == True :
                    params =  {"username":"mahditz","password":"T0ZWLqyWAGj8qzcRlmASEyr2J5oAgTlccTGdVJZxEpZnBF1hbUXGjk3oJVTZwZyG",
                            "line":"30007732002955"}
                    params["mobile"] = "input your number here"
                    params["text"]  = file.find(class_='kt-post-card__title').text
                    x = requests.get("https://api.sms.ir/v1/send",params=params)
                    params["mobile"] = "input your number here"
                    x = requests.get("https://api.sms.ir/v1/send",params=params)
                    f.append(file.find(class_='kt-post-card__title').text)
    if len(f) == 25 :
        del f[-10:]
    sleep(900)  
        

        

