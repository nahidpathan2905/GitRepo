import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.maximize_window()
driver.get("file:///C:/Users/mulanii/Desktop/WebTable.html")
time.sleep(2)
allrows=driver.find_elements(By.XPATH,"//table[@id='abc1234']//tr")
print(len(allrows))
time.sleep(3)

