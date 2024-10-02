import time
from logging import exception

import self
from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from test.FoveroLoginTests.conftest import driver
from utils.common_utils import webdriver_wait


class DashboardPage:
    def __init__(self, driver):
        self.driver = driver

        # Page Locators

   # user_logged_in = (By.ID, "dropdown-basic")
    upcoming_birthday = (By.XPATH, "/html/body/div/div[2]/div[3]/div/div/div[2]/div[1]/div/div[1]/div/div/button[2]")
    upcoming_birthday_forward = (By.XPATH, '//*[@id="root"]/div[2]/div[3]/div/div/div[2]/div[1]/div/div[2]/div/div/button[2]')
    upcoming_birthday_backward = (By.XPATH,'//*[@id="root"]/div[2]/div[3]/div/div/div[2]/div[1]/div/div[2]/div/div/button[1]')
    Attendance = (By.CSS_SELECTOR,"#root > div.sc-dBmzty.bKScJK.sidebarOpen > div.rightSide > div > div > div.mb-3.ps-1.col-lg-4 > div.row > div > div > a > div > div > div > div:nth-child(2) > div")
    close_attendance = (By.CSS_SELECTOR, "body > div.modal.show > div > div > div > div.border-0.flex-column.align-items-start.modal-header > button")
    leaves_upcoming = (By.CSS_SELECTOR, "#root > div.sc-dBmzty.bKScJK.sidebarOpen > div.rightSide > div > div > div.mb-3.col-lg-8 > div.mb-3.row > div.mb-3.mb-lg-0.col-md-6 > div > div.p-0.card-header > div > div > button.fw-semibold.px-2.border-0.border-bottom.rounded-0.undefined.btn.btn-sm")
    wfh_upcoming = (By.CSS_SELECTOR, "#root > div.sc-dBmzty.bKScJK.sidebarOpen > div.rightSide > div > div > div.mb-3.col-lg-8 > div.mb-3.row > div.mb-3.mb-lg-0.ps-1.col-lg-6 > div > div.p-0.card-header > div > div > button.fw-semibold.px-2.border-0.border-bottom.rounded-0.undefined.btn.btn-sm")
    #clicking_graph = (By.XPATH, '//*[@id=//*[@id="reactgooglegraph-1"]/div/div[1]/div/svg/g[1]/g[1]/g[2]/rect[26]')
    Recent_timesheet = (By.XPATH, '//*[@id="root"]/div[2]/div[3]/div/div/div[1]/div[3]/div/div/div[1]/a')
    Recent_timesheet_popup_close_button = (By.CSS_SELECTOR,"body > div.modal.show > div > div > div > div.border-0.flex-column.align-items-start.modal-header > button")
    Recent_timesheet_view_details = (By.CSS_SELECTOR, "#root > div.sc-dBmzty.bKScJK.sidebarOpen > div.rightSide > div > div > div.mb-3.col-lg-8 > div:nth-child(3) > div > div > div.recentTimesheetBoxContainer.card-body > div:nth-child(1) > div > div > div:nth-child(5) > img")

    # Page Actions
    # def get_user_logged_in(self):
    #     return self.driver.find_element(*DashboardPage.user_logged_in)



    def get_upcoming_birthday(self):
        return self.driver.find_element(*DashboardPage.upcoming_birthday)
    # def get_upcoming_birthday_forward(self):
    #     return self.driver.find_element(*DashboardPage.upcoming_birthday_forward)

    def get_upcoming_birthday_forward(self):
        try:
            dd = self.driver.find_element(*DashboardPage.upcoming_birthday_forward)
        except:
            dd = None
        return dd

    # def get_upcoming_birthday_backward(self):
    #     return self.driver.find_element(*DashboardPage.upcoming_birthday_backward)
    def get_upcoming_birthday_backward(self):
        try:
            dd = self.driver.find_element(*DashboardPage.upcoming_birthday_backward)
        except:
            dd = None
        return dd

    def get_attendance(self):
        return self.driver.find_element(*DashboardPage.Attendance)


    def get_close_attendance(self):
        return self.driver.find_element(*DashboardPage.close_attendance)

    def get_leaves_upcoming(self):
        return self.driver.find_element(*DashboardPage.leaves_upcoming)

    def get_wfh_upcoming(self):
        return self.driver.find_element(*DashboardPage.wfh_upcoming)

    # def get_clicking_graph(self):
    #     return self.driver.find_element(*DashboardPage.clicking_graph)

    def get_recent_timesheet(self):
        return self.driver.find_element(*DashboardPage.Recent_timesheet)

    def get_recent_timesheet_popup_close(self):
        return self.driver.find_element(*DashboardPage.Recent_timesheet_popup_close_button)

    def get_recent_timesheet_view_buttom(self):
        return self.driver.find_element(*DashboardPage.Recent_timesheet_view_details)



    # Page Action
    def dashboard_fovero(self):
     #   self.get_user_logged_in()

        print("123")
        self.get_upcoming_birthday().click()

        print("456")
        if self.get_upcoming_birthday_forward():
            self.get_upcoming_birthday_forward().click()
        if self.get_upcoming_birthday_backward():
            self.get_upcoming_birthday_backward().click()
        self.get_attendance().click()
        self.get_close_attendance().click()
        self.get_leaves_upcoming().click()
        self.get_wfh_upcoming().click()


        self.get_recent_timesheet().click()
        self.get_recent_timesheet_popup_close().click()
        time.sleep(1)  # Wait for the scroll action to finish
        print("above")
        print("below")
        self.get_recent_timesheet_view_buttom().click()

    # Close the driver
    driver.quit()

