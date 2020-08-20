from selenium import webdriver
from selenium.webdriver.support.ui import Select

driver = webdriver.Chrome(executable_path='/Users/king/Coding/Python/PySelenium/ChDriver/chromedriver')
driver.get('https://fs2.formsite.com/meherpavan/form2/index.html?1537702596407')

element = driver.find_element_by_id('RESULT_RadioButton-9')
drop_down = Select(element)

# select
drop_down.select_by_index(2)
drop_down.select_by_value('Radio-2')
drop_down.select_by_visible_text("Afternoon")

# count
print(len(drop_down.options))

# capture and print the options
options = drop_down.options
lis = []
for option in options:
	lis.append(option.text)
print(lis)