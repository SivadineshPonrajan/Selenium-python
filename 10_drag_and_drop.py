#Action Chain performs drag&drop, hover, etc...

from selenium import webdriver
import time
from selenium.webdriver import ActionChains

driver = webdriver.Firefox(executable_path=r'C:/Users/sivad/Desktop/Selenium/geckodriver.exe')
driver.get("http://jqueryui.com/droppable")
driver.switch_to.frame(0)

action = ActionChains(driver)

source = driver.find_element_by_id('draggable')
target = driver.find_element_by_id('droppable')

action.drag_and_drop_by_offset(source, 100, 100).perform()
time.sleep(2)
action.drag_and_drop(source, target).perform()
time.sleep(2)

driver.close()