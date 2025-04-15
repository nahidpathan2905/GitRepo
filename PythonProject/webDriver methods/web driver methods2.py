import time

from selenium import webdriver
driver=webdriver.Chrome()
time.sleep(3)
driver.get("https://www.google.com/")
#get title
actTitle=driver.title
print(actTitle)
if actTitle=="Google":  #"google" then fail
    print("pass")
else:
    print("fail")
print(driver.title)
#get current URL
actURL=driver.current_url
print(actURL)
print(driver.current_url)

