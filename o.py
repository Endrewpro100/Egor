import requests
from bs4 import BeautifulSoup


response=requests.get("https://coinmarketcap.com/")
if response.status_code==200:
    bs=BeautifulSoup(response.text, features="html.parser")
    list=bs.find_all("a", {"href":"/currencies/tron/#markets"})
    for el in list:
        print(el.text)
