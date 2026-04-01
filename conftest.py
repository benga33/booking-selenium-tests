import pytest
from selenium import webdriver

@pytest.fixture
def driver():
    d = webdriver.Chrome()
    d.implicitly_wait(10)
    yield d
    d.quit()