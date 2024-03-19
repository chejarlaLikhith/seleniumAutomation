from pageObjects.LoginTutorial import Login
from Utilities.readProperties import ReadConfig
from Utilities.customLog import LogInfoGenerator
from pageObjects.CertificationEnrolled import Enrolled

class Test_002_Enrolled:

    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUsername()
    password = ReadConfig.getPassword()

    log = LogInfoGenerator.logGen()

    def test_CertificationEnrolled(self, setUp):
        self.log.info("####################CertificationEnrolled Test Case Started#################")
        self.driver = setUp
        self.driver.get(self.baseURL)

        self.lp = Login(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()

        self.CertificateEnrolled = Enrolled(self.driver)
        self.CertificateEnrolled.clickCertification()
        self.CertificateEnrolled.clickEnrolled()
        self.CertificateEnrolled.clickSMR()
        self.driver.save_screenshot("C:\\Users\\lokes\\PycharmProjects\\seleniumAutomation\\ScreenShots\\CertifyEnrolled.png")
        self.log.info("####################CertificationEnrolled Test Case Completed#################")




