import pytest
from selenium import webdriver
import pickle
import os

LT_USERNAME = "quandalenottrippin"
LT_ACCESS_KEY = "LT_28vgXKTx7CgtfKOWwYuA4x8Njm5jlOTK1U9x1UNGYEAYDtw"

@pytest.fixture
def driver(request):
    test_name = request.node.name

    lt_options = {
        "user": LT_USERNAME,
        "accessKey": LT_ACCESS_KEY,
        "build": "Booking Selenium Tests",
        "name": test_name,
        "platformName": "Windows 11",
        "browserName": "Chrome",
        "browserVersion": "latest",
        "video": True,
        "selenium_version": "4.0.0"
    }

    options = webdriver.ChromeOptions()
    options.add_argument("--disable-blink-features=AutomationControlled")
    options.set_capability("LT:Options", lt_options)

    d = webdriver.Remote(
        command_executor="https://hub.lambdatest.com/wd/hub",
        options=options
    )

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
