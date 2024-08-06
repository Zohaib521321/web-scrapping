from bs4 import BeautifulSoup
import requests
import re
url="https://webscraper.io/test-sites/e-commerce/allinone/computers"
response=requests.get(url)
# print(response.text)
soap=BeautifulSoup(response.text,"html.parser")
# print(soap.div.h1)
# Find Url test

findUrl="https://webscraper.io/test-sites/e-commerce/allinone/computers/tablets"
findResponse=requests.get(findUrl)
findSoup=BeautifulSoup(response.text,"html.parser")
description=findSoup.find("p",class_="description")
print(description)

print(findSoup.find("h4",{"class":"pull-right"}).string)


# Find all 

findAllDescription=findSoup.find_all("p",class_="description")
for i in findAllDescription:
    print(i.text)
findspecificDesc=findSoup.find_all(string="$96.99")
print("Specific desc are " + str(findspecificDesc)) 

# Regex in findall
allTags=findSoup.find_all(string=re.compile("Lenovo"))
print(allTags)
