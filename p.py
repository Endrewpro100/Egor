import requests
from bs4 import BeautifulSoup


response=requests.get("https://sinoptik.ua/%D0%BF%D0%BE%D0%B3%D0%BE%D0%B4%D0%B0-%D0%BA%D1%80%D0%B5%D0%BC%D0%B5%D0%BD%D1%87%D1%83%D0%B3")
if response.status_code==200:
    bs=BeautifulSoup(response.text, features="html.parser")
    list=bs.find("p", {"class":"today-temp"})
    for el in list:
        print(el.text)
