from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome(executable_path="/Users/king/Coding/Python/PySelenium/ChDriver/chromedriver")
driver.get("https://www.google.com")
print(driver.title)
time.sleep(4)
driver.get("https://www.yahoo.com")
print(driver.title)
time.sleep(4)
driver.back()
print(driver.title)
time.sleep(4)
driver.forward()
print(driver.title)
time.sleep(10)
driver.quit()