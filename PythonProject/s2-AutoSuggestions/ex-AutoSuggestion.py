import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.google.com/")
time.sleep(5)

driver.find_element(By.XPATH,"//textarea[@class='gLFyf']").send_keys("iphone 16")
time.sleep(1)

allOptions=driver.find_elements(By.XPATH,"//ul[@class='G43f7e'][1]/li")

expText="iphone 16 pro price"
for i in allOptions:
    actText=i.text
    if actText==expText:
        i.click()
        break

time.sleep(10)
