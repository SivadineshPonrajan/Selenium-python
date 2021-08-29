from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Firefox(executable_path=r'C:/Users/sivad/Desktop/Selenium/geckodriver.exe')
driver.get("http://www.google.com/")

elem = driver.find_element_by_name("q")
elem.clear()
elem.send_keys("digisafenations")
elem.send_keys(Keys.RETURN)
time.sleep(10)

driver.close()