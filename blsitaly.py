from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Initialize the WebDriver
driver = webdriver.Chrome()

try:
    for _ in range(100):  # Adjust the range for the number of requests you want to make
        # Open the URL
        driver.get("https://blsitalypakistan.com/bls_appmnt/bls-italy-appointment/MUFtdFNpNjQ2ODM3MDMxMjk/NjlmYmRHajQzODQwNjk3MDg3/MWFka3JJMjE1NTI4NDA2NzY")

        # Wait for the page to load
        time.sleep(0.5)  # Adjust timing as necessary

        # Locate the captcha input field by its name attribute
        captcha_input = driver.find_element(By.NAME, "captcha_code")

        # Fill in the captcha field (Replace with the actual captcha code)
        captcha_input.send_keys("YourCaptchaCode")

        # Optionally, you can submit the form if needed
        # captcha_input.send_keys(Keys.RETURN)

        # Short delay before the next request
        time.sleep(0.1)  # Adjust timing as necessary

finally:
    # Close the browser
    driver.quit()
