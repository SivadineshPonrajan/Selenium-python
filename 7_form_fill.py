from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time

driver = webdriver.Firefox(executable_path=r'C:/Users/sivad/Desktop/Selenium/geckodriver.exe')
driver.get("file:///C:/Users/sivad/Desktop/Selenium/website.html")

element = Select(driver.find_element_by_tag_name('select'))

element.select_by_index(2)
time.sleep(2)

element.select_by_visible_text("500")
time.sleep(2)

element.select_by_value("100")
time.sleep(2)

options = element.options
print(options)

submit_btn = driver.find_element_by_name('continue')
submit_btn.submit()
time.sleep(2)

driver.close()