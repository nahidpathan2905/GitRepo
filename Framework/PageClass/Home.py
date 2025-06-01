from selenium.webdriver.common.by import By
from selenium import webdriver

class SwagLabHomePage:

    #1: declare web elements globally
    textBackpackProductXpath="//div[text()='Sauce Labs Backpack']"

    allProductPriceXpath = "//div[@class='inventory_item_price']"

    #2: initialization webdriver object globally
    def __init__(self,driver):
        self.driver=driver

    #3: perform actions
    def getBackpackProductName(self):
        productName=self.driver.find_element(By.XPATH,self.textBackpackProductXpath).text
        return productName
    def getProductSize(self):
        productSize=self.driver.find_elements(By.XPATH,)
        return len(productSize)
    def getAllProductPrice(self):
        allproductprice=self.driver.find_elements(By.XPATH,self.allProductPriceXpath)

        TotalProductPrice=0

        for i in allproductprice:
            s1=i.text
            s1=s1[1:]
            s1=float(s1)

            TotalProductPrice=TotalProductPrice+s1

            return TotalProductPrice