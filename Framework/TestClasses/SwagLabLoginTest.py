import time

from PageClass.Home import SwagLabHomePage
from PageClass.Login import SwagLabLoginPage
from TestClasses.conftest import openbrowser
from Utility.ReadExcel import ReadTD
from Utility.customLoggers import LogGen
from Utility.readProperties import ReadConfig

class Test_SwagLabLogin:
    logger = LogGen.loggen()

    def loginToApp(self,openbrowser):
        driver=openbrowser
        login=SwagLabLoginPage(driver)
        login.enterUsername(ReadConfig.getAppUsername())
        login.enterPassword(ReadConfig.getAppPassword())
        login.clickOnLoginBtn()


    def test_TC1_loginToApp_titleValidation(self,openbrowser):
        self.logger.info("----Test Case execution started-------")
        self.logger.info("----test_TC1_loginToApp_titleValidation-------")
        driver=openbrowser
        self.loginToApp(driver)

        actTitle=driver.title
        expTilte=ReadTD.getTestData(1,1)

        if actTitle==expTilte:
            assert True
            self.logger.info("----Passed- Act & Exp Title match----")
        else:
            driver.save_screenshot(".\\ScreenShots\\test_TC1_loginToApp_titleValidation.png")
            self.logger.error("----Failed- Act & Exp Title mist-match----")
            assert False
        time.sleep(3)
        driver.quit()

    def test_TC2_verifyProductName(self, openbrowser):
        self.logger.info("----Test Case execution started-------")
        self.logger.info("----test_TC2_verifyProductName-------")
        driver = openbrowser
        self.loginToApp(driver)

        home=SwagLabHomePage(driver)
        actProductName=home.getBackpackProductName()
        expProductName=ReadTD.getTestData(2,1)

        if actProductName==expProductName:
             assert True
             self.logger.info("----Passed- Act & Exp product name match----")
        else:
            driver.save_screenshot(".\\ScreenShots\\test_TC2_verifyProductName.png")
            self.logger.error("----Failed- Act & Exp product name mist-match----")
            assert False
        time.sleep(3)
        driver.quit()

    def test_TC3_verifyProductSize(self,openbrowser):
        self.logger.info("----Test Case execution started-------")
        self.logger.info("----test_TC3_verifyProductSize-------")
        driver = openbrowser
        self.loginToApp(driver)

        home=SwagLabHomePage(driver)
        actProductSize=home.getProductSize()
        expProductSize=ReadTD.getTestData(3,1)
        if actProductSize==expProductSize:
            assert True
            self.logger.info("----Passed- Act & Exp product name match----")
        else:
            driver.save_screenshot(".\\ScreenShots\\test_TC3_verifyProductSize.png")
            self.logger.error("----Failed- Act & Exp product size mist-match----")
            assert False
        time.sleep(3)
        driver.quit()



