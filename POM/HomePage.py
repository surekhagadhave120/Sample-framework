from selenium.webdriver.common.by import By
from Library.selenium_wrapper import SeleniumWrapper

class HomePage(SeleniumWrapper):
    def __init__(self, driver):
        super().__init__(driver)

    def get_user_name(self):
        username = (By.XPATH, "//div[@class='nav-line-1-container']/span")
        return self.get_text_from_element(username)

    def enter_search_text(self,text):
        search = (By.ID, "twotabsearchtextbox")
        self.enter_text(search, text)

    def click_go_btn(self):
        go=(By.XPATH,"//input[@value='Go']")
        self.click_element(go)

    def get_search_result(self):
        search_result=(By.XPATH,"//span[@class='a-color-state a-text-bold']")
        self.get_text_from_element(search_result)

    def click_product(self):
        product=(By.XPATH,"//div[@class='s-widget-container s-spacing-small s-widget-container-height-small"
                          " celwidget slot=MAIN template=SEARCH_RESULTS widgetId=search-results_1']//img")
        self.click_element(product)

    def click_add_to_cart_btn(self):
        add_to_cart_button=(By.ID,"add-to-cart-button")
        self.click_element(add_to_cart_button)

    def get_added_to_cart_text(self):
        text=(By.XPATH,"//span[@class='a-size-medium-plus a-color-base sw-atc-text a-text-bold']")
        self.click_element(text)