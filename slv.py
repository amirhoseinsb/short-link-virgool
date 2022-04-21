from bs4 import BeautifulSoup
import requests


def banner():
    print(
        """

 ____  _                _     _ _       _            _                       _ 
/ ___|| |__   ___  _ __| |_  | (_)_ __ | | __ __   _(_)_ __ __ _  ___   ___ | |
\___ \| '_ \ / _ \| '__| __| | | | '_ \| |/ / \ \ / / | '__/ _` |/ _ \ / _ \| |
 ___) | | | | (_) | |  | |_  | | | | | |   <   \ V /| | | | (_| | (_) | (_) | |
|____/|_| |_|\___/|_|   \__| |_|_|_| |_|_|\_\   \_/ |_|_|  \__, |\___/ \___/|_|
                                                           |___/               

Created By : Amirhoseinsohrabi
------------------------------
Gmail : amirhoseinsohrabi.official@gmail.com
--------------------------------------------

1 : Print The first ten posts links
2 : Print The Short Link a Post
        """
    )
def request_(url):
    global web_content
    session = requests.session()
    session.headers.update({'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/64.0.3282.167 Chrome/64.0.3282.167 Safari/537.36'})
    url = (url)
    req = session.get(url) # request to url
    if req.status_code == 200:
        print(f"\nconnection is ok :{req.status_code}")
        web_content = req.content
    

def filter_(response): # print the short link
    soup = BeautifulSoup(response,"html.parser")
    short_link = soup.select_one(".shorturl-input") # filter the web page
    slv = short_link.find("span").text.replace("\n","").strip() # slv is short link virgool
    print(f"""
----------------------------------------
short link is : {slv}""")

def filter10(response):# print the 10 page link
    soup = BeautifulSoup(response , "html.parser")
    url_link = soup.select('.streamItem-caption a')
    for i in url_link:
        tag = i.h3
        print(tag.string)
        print(i.get('href'))


def switch(number):
    if number == 1:
        request_(input("Paste the Profile link ! :"))
        filter10(web_content)
    elif number == 2:
        request_(input("Paste the link ! :"))
        filter_(web_content)
               

banner()
switch(int(input("please Enter The Number! : ")))
