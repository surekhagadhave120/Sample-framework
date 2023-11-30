import time
import warnings

import pytest

from pytest import fixture
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from Library.config import Config
from POM.LoginPage import LoginPage

driver ="chrome"
@fixture
def setup():
    global driver

    if Config.BROWSER_NAME.upper() == "CHROME":
        serv_obj1=Service(Config.CHROME_PATH)
        driver = webdriver.Chrome(service=serv_obj1)

    elif Config.BROWSER_NAME.upper() == "EDGE":
        serv_obj2=Service(Config.EDGE_PATH)
        driver = webdriver.Edge(service=serv_obj2)

    else:
        serv_obj3 = Service(Config.GECKO_PATH)
        driver = webdriver.Firefox(service=serv_obj3)

    time.sleep(5)
    driver.maximize_window()
    driver.delete_all_cookies()
    driver.get(Config.URL)
    time.sleep(5)
    yield driver
    driver.close()

# code to attach screenshot to the html report generated
@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    pytest_html = item.config.pluginmanager.getplugin('html')
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, 'extra', [])
    if report.when == "call" or report.when == "setup":
        xfail = hasattr(report, "wasxfail")
        if (report.skipped and xfail) or (report.failed and not xfail):
            file_name = report.nodeid.replace("::", "_") + ".jpg"
            _capture_screenshot(file_name)
            if file_name:
                html = '<div><img src="%s" alt="screenshot" style="width:304px;height:228px;" ' \
                       'onclick=window.open(this.src)" align="right"/></div>' % file_name
                extra.append(pytest_html.extras.html(html))
        report.extra = extra


def _capture_screenshot(name):
    driver.get_screenshot_as_file(name)

def pytest_html_report_title(report):
    report.title = "Automation Report"


def test_warning():
    with pytest.warns(UserWarning):
        warnings.warn("my warning", UserWarning)
