from selenium import webdriver
from selenium.webdriver.common.by import By
class Enrolled:
    button_Certification_xpath = '//a[@role="button"]'
    button_Enrolled_xpath = "(//a[@class='nav-link'])[3]"
    link_SMR_xpath = "//a[text()='Search More Roles']"

    def __init__(self, driver):
        self.driver = driver

    def clickCertification(self):
        self.driver.find_element(By.XPATH, self.button_Certification_xpath).click()

    def clickEnrolled(self):
        self.driver.find_element(By.XPATH, self.button_Enrolled_xpath).click()

    def clickSMR(self):
        self.driver.find_element(By.XPATH, self.link_SMR_xpath).click()
        



