import configparser
import time

from selenium import webdriver
import pytest

@pytest.fixture()
def setUp(browser):
    if browser == 'chrome':
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.implicitly_wait(5)
    elif browser == 'firefox':
        driver = webdriver.Firefox()
        driver.maximize_window()
        driver.implicitly_wait(5)
    else:
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.implicitly_wait(5)
    return driver


def pytest_addoption(parser):
    parser.addoption('--browser')

@pytest.fixture()
def browser(request):
    return request.config.getoption('--browser')


##########################PyTest HTML Report######################
"""config = configparser.ConfigParser
def pytest_configure(config):
    config._metadata = {
        "Tester": "Likhith",
        "Project Name": "Tutorial",
    }"""


