from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def accept_cookies(driver, wait):
    try:
        btn = wait.until(EC.element_to_be_clickable(
            (By.ID, "onetrust-accept-btn-handler")))
        btn.click()
    except:
        pass

# TC_06 - Pretraga validna
def test_search_valid_stays(driver):
    driver.get("https://www.booking.com")
    wait = WebDriverWait(driver, 15)
    accept_cookies(driver, wait)
    dest = wait.until(EC.presence_of_element_located((By.NAME, "ss")))
    dest.clear()
    dest.send_keys("Sarajevo")
    search_btn = wait.until(EC.element_to_be_clickable(
        (By.CSS_SELECTOR, "button[type='submit']")))
    driver.execute_script("arguments[0].click();", search_btn)
    results = wait.until(EC.presence_of_element_located(
        (By.CSS_SELECTOR, "[data-testid='property-card']")))
    assert results is not None

# TC_07 - Pretraga bez lokacije
def test_search_no_location(driver):
    driver.get("https://www.booking.com")
    wait = WebDriverWait(driver, 15)
    accept_cookies(driver, wait)
    search_btn = wait.until(EC.element_to_be_clickable(
        (By.CSS_SELECTOR, "button[type='submit']")))
    driver.execute_script("arguments[0].click();", search_btn)
    error = wait.until(EC.presence_of_element_located(
        (By.CSS_SELECTOR, "[class*='error'], [data-testid*='error'], [class*='Error']")))
    assert error is not None

# TC_08 - Pretraga sa prošlim datumima
def test_search_past_dates(driver):
    driver.get("https://www.booking.com")
    wait = WebDriverWait(driver, 15)
    accept_cookies(driver, wait)
    dest = wait.until(EC.presence_of_element_located((By.NAME, "ss")))
    dest.clear()
    dest.send_keys("Sarajevo")
    date_btn = wait.until(EC.element_to_be_clickable(
        (By.CSS_SELECTOR, "[data-testid='searchbox-dates-container']")))
    driver.execute_script("arguments[0].click();", date_btn)
    past_day = wait.until(EC.presence_of_element_located(
        (By.CSS_SELECTOR, "[data-date] [aria-disabled='true'], .bui-calendar__date--disabled")))
    assert past_day is not None

# TC_09 - Minimalan unos
def test_search_min_input(driver):
    driver.get("https://www.booking.com")
    wait = WebDriverWait(driver, 15)
    accept_cookies(driver, wait)
    dest = wait.until(EC.presence_of_element_located((By.NAME, "ss")))
    dest.clear()
    dest.send_keys("A")
    dropdown = wait.until(EC.presence_of_element_located(
        (By.CSS_SELECTOR, "[data-testid='autocomplete-results'], [class*='autocomplete']")))
    assert dropdown is not None

# TC_10 - Maksimalan unos
def test_search_max_input(driver):
    driver.get("https://www.booking.com")
    wait = WebDriverWait(driver, 15)
    accept_cookies(driver, wait)
    dest = wait.until(EC.presence_of_element_located((By.NAME, "ss")))
    dest.clear()
    dest.send_keys("A" * 150)
    value = dest.get_attribute("value")
    assert len(value) <= 150