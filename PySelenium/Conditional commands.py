from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(executable_path='/Users/king/Coding/Python/PySelenium/ChDriver/chromedriver')
driver.get("https://www.google.com")
element_to_check = driver.find_element_by_xpath("//*[@id='tsf']/div[2]/div[1]/div[1]/div/div[2]/input")
# Search bar id.
print(f'Element to check is displayed - {element_to_check.is_displayed()}')
print(f'Element to check is Enabled - {element_to_check.is_enabled()}')

icon_to_check = driver.find_element_by_xpath("//*[@id='gbw']/div/div/div[2]/div[2]/div[1]/a/img")
# User icon on top right
print(f'Icon to check is displayed - {icon_to_check.is_displayed()}')
print(f'Icon to check is Enabled - {icon_to_check.is_enabled()}')