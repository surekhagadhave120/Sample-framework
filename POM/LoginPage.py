from Data.ExcelLib import read_locators
from Library.selenium_wrapper import SeleniumWrapper
from Library.config import Config


class LoginPage(SeleniumWrapper):
    locators = read_locators("loginPage")

    def __init__(self, driver):
        super().__init__(driver)

    def enter_username(self):
        username = LoginPage.locators['txt_email']  # (id, 'email')
        self.enter_text(username, Config.USERNAME)

    def click_continue_btn(self):
        continuebtn = LoginPage.locators['btn_continue']
        self.click_element(continuebtn)

    def enter_password(self):
        password = LoginPage.locators['txt_password']
        self.enter_text(password, Config.PASSWORD)

    def click_signin_btn(self):
        login = LoginPage.locators['btn_signin']
        self.click_element(login)

    def click_forgot_password_link(self):
        forget = LoginPage.locators['link_forget']
        self.click_element(forget)
