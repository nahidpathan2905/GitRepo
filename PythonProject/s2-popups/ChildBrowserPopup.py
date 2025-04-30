import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://skpatro.github.io/demo/links/")
driver.implicitly_wait(10)
time.sleep(2)
#click on New Tab from main pg
driver.find_element(By.XPATH,"//input [@value='New Tab']").click()
#get child window Id
allIds=driver.window_handles
#switch to child window
driver.switch_to.window(allIds[1])
#click on training link
driver.find_element(By.XPATH,"(//span[text()='Training'])[1]").click()
time.sleep(5)
#switch to main pg/window
driver.switch_to.window(allIds[0])
time.sleep(3)
driver.find_element(By.XPATH,"(//input [@name='New Window']").click()
time.sleep(10)

