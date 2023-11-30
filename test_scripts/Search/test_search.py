import time

import pytest
from selenium.webdriver.common.by import By

from POM.HomePage import HomePage


@pytest.mark.home
def test_search(setup):
    driver = setup
    driver.implicitly_wait(5)
    hp = HomePage(setup)
    text = "birthday candles"
    hp.enter_search_text(text)
    hp.click_go_btn()
    search_result = driver.find_element(By.XPATH, "//span[@class='a-color-state a-text-bold']")
    assert search_result.is_displayed()
