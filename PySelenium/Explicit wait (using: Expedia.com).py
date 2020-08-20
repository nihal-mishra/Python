from selenium import webdriver
import time
from selenium.webdriver.common.by import By
import selenium.webdriver.support.expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome(executable_path="/Users/king/Coding/Python/PySelenium/ChDriver/chromedriver")
driver.maximize_window()
driver.get("https://www.expedia.com/")

# flight
driver.find_element_by_xpath('//*[@id="uitk-tabs-button-container"]/li[2]/a').click()

# one way
driver.find_element_by_xpath('//*[@id="uitk-tabs-button-container"]/div[1]/li[2]/a').click()
# origin
driver.find_element_by_xpath('//*[@id="location-field-leg1-origin-menu"]/div[1]/button').send_keys('Lucknow (LKO-Amausi Intl.)')
driver.find_element_by_xpath('//*[@id="location-field-leg1-origin-menu"]/div[2]/ul/li[1]/button').click()

# destination
driver.find_element_by_xpath('//*[@id="location-field-leg1-destination-menu"]/div[1]/button').send_keys('Mumbai (BOM-Chhatrapati Shivaji Intl.)')
driver.find_element_by_xpath('//*[@id="location-field-leg1-destination-menu"]/div[2]/ul/li[1]/button').click()

driver.find_element_by_xpath('//*[@id="d1-btn"]').click()
driver.find_element_by_xpath('//*[@id="wizard-flight-tab-oneway"]/div/div[2]/div/div/div/div/div/div[2]/div/div[1]/div[2]/div[1]/table/tbody/tr[3]/td[7]/button').click()

# clicking done
driver.find_element_by_xpath('//*[@id="wizard-flight-tab-oneway"]/div/div[2]/div/div/div/div/div/div[2]/div/div[2]/button').click()

# searching for flight
driver.find_element_by_xpath('//*[@id="wizard-flight-pwa-1"]/div[3]/div[2]/button').click()

wait = WebDriverWait(driver, 10)
wait.until(EC.element_to_be_clickable(By.XPATH('//*[@id="stops"]/div/div[3]'))).click()
time.sleep(8)
driver.quit()