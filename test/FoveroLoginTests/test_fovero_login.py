import time
import pytest
import selenium
from selenium import webdriver
import allure
from allure_commons.types import AttachmentType

from PageObjects.pom.loginpage import LoginPage
from constants.constants import Constants
import logging

# Assertions and use the Page Object class

@pytest.fixture()
def setup():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get(Constants.app_url())
    return driver

@allure.epic("Fovero Login Test")
@allure.feature("TC#1 - Fovero App Positive Test")
@pytest.mark.positive
def test_fovero_login_positive(setup):
    login_page = LoginPage(driver=setup)
    login_page.login_to_vwo(eml="Dhruvil.patel@concettolabs.com", pwd="Devil@123")
    # dashboardPage = DashboardPage(driver=setup)
    # assert "Aman Ji" in dashboardPage.user_logged_in_text()