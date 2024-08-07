import requests
from bs4 import BeautifulSoup
response=requests.get("https://www.flipkart.com/search?q=mobile&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off")
print(response)
soup=BeautifulSoup(response.text,"html.parser")
np=soup.find("a",class_="_9QVEpD").get("href")
cnp="https://www.flipkart.com/"+np
print(cnp)
