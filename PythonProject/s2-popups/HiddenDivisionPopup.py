import time
from pkgutil import extend_path

from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.get("https://www.mobikwik.com/")
time.sleep(2)
#click on login button

driver.find_element(By.XPATH,"(//span[text()='Login'])[1]").click()
time.sleep(2)
driver.find_element(By.XPATH,"//input[@id='email']").send_keys(987654)
time.sleep(2)