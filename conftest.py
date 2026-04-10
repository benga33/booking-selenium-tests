import pytest
from selenium import webdriver
import pickle
import os

@pytest.fixture
def driver():
    d = webdriver.Chrome()
    d.implicitly_wait(10)
    d.get("https://www.booking.com")

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
