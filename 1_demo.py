from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Firefox(executable_path=r'C:\\Users\\sivad\\Desktop\\Selenium\\geckodriver.exe') 
driver.get("https://www.google.com/")

driver.maximize_window()

elem = driver.find_element_by_name("q")
elem.clear()
elem.send_keys("digisafenations")
time.sleep(3)
elem.send_keys(Keys.RETURN)

driver.implicitly_wait(3)
driver.find_element_by_xpath('//*[@id="rso"]/div[1]/div/div/div[1]/a/h3').click()
time.sleep(3)
instaURL = driver.find_element_by_xpath('/html/body/footer/div/div/div/div[1]/ul/li[3]/a')
instaURL.location_once_scrolled_into_view
time.sleep(3)
instaURL.click()
time.sleep(3)

driver.close()