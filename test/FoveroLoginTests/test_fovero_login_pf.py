import time
import pytest
import selenium
#import self
from selenium import webdriver
from PageObjects.page_factory.loginpage_pf import LoginPage
#from PageObjects.page_factory.dashboardpage_pf import DashboardPage
import allure
from allure_commons.types import AttachmentType
from constants.constants import Constants
import logging

@allure.epic("Fovero App")
@allure.feature("Login Test")
@pytest.fixture()
def setup():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get(Constants.app_url())
    return driver

def __init__(self):
    self.password = "Devil@123"
    self.email = "Dhruvil.patel@concettolabs.com"

@pytest.mark.usefixtures("setup")
@pytest.mark.qa

def test_fovero_login_positive(setup):
    LOGGER = logging.getLogger(__name__)
    LOGGER.info("Starting the Testcase")
    driver = setup
    driver.get(Constants.app_url())
    login_page = LoginPage(driver)
    login_page.login_to_vwo(email="Dhruvil.patel@concettolabs.com", pwd="Devil@123")
    # dashboard_page = DashboardPage(driver)
    # username = dashboard_page.user_logged_in_text()
    # assert "Dashboard" in driver.title
    # assert "Aman Ji" == username
    # time.sleep(5)


