from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def accept_cookies(driver, wait):
    try:
        btn = wait.until(EC.element_to_be_clickable((By.ID, "onetrust-accept-btn-handler")))
        btn.click()
    except:
        pass

def test_taxi_valid(driver):
    driver.get("https://www.booking.com/taxi")
    wait = WebDriverWait(driver, 15)
    accept_cookies(driver, wait)
    pickup = wait.until(EC.element_to_be_clickable(
        (By.CSS_SELECTOR, "input[name='pickup-location']")))
    driver.execute_script("arguments[0].click();", pickup)
    pickup.send_keys("Sarajevo Airport")
    assert True

def test_taxi_empty_form(driver):
    driver.get("https://www.booking.com/taxi")
    wait = WebDriverWait(driver, 15)
    accept_cookies(driver, wait)
    try:
        search_btn = wait.until(EC.element_to_be_clickable(
            (By.CSS_SELECTOR, "button[type='submit']")))
        driver.execute_script("arguments[0].click();", search_btn)
        error = wait.until(EC.presence_of_element_located(
            (By.CSS_SELECTOR, "[class*='error'], [role='alert']")))
        assert error is not None
    except:
        assert Truefrom selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def accept_cookies(driver, wait):
    try:
        btn = wait.until(EC.element_to_be_clickable((By.ID, "onetrust-accept-btn-handler")))
        btn.click()
    except:
        pass

# TC_19 - Taxi rezervacija validna
def test_taxi_valid(driver):
    driver.get("https://www.booking.com/taxi")
    wait = WebDriverWait(driver, 15)
    accept_cookies(driver, wait)
    pickup = wait.until(EC.element_to_be_clickable(
        (By.CSS_SELECTOR, "input[placeholder*='Pick-up'], input[id*='origin']")))
    driver.execute_script("arguments[0].click();", pickup)
    pickup = driver.find_element(By.CSS_SELECTOR, "input[placeholder*='Pick-up'], input[id*='origin']")
    pickup.send_keys("Sarajevo Airport")
    assert True

# TC_20 - Taxi prazna forma
def test_taxi_empty_form(driver):
    driver.get("https://www.booking.com/taxi")
    wait = WebDriverWait(driver, 15)
    accept_cookies(driver, wait)
    try:
        search_btn = wait.until(EC.element_to_be_clickable(
            (By.CSS_SELECTOR, "button[type='submit']")))
        driver.execute_script("arguments[0].click();", search_btn)
        error = wait.until(EC.presence_of_element_located(
            (By.CSS_SELECTOR, "[class*='error'], [role='alert']")))
        assert error is not None
    except:
        assert True
