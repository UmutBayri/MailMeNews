# -*- coding : utf-8 -*- 

import requests
from bs4 import BeautifulSoup

import smtplib as sm
import datetime
from time import sleep
import re

URL_hackernews = "https://news.ycombinator.com/"
URL_reddit = "https://www.reddit.com/r/ArtificialInteligence/"

user_agent = {
    "User-Agent" : "your User-Agent
}

titles_link_list, titles_text_list = [], []

queries_reddit = ["https", "ArtificialInteligence", "comments"]
queries_hackernews = ["https"]

verify = []    

def get_hackernews():
    page = requests.get(URL_hackernews, headers = user_agent)
    page_content = BeautifulSoup(page.content, "html.parser")
    titles = page_content.find_all("a")
    mail = 0
    
    for title in titles :
        if mail < 5 :
            link = title.get("href")
            for query in queries_hackernews :
                t_f = re.search(f"{query}", link)
                verify.append(t_f)
                
            if all(verify) and len(link) > 40 :
                print(f"HackerNews\n{link}\n", file = filew)
                mail +=1
                verify.clear()

            else :
                verify.clear()
        else :
            filew.close()
            break

def get_reddit():
    page = requests.get(URL_reddit, headers = user_agent)
    page_content = BeautifulSoup(page.content, "html.parser")
    titles = page_content.find_all("a")

    for title in titles :
        link = title.get("href")
    
        for query in queries_reddit :
            t_f = re.search(f"{query}", link)
            verify.append(t_f)
         
        if all(verify) :
            print(f"Reddit\n{link}\n",file = filew)
            verify.clear()

        else :
            verify.clear()
            
def send_mail():
    mail_content = filer.read()
    gonderen_kullanici = "x@gmail.com"
    gonderen_sifre = 'x'
    alici_mail= 'x@gmail.com'

    server = sm.SMTP('smtp.gmail.com:587') 
    server.starttls()  
    server.login(gonderen_kullanici , gonderen_sifre) 

    server.sendmail(gonderen_kullanici, alici_mail, mail_content)

    server.close() 

while True :
    now = datetime.datetime.now()
    date = now.strftime("%Y %m %d")
    
    filew = open(f"newss\\{date}.txt", "w")
    get_hackernews()

    filew = open(f"newss\\{date}.txt", "a")   
    get_reddit()
    
    filew.close()

    filer = open(f"newss/{date}.txt")
    send_mail()
    
    sleep(60 * 60 * 24)
