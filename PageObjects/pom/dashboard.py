from selenium.webdriver.common.by import By
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

    # Page Actions
    # def get_user_logged_in(self):
    #     return self.driver.find_element(*DashboardPage.user_logged_in)

    def get_upcoming_birthday(self):
        return self.driver.find_element(*DashboardPage.upcoming_birthday)
    def get_upcoming_birthday_forward(self):
        return self.driver.find_element(*DashboardPage.upcoming_birthday_forward)

    def get_upcoming_birthday_backward(self):
        return self.driver.find_element(*DashboardPage.upcoming_birthday_backward)

    def get_attendance(self):
        return self.driver.find_element(*DashboardPage.Attendance)

    def get_close_attendance(self):
        return self.driver.find_element(*DashboardPage.close_attendance)

    # Page Action
    def dashboard_fovero(self):
     #   self.get_user_logged_in()
        print("123")
        self.get_upcoming_birthday().click()
        print("456")
        self.get_upcoming_birthday_forward().click()
        self.get_upcoming_birthday_backward().click()
        self.get_attendance().click()
        self.get_close_attendance().click()

