import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
time.sleep(2)
driver.get("https://www.gmail.com/")
driver.find_element(By.XPATH,"//input[@name='identifier']").send_keys("nahid")
time.sleep(5)
