from bs4 import BeautifulSoup
import requests
url="https://webscraper.io/test-sites/e-commerce/allinone/computers"
response=requests.get(url)
# print(response.text)
soap=BeautifulSoup(response.text,"html.parser")
print(soap.prettify())