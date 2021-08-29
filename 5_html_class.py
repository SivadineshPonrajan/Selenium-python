#Locating HTML class
import time
from selenium import webdriver

driver = webdriver.Firefox(executable_path=r'C:/Users/sivad/Desktop/Selenium/geckodriver.exe')
driver.get("file:///C:/Users/sivad/Desktop/Selenium/website.html")

oneElement = driver.find_element_by_class_name('numbers')

print("First class elements is : ")
print(oneElement)
time.sleep(3)
oneElement.click()
time.sleep(3)

inputbox = driver.find_element_by_id('display')
print("Input element is : ")
print(inputbox)
inputbox.clear()
time.sleep(1)


allElements = driver.find_elements_by_class_name('numbers')

for eachElement in allElements:
	print("The element is : ")
	print(eachElement)
	time.sleep(1)
	eachElement.click()

time.sleep(10)

driver.close()