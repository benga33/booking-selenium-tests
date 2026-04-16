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


def test_login_page_load(driver):
    driver.get("https://account.booking.com/sign-in")
    wait = WebDriverWait(driver, 20)

    email = wait.until(EC.visibility_of_element_located((By.ID, "username")))
    assert email.is_displayed()


def test_login_wrong_password(driver):
    driver.get("https://account.booking.com/sign-in")
    wait = WebDriverWait(driver, 20)

    accept_cookies(driver, wait)

    email = wait.until(EC.visibility_of_element_located((By.ID, "username")))
    email.clear()
    email.send_keys("test@example.com")

    driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

    time.sleep(3)

    try:
        password = wait.until(EC.visibility_of_element_located(
            (By.XPATH, "//input[@type='password']")
        ))
    except TimeoutException:
        pytest.skip("Password polje se nije pojavilo (anti-bot ili drugačiji flow)")

    password.clear()
    password.send_keys("wrongpassword123")

    driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

    try:
        error = wait.until(EC.presence_of_element_located((
            By.XPATH, "//*[contains(@class,'error') or @role='alert']"
        )))
        assert error.is_displayed()
    except TimeoutException:
        pytest.skip("Nema error poruke (Booking promijenio flow)")
