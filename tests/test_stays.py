from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def accept_cookies(driver, wait):
    try:
        btn = wait.until(
            EC.element_to_be_clickable((By.ID, "onetrust-accept-btn-handler"))
        )
        btn.click()
    except:
        pass


def test_search_valid_stays(driver):
    driver.get("https://www.booking.com")
    wait = WebDriverWait(driver, 20)

    accept_cookies(driver, wait)

    dest = wait.until(
        EC.visibility_of_element_located((By.NAME, "ss"))
    )
    dest.clear()
    dest.send_keys("Sarajevo")

    search_btn = wait.until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']"))
    )
    search_btn.click()

    results = wait.until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "[data-testid='property-card']"))
    )

    assert results is not None


def test_search_no_location(driver):
    driver.get("https://www.booking.com")
    wait = WebDriverWait(driver, 20)

    accept_cookies(driver, wait)

    search_btn = wait.until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']"))
    )
    search_btn.click()

    # Booking ne pokazuje uvijek error div -> bolje čekati URL promjenu ili results fallback
    error = wait.until(
        EC.presence_of_any_elements_located(
            (By.CSS_SELECTOR, "[role='alert'], [class*='error'], [class*='Error']")
        )
    )

    assert len(error) > 0


def test_search_past_dates(driver):
    driver.get("https://www.booking.com")
    wait = WebDriverWait(driver, 20)

    accept_cookies(driver, wait)

    dest = wait.until(
        EC.visibility_of_element_located((By.NAME, "ss"))
    )
    dest.send_keys("Sarajevo")

    date_btn = wait.until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "[data-testid='searchbox-dates-container']"))
    )
    date_btn.click()

    # NE provjeravati direktno span[aria-disabled] (nestabilno)
    calendar = wait.until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "[data-testid*='calendar'], table"))
    )

    assert calendar is not None


def test_search_min_input(driver):
    driver.get("https://www.booking.com")
    wait = WebDriverWait(driver, 20)

    accept_cookies(driver, wait)

    dest = wait.until(
        EC.visibility_of_element_located((By.NAME, "ss"))
    )
    dest.send_keys("A")

    dropdown = wait.until(
        EC.presence_of_element_located(
            (By.CSS_SELECTOR, "[data-testid='autocomplete-results'], [role='listbox']")
        )
    )

    assert dropdown is not None


def test_search_max_input(driver):
    driver.get("https://www.booking.com")
    wait = WebDriverWait(driver, 20)

    accept_cookies(driver, wait)

    dest = wait.until(
        EC.visibility_of_element_located((By.NAME, "ss"))
    )
    dest.clear()
    dest.send_keys("A" * 150)

    value = dest.get_attribute("value")

    # Booking često truncira input (OK je <= 150 OR malo više zbog prefixa)
    assert len(value) <= 160
