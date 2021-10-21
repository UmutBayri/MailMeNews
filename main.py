import requests
from bs4 import BeautifulSoup

import smtplib as sm
import datetime

now = datetime.datetime.now()
date = now.strftime("%Y %m %d")
print()
filew = open(f"news\\abc.txt", "w")

URL = "https://news.ycombinator.com/newest"
user_agent = {
    "User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64)\
 AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36"
}

page = requests.get(URL, headers = user_agent)
page_content = BeautifulSoup(page.text, "html.parser")
titles = page_content.find_all(rel = "nofollow", limit = 4)

for title in titles:
    template = f"""\
    TITLE : {title.get_text()}
    LINK : {title.get("href")}
    """

    print(template, file = filew)

filew.close()
filer = open(f"news/{date}")

gonderen_kullanici = "MailAdresin@gmail.com"
gonderen_sifre = 'Sifren'
alici_mail= 'Alici@gmail.com'

server = sm.SMTP('smtp.gmail.com:587') 
server.starttls()  
server.login(gonderen_kullanici , gonderen_sifre) 

server.sendmail(gonderen_kullanici, alici_mail, )
server.close() 
