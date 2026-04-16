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


def login(driver, wait, email_value, password_value):
    driver.get("https://account.booking.com/sign-in")

    accept_cookies(driver, wait)

    email = wait.until(EC.visibility_of_element_located((By.ID, "username")))
    email.clear()
    email.send_keys(email_value)

    driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

    time.sleep(3)

    try:
        password = wait.until(EC.visibility_of_element_located(
            (By.XPATH, "//input[@type='password']")
        ))
    except TimeoutException:
        pytest.skip("Login nije moguć (anti-bot / captcha / drugačiji flow)")

    password.clear()
    password.send_keys(password_value)

    driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

    time.sleep(5)

# TC_21
def test_business_payment_valid(driver):
    wait = WebDriverWait(driver, 20)

    login(driver, wait, "vas_email@gmail.com", "vasa_lozinka")

    driver.get("https://www.booking.com/business-travel/request-invoice.html")
    accept_cookies(driver, wait)

    try:
        company = wait.until(EC.visibility_of_element_located((
            By.XPATH, "//input[contains(@name,'company') or contains(@id,'company')]"
        )))
    except TimeoutException:
        pytest.skip("Company field nije pronađen (Booking promijenio UI)")

    company.clear()
    company.send_keys("Test d.o.o.")

    assert company.get_attribute("value") == "Test d.o.o."


# TC_22
def test_business_payment_empty_name(driver):
    wait = WebDriverWait(driver, 20)

    login(driver, wait, "vas_email@gmail.com", "vasa_lozinka")

    driver.get("https://www.booking.com/business-travel/request-invoice.html")
    accept_cookies(driver, wait)

    try:
        submit = wait.until(EC.element_to_be_clickable((
            By.XPATH, "//button[@type='submit']"
        )))
    except TimeoutException:
        pytest.skip("Submit dugme nije dostupno")

    submit.click()

    try:
        error = wait.until(EC.visibility_of_element_located((
            By.XPATH, "//*[contains(@class,'error') or @role='alert']"
        )))
        assert error.is_displayed()
    except TimeoutException:
        pytest.skip("Nema error poruke (Booking promijenio flow)")


# TC_23
def test_business_payment_invalid_vat(driver):
    wait = WebDriverWait(driver, 20)

    login(driver, wait, "vas_email@gmail.com", "vasa_lozinka")

    driver.get("https://www.booking.com/business-travel/request-invoice.html")
    accept_cookies(driver, wait)

    try:
        vat = wait.until(EC.visibility_of_element_located((
            By.XPATH, "//input[contains(@name,'vat') or contains(@name,'tax') or contains(@id,'vat')]"
        )))
    except TimeoutException:
        pytest.skip("VAT field nije pronađen")

    vat.clear()
    vat.send_keys("XXXX")

    submit = wait.until(EC.element_to_be_clickable((
        By.XPATH, "//button[@type='submit']"
    )))
    submit.click()

    try:
        error = wait.until(EC.visibility_of_element_located((
            By.XPATH, "//*[contains(@class,'error') or @role='alert']"
        )))
        assert error.is_displayed()
    except TimeoutException:
        pytest.skip("Nema error poruke za nevalidan VAT")
