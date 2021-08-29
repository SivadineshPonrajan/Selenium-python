from selenium import webdriver 
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC 
from selenium.webdriver.common.by import By 


driver = webdriver.Firefox(executable_path=r'C:/Users/sivad/Desktop/Selenium/geckodriver.exe')
driver.get("http://www.python.org/")

try:
	element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "start-shell")))
finally:
	driver.quit()