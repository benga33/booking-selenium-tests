import pytest
from selenium import webdriver
import pytest
from selenium import webdriver
import pickle
import os

@pytest.fixture
def driver():
    d = webdriver.Chrome()
    d.implicitly_wait(10)
    d.get("https://www.booking.com")
    
    # Učitaj cookies ako postoje
    if os.path.exists("cookies.pkl"):
        cookies = pickle.load(open("cookies.pkl", "rb"))
        for cookie in cookies:
            try:
                d.add_cookie(cookie)
            except:
                pass
        d.refresh()
    
    yield d
    d.quit()
@pytest.fixture
def driver():
    d = webdriver.Chrome()
    d.implicitly_wait(10)
    yield d
    d.quit()
