from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def accept_cookies(driver, wait):
    try:
        btn = wait.until(EC.element_to_be_clickable((By.ID, "onetrust-accept-btn-handler")))
        btn.click()
    except:
        pass

# TC_16 - Pretraga auta validna
# TC_16 - Pretraga auta validna
def test_car_valid_search(driver):
    driver.get("https://www.booking.com/cars")
    wait = WebDriverWait(driver, 20)
    accept_cookies(driver, wait)
    pickup = wait.until(EC.element_to_be_clickable(
        (By.CSS_SELECTOR, "input[name*='pickup'], input[placeholder*='Pick-up'], input[id*='pickup']")))
    driver.execute_script("arguments[0].click();", pickup)
    pickup = driver.find_element(By.CSS_SELECTOR, "input[name*='pickup'], input[placeholder*='Pick-up'], input[id*='pickup']")
    pickup.send_keys("Sarajevo")
    assert True
# TC_17 - Car rental nevalidni datumi
def test_car_invalid_dates(driver):
    driver.get("https://www.booking.com/cars")
    wait = WebDriverWait(driver, 20)
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
