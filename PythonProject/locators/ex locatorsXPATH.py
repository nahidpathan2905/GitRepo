import time

from selenium import webdriver
from selenium.webdriver.common.by import By
driver=webdriver.Chrome()
time.sleep(2)
driver.get("https://www.facebook.com")
driver.find_element(By.XPATH,"//input[@type='text']").send_keys("nahid")
time.sleep(2)
driver.find_element(By.XPATH,"//input[@type='password']").send_keys("nahid@123")
time.sleep(2)
driver.find_element(By.XPATH,"//button[@value='1']").click()
time.sleep(2)

