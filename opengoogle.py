from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

options = webdriver.ChromeOptions()
options.add_argument('user-data-dir=C:\\Users\\Zohaib\\AppData\\Local\\Google\\Chrome\\User Data')
options.add_argument('profile-directory=Profile 5')
driver = webdriver.Chrome(options=options)
driver.get('https://google.com')
time.sleep(10)
driver.quit()
# # Set up the path to your Chrome profile
# chrome_profile_path = "C:\\Users\\Zohaib\\AppData\\Local\\Google\\Chrome\\User Data\\Profile 5"

# # Set up Chrome options to use the specified profile
# options = webdriver.ChromeOptions()
# options.add_argument(f"user-data-dir={chrome_profile_path}")

# # Initialize the Chrome driver with the specified options
# driver = webdriver.Chrome()

# try:
#     # Open a specific URL
#     driver.get("https://www.example.com")

#     # Perform other actions as needed
#     # ...
    
# finally:
#     # Close the browser
#     driver.quit()
