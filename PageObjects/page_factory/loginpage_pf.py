from seleniumpagefactory.Pagefactory import PageFactory
from utils.common_utils import webdriver_wait

from selenium.webdriver.common.by import By


class LoginPage(PageFactory):
    # Webdriver - Init
    def __init__(self, driver):
        self.driver = driver
        self.highlight = True


        # Page Locators

    locators = {
        'email': ('ID', "email"),
        'password': ('ID', 'password'),
        'signin': ('XPATH', '//*[@id="root"]/div[3]/div/div/div[2]/div/div/form/div[2]/div/button')
    }


    # Page Actions

    def login_to_vwo(self, email, pwd):
        self.email.set_text(email)
        self.password.set_text(pwd)
        self.signin.click_button()