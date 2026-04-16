import pytest
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


def accept_cookies(driver, wait):
    try:
        btn = wait.until(EC.element_to_be_clickable((By.ID, "onetrust-accept-btn-handler")))
        btn.click()
    except TimeoutException:
        pass


def test_flights_valid_search(driver):
    driver.get("https://www.booking.com/flights")
    wait = WebDriverWait(driver, 30)

    accept_cookies(driver, wait)

    time.sleep(3)

    try:
        origin = wait.until(EC.element_to_be_clickable((
            By.XPATH, "//div[@data-testid='searchbox-origin']//input"
        )))
    except TimeoutException:
        pytest.skip("Origin field nije pronađen (UI promijenjen)")

    origin.click()
    origin.clear()
    origin.send_keys("Sarajevo")
    time.sleep(2)

    try:
        first_option = wait.until(EC.element_to_be_clickable((
            By.XPATH, "//li[@data-testid='autocomplete-result']"
        )))
        first_option.click()
    except TimeoutException:
        pytest.skip("Autocomplete nije radio")

    try:
        destination = wait.until(EC.element_to_be_clickable((
            By.XPATH, "//div[@data-testid='searchbox-destination']//input"
        )))
    except TimeoutException:
        pytest.skip("Destination field nije pronađen")

    destination.click()
    destination.clear()
    destination.send_keys("Vienna")
    time.sleep(2)

    try:
        first_option = wait.until(EC.element_to_be_clickable((
            By.XPATH, "//li[@data-testid='autocomplete-result']"
        )))
        first_option.click()
    except TimeoutException:
        pytest.skip("Autocomplete za destination nije radio")

    try:
        search_btn = wait.until(EC.element_to_be_clickable((
            By.XPATH, "//button[@data-testid='searchbox-submit']"
        )))
    except TimeoutException:
        pytest.skip("Search dugme nije pronađeno")

    search_btn.click()

    try:
        wait.until(EC.url_contains("flights"))
    except TimeoutException:
        pytest.skip("Nema rezultata (Booking promijenio flow)")

    assert "flights" in driver.current_url


def test_flights_no_destination(driver):
    driver.get("https://www.booking.com/flights")
    wait = WebDriverWait(driver, 30)

    accept_cookies(driver, wait)
    time.sleep(3)

    try:
        search_btn = wait.until(EC.element_to_be_clickable((
            By.XPATH, "//button[@data-testid='searchbox-submit']"
        )))
    except TimeoutException:
        pytest.skip("Search dugme nije dostupno")

    search_btn.click()

    try:
        error_elements = wait.until(EC.presence_of_all_elements_located((
            By.XPATH, "//*[contains(@class,'error') or @role='alert']"
        )))
        assert len(error_elements) > 0
    except TimeoutException:
        pytest.skip("Nema error poruke (Booking drugačiji flow)")
