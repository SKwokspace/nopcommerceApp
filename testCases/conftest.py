import pytest
from selenium.webdriver import Chrome


@pytest.fixture()
def setup():
    driver = Chrome(r'C:\Users\MohanMadhuri\Desktop\training\chromedriver.exe')
    return driver
