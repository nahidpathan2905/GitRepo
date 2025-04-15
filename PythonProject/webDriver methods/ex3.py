import time

from selenium import webdriver
driver=webdriver.Chrome()
time.sleep(3)
driver.maximize_window()
time.sleep(3)
driver.minimize_window()
time.sleep(2)
driver.maximize_window()
time.sleep(2)
driver.fullscreen_window()
time.sleep(2)
