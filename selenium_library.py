from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Initialize the Chrome driver
driver = webdriver.Chrome()

# Open the specified URL
driver.get("https://www.python.org/")

# Wait for the page to load completely (optional)
time.sleep(2)

# Find the input element by its name (assuming the name is 'q')
search_box = driver.find_element(By.NAME, "q")  # Adjust the name as needed

# Enter the text "pycorn" into the search box
search_box.send_keys("selenium")

# Simulate pressing the Enter key
search_box.send_keys(Keys.RETURN)

# Optional: Keep the browser open for a while to see the result
time.sleep(10)

# Close the driver
driver.quit()
