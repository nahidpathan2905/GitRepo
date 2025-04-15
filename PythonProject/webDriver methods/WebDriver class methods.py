import time

from selenium import webdriver
#open browser
driver=webdriver.Firefox()
#open application
driver.get("https://www.youtube.com/")
time.sleep(5)
#close browser
driver.close()
driver.quit()

