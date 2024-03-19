import time

from selenium import webdriver
from pageObjects.LoginTutorial import Login
from Utilities.readProperties import ReadConfig
from Utilities.customLog import LogInfoGenerator

class Test_001_Login:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUsername()
    password = ReadConfig.getPassword()

    log = LogInfoGenerator.logGen()

    def test_LoginPage(self, setUp):
        self.log.info("#############TC_001 Started#############")
        self.driver = setUp
        self.driver.get(self.baseURL)
        act_title = self.driver.title
        time.sleep(2)
        if act_title == "Login - Video Courses, eBooks, Certifications | Tutorialspoint":
            assert True
            self.log.info("#############TC_001 Complete#############")
        else:
            self.driver.save_screenshot("C:\\Users\\lokes\\PycharmProjects\\seleniumAutomation\\ScreenShots\\InvalidWebpage.png")
            assert False
            self.log.info("#############TC_001 Failed#############")

    def test_LoginTutorial(self, setUp):
        self.log.info("#############TC_001 Started#############")
        self.driver = setUp
        self.driver.get(self.baseURL)

        self.lp = Login(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        time.sleep(1)
        act_title = self.driver.title
        if act_title == "Login - Video Courses, eBooks, Certifications | Tutorialspoint":
            assert True
            self.log.info("#############TC_001 Complete#############")
        else:
            self.driver.save_screenshot("C:\\Users\\lokes\\PycharmProjects\\seleniumAutomation\\ScreenShots\\InvalidWebpage.png")
            assert False


