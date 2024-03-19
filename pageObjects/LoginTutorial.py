from selenium import webdriver
from selenium.webdriver.common.by import By
class Login:
    textbox_email_id = 'login_email'
    textbox_password_id = 'login_password'
    button_login_id = 'sign_in_btn'
    link_profileImage_id = 'profileImage'
    button_logout_xpath = "//a[@class='logout']"

    def __init__(self, driver):
        self.driver = driver

    def setUserName(self, username):
        self.driver.find_element(By.ID, self.textbox_email_id).send_keys(username)

    def setPassword(self, password):
        self.driver.find_element(By.ID, self.textbox_password_id).send_keys(password)

    def clickLogin(self):
        self.driver.find_element(By.ID, self.button_login_id).click()

    def clickOnProfileImage(self):
        self.driver.find_element(By.ID, self.link_profileImage_id).click()

    def clickLogout(self):
        self.driver.find_element(By.XPATH, self.button_logout_xpath).click()

    






