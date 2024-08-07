import requests
import pandas as pd
from bs4 import BeautifulSoup

# Step 1: Get the webpage content
url = "https://webscraper.io/test-sites/e-commerce/allinone/computers/tablets"
response = requests.get(url)
print(response)
soup = BeautifulSoup(response.text, 'html.parser')

# Step 2: Extract titles, prices, and descriptions
titles = soup.find_all("a", class_="title")
titlesList = [i.text for i in titles]

prices = soup.find_all("h4", class_="pull-right")
pricesList = [i.text for i in prices]

descriptions = soup.find_all("p", class_="description")
descriptionList = [i.text for i in descriptions]

# Print the extracted lists
print(titlesList)
print(pricesList)
print(descriptionList)

# Step 3: Create a DataFrame
print(len(titlesList))
print(len(pricesList))
print(len(descriptionList))
data = {
    "product":titlesList,
    "Price": pricesList,
    "Description": descriptionList
}
df = pd.DataFrame(data)
print(df)
# # Step 4: Save the DataFrame to a CSV file
df.to_csv("tablets.csv", index=False)

# print("Data saved to tablets.csv")
