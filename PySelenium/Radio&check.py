from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import selenium.webdriver.support.expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome(executable_path='/Users/king/Coding/Python/PySelenium/ChDriver/chromedriver')
driver.maximize_window()
driver.get('https://fs2.formsite.com/meherpavan/form2/index.html?1537702596407')

status = driver.find_element_by_id('RESULT_RadioButton-7_1').is_selected()
print(status)

driver.find_element_by_id('RESULT_TextField-1').send_keys('Nihal')

driver.find_element_by_class_name("multiple_choice").click()

status = driver.find_element_by_id('RESULT_RadioButton-7_1').is_selected()
print(status)
time.sleep(10)
