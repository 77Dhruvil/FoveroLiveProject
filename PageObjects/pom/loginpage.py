from selenium.webdriver.common.by import By
from utils.common_utils import webdriver_wait

#TODO - 5. Class and Object
class LoginPage:  #TODO - 4. Encapsulation

    def __init__(self, driver): #TODO - 6. Constructor

        self.driver = driver

    # Page Locators
    email = (By.ID,"email")
    password = (By.ID,"password")
    signin = (By.XPATH, '//*[@id="root"]/div[3]/div/div/div[2]/div/div/form/div[2]/div/button')

    # Page Actions
    def get_email(self):
        return self.driver.find_element(*LoginPage.email)

    def get_password(self):
        return self.driver.find_element(*LoginPage.password)

    def get_signin(self):
        return self.driver.find_element(*LoginPage.signin)


    def login_to_vwo(self, eml, pwd):
        self.get_email().send_keys(eml)
        self.get_password().send_keys(pwd)
        self.get_signin().click()