from selenium import webdriver
from selenium.webdriver import Chrome
import pytest

import os
from dotenv import  load_dotenv
load_dotenv()

driver = webdriver.Chrome()


@pytest.fixture(scope='class')
def setup(request):
    driver.maximize_window()
    email = os.getenv("EMAIL")
    password = os.getenv("PASSWORD")

    request.cls.driver = driver
    request.cls.username = email
    request.cls.password = password


    yield driver # return driver
    driver.quit()