import time

import pytest

from POM.LoginPage import LoginPage
from POM.HomePage import HomePage


@pytest.mark.login
def test_login(setup):
    print(setup)
    lp = LoginPage(setup)
    lp.enter_username()
    lp.click_continue_btn()
    lp.enter_password()
    lp.click_signin_btn()
    dp = HomePage(setup)
    time.sleep(4)
    username_text = dp.get_user_name()
    print(username_text)
    assert username_text == "surekha"
