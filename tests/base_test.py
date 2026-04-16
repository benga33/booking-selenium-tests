from selenium import webdriver

def create_driver():
    desired_caps = {
        "browserName": "Chrome",
        "browserVersion": "latest",
        "LT:Options": {
            "platformName": "Windows 10",
            "user": "<TVOJ_USERNAME>",
            "accessKey": "<TVOJ_ACCESS_KEY>",
            "video": True,
            "visual": True,
            "network": True,
            "console": True,
            "build": "Booking Python Tests",
            "name": "Test Execution"
        }
    }

    driver = webdriver.Remote(
        command_executor="https://hub.lambdatest.com/wd/hub",
        desired_capabilities=desired_caps
    )

    return driver
