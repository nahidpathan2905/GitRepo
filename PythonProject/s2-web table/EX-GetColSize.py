import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.maximize_window()
driver.get("file:///C:/Users/mulanii/Desktop/WebTable.html")
allCol=driver.find_elements(By.XPATH,"//table[@id='abc1234']//tr[4]/td")
print(len(allCol))
time.sleep(3)

