from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException
from selenium.webdriver.support.wait import WebDriverWait


def is_visible(self, loc_type, loc_value):
    def wrapper(driver):
        try:
            displayed = self.driver.find_element(loc_type, loc_value).is_displayed
            enabled = self.driver.find_element(loc_type, loc_value).is_enabled()
        except(NoSuchElementException, StaleElementReferenceException):
            return False
        else:
            return displayed and enabled
    return wrapper


def _wait(func):
    def wrapper2(self, element, text=None, item=None):
        wait = WebDriverWait(self, timeout=10)
        w = wait.until(is_visible(self, element[0], element[1]))
        if w:
            if text:
                func(self, element, text)
            elif item:
                func(self, element, item)
            else:
                func(self, element)
        else:
            raise NoSuchElementException
    return wrapper2