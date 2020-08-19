from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(executable_path='/Users/king/Coding/Python/PySelenium/ChDriver/chromedriver')

driver.get('http://www.newtours.demoaut.com/')
driver.implicitly_wait(10)  # time in seconds
assert "Welcome: Mercury Tours" in driver.title

driver.find_element_by_name('userName').send_keys('mercury')
driver.find_element_by_name('password').send_keys('mercury')
driver.find_element_by_name('login').click()