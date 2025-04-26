import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.get("https://demo.guru99.com/test/delete_customer.php")
time.sleep(2)
driver.find_element(By.XPATH,"//input[@type='text']").send_keys("9875")
time.sleep(2)
driver.find_element(By.XPATH, "//input[@type='submit']").click()

#get Text
value=driver.switch_to.alert.text
print(value)
#driver.switch_to.alert.accept()
driver.switch_to.alert.dismiss()
time.sleep(5)
