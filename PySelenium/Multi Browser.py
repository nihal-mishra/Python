from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(executable_path="/Users/king/Coding/Python/PySelenium/ChDriver/chromedriver")
driver.get("https://www.google.com/")
print(driver.title)
html = driver.page_source

driver.find_element_by_xpath("//*[@id='tsf']/div[2]/div[1]/div[3]/center/input[2]").click()