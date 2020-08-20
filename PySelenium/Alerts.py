from selenium import webdriver
import time

driver = webdriver.Chrome(executable_path='/Users/king/Coding/Python/PySelenium/ChDriver/chromedriver')
driver.maximize_window()
driver.get("https://testautomationpractice.blogspot.com")

driver.find_element_by_xpath('//*[@id="HTML9"]/div[1]/button').click()
time.sleep(5)
driver.switch_to_alert().accept()

driver.find_element_by_xpath('//*[@id="HTML9"]/div[1]/button').click()
time.sleep(5)
driver.switch_to_alert().dismiss()
time.sleep(5)
driver.quit()


