import time
import pytest
import selenium
from selenium import webdriver
import allure
from allure_commons.types import AttachmentType

from PageObjects.pom.dashboard import DashboardPage
from PageObjects.pom.loginpage import LoginPage
from constants.constants import Constants
from PageObjects.pom.loginpage import LoginPage
import logging
from test.FoveroLoginTests.test_fovero_login import test_fovero_login_positive


# Assertions and use the Page Object class

@pytest.fixture()
def setup():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get(Constants.app_url())
    return driver

@allure.epic("Fovero Dashboard Test")
@allure.feature("TC#1 - After Login Redirect to the Dashboard page")
@pytest.mark.positive


def test_fovero_dashboard_positive(setup):
    test_fovero_login_positive(setup)
    time.sleep(15)
    dashboardPage = DashboardPage(driver=setup)
#    dashboardPage.get_user_logged_in()
#    assert "Dhruvil Patel" in dashboardPage.dashboard_fovero()
    dashboardPage.dashboard_fovero()
    time.sleep(15)









