from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path='/Users/king/Coding/Python/PySelenium/ChDriver/chromedriver')
driver.maximize_window()
driver.get('http://automationpractice.com/index.php')

links = driver.find_elements(By.TAG_NAME, 'a')
print(len(links))

links_list = []
for link in links:
	links_list.append(link.text)
print(links_list)

driver.find_element(By.PARTIAL_LINK_TEXT, 'T-SHIRTS').click()