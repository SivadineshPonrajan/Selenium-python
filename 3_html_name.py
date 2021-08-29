#Locating HTML name
import time
from selenium import webdriver

driver = webdriver.Firefox(executable_path=r'C:/Users/sivad/Desktop/Selenium/geckodriver.exe')
driver.get("file:///C:/Users/sivad/Desktop/Selenium/website.html")

element = driver.find_element_by_name('username')

print("My input element is : ")
print(element)

element.clear()
time.sleep(3)
element.send_keys("digisafenations")
time.sleep(5)

driver.close()