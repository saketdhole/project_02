from datetime import datetime

import pytest
from selenium import webdriver
import os


@pytest.fixture
def setup(browser):
    if browser=="chrome":
        driver=webdriver.Chrome()
        driver.implicitly_wait(10)
        driver.maximize_window()
        return driver
    elif browser =="edge":
        driver=webdriver.Edge()
        driver.implicitly_wait(10)
        driver.maximize_window()
        return driver
    elif browser =="firefox":
        driver=webdriver.Firefox()
        driver.implicitly_wait(10)
        driver.maximize_window()
        return driver
def pytest_addoption(parser):
    parser.addoption("--browser", default='chrome')

@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")

def pytest_configure(config):
    config._metadata['Project Name'] = 'Open Cart'
    config._metadata['Module Name'] = 'Registration'
    config._metadata['Tester Name'] = 'Saket Dhole'

@pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME", None)
    metadata.pop("Plugins", None)
    metadata.pop("Packages", None)

@pytest.hookimpl(tryfirst=True)
def pytest_configure(config):
    config.option.htmlpath= os.path.abspath(os.curdir)+ "//reports//" + datetime.now().strftime("%d-%m-%Y %H-%M-%S") +".html"