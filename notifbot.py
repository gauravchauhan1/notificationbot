import requests
from bs4 import BeautifulSoup
URL="http://164.100.213.114/"
headers={"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36 OPR/72.0.3815.459'}
page=requests.get(URL,headers=headers)
soup=BeautifulSoup(page.content,'html.parser')
notif=soup.find(class_="eachNotification").text
print(notif)

