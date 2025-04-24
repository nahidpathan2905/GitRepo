import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.maximize_window()
driver.get("file:///C:/Users/mulanii/Desktop/WebTable.html")
time.sleep(2)

bookName=driver.find_element(By.XPATH,"//table[@id='abc1234']//td[text()='200']//parent::tr/td[2]").text
print(bookName)

bookprice=driver.find_element(By.XPATH,"//table[@id='abc1234']//td[text()='300']//parent::tr/td[3]").text
print(bookprice)
time.sleep(2)

value=driver.find_element(By.XPATH,"//table[@id='abc1234']//tr[4]/td[3]").text
print(value)