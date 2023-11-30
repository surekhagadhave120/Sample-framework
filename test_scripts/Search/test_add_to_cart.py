from selenium.webdriver.common.by import By

from POM.HomePage import HomePage


def test_product_order(setup):
    driver = setup
    driver.implicitly_wait(5)
    hp = HomePage(setup)
    text = "tshirt for women"
    hp.enter_search_text(text)
    hp.click_go_btn()
    search_result = driver.find_element(By.XPATH, "//span[@class='a-color-state a-text-bold']")
    assert search_result.is_displayed()
    hp.click_product()
    hp.click_add_to_cart_btn()
    cart=driver.find_element(By.XPATH, "//span[@class='a-size-medium-plus a-color-base sw-atc-text a-text-bold']")
    assert cart.is_displayed()


