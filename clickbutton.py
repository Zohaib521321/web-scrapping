from selenium import webdriver
from selenium.webdriver.common.by import By
import time
driver=webdriver.Chrome()
driver.get("https://app.resumas.com/login")
# time.sleep(2)
# button=driver.find_element(By.CLASS_NAME,"Navbar-module--btnprimary--efae2")

# button.click()
# time.sleep(2)
email_field=driver.find_element(By.NAME,"email")
email_field.send_keys("JohnDoe23@gmail.com")
password_field=driver.find_element(By.NAME,"password")
password_field.send_keys("145363647448")
loginButton=driver.find_element(By.CSS_SELECTOR,".btn.btn-primary.w-100")


loginButton.click()
time.sleep(10)
driver.quit()