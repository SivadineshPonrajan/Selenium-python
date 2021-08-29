#Locating HTML xpath

from selenium import webdriver

driver = webdriver.Firefox(executable_path=r'C:/Users/sivad/Desktop/Selenium/geckodriver.exe')
driver.get("file:///C:/Users/sivad/Desktop/Selenium/website.html")

userinput = driver.find_element_by_xpath('/html/body/center/form[2]/input') #Absolute
userform = driver.find_element_by_xpath('//*[@id="input2"]') #Xpath_Id
checkform = driver.find_element_by_xpath("//form[2]/input") #Relative

print("My elements are : ")
print(userinput)
print(userform)
print(checkform)

driver.close()