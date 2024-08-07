import requests
import pandas as pd
from bs4 import BeautifulSoup
url="https://test-sites.octoparse.com/table"
response=requests.get(url)
# print(response)
soup=BeautifulSoup(response.text,"html.parser")
div=soup.find("div",class_="ant-table-content")
th=div.find_all("th")
thList=[i.text for i in th]
df=pd.DataFrame(columns=thList)
rows=div.find_all("tr")
for i in rows[1:]:
    data=i.find_all("td")
    row=[i.text for i in data]
    l=len(df)
    df.loc[l]=row
    print(row)
print(df)
df.to_csv("octupus_data.csv")