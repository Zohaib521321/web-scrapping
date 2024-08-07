import requests
from bs4 import BeautifulSoup
response=requests.get("https://www.flipkart.com/search?q=aptop&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=off&as=off"+"&page=3")
print(response)
soup=BeautifulSoup(response.text,"html.parser")
np=soup.find("a",class_="_9QVEpD").get("href")
cnp="https://www.flipkart.com/"+np
print(cnp)
