import time
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from Library.custom_wait import _wait, is_visible
from Library.config import Config


class SeleniumWrapper:
    def __init__(self, driver):
        self.driver = driver

    @_wait
    def enter_text(self, element, text):
        self.driver.find_element(element[0], element[1]).send_keys(text)

    @_wait
    def click_element(self, element):
        self.driver.find_element(element[0], element[1]).click()

    @_wait
    def select_element(self, element, item=None):
        element = self.driver.find_element(element[0], element[1])
        s = Select(element)
        if isinstance(item, str):
            s.select_by_visible_text(item)
        elif isinstance(item, int):
            s.select_by_index(item)
        else:
            raise Exception

    def get_text_from_element(self, element):
        object = self.driver.find_element(element[0], element[1])
        return object.text

    def wait_till(self, element):
        wait = WebDriverWait(self.driver, timeout=10)
        if wait.until(is_visible(self, element[0], element[1])):
            return
        else:
            raise NoSuchElementException

    def get_table_data(self, element):
        rows = self.driver.find_elements(element[0],element[1])
        table_data = []
        for row in rows:
            table_data.append(row.text)
        return table_data

    def clear_data(self, element):
        self.driver.find_element(element[0],element[1]).clear()
        self.driver.refresh()
        time.sleep(5)

    def get_no_of_rows(self, element):
        rows = self.driver.find_elements(By.XPATH, element)
        return len(rows)

    def sort_by_column(self, element):
        column = self.driver.find_element(element[0], element[1])
        column.send_keys(Keys.ENTER)
        time.sleep(4)

    def mouse_hover_on(self, element):
        act = ActionChains(self.driver)
        ele = self.driver.find_element(element[0], element[1])
        act.move_to_element(ele).perform()
        time.sleep(2)
        act.click(ele).perform()

    def execute_Script_to(self, element):
        move = self.driver.find_element(element[0], element[1])
        self.driver.execute_script("agruments[0].scrollIntoView(true);", move)

    def pdf_upload(self, element):
        upload_textbox = self.driver.find_element(element[0], element[1])
        upload_textbox.send_keys(Config.SAMPLE_PDF)
        time.sleep(2)

    def photo_upload(self, element):
        upload_textbox = self.driver.find_element(element[0], element[1])
        upload_textbox.send_keys(Config.SAMPLE_PHOTO)
        time.sleep(4)

    def clear_textbox(self, element):
        self.driver.find_element(element[0], element[1]).clear()

    def samplejob_upload(self, element):
        upload_textbox = self.driver.find_element(element[0], element[1])
        upload_textbox.send_keys(Config.SAMPLE_CSV)
        time.sleep(4)