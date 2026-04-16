from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time


def accept_cookies(driver, wait):
    try:
        btn = wait.until(EC.element_to_be_clickable((By.ID, "onetrust-accept-btn-handler")))
        btn.click()
    except TimeoutException:
        print("Cookie button not found")


def login(driver, wait, email_value, password_value):
    driver.get("https://account.booking.com/sign-in")

    email = wait.until(EC.visibility_of_element_located((By.ID, "username")))
    email.clear()
    email.send_keys(email_value)

    driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
    
    time.sleep(3)

    try:
        password = wait.until(EC.visibility_of_element_located(
            (By.XPATH, "//input[@type='password']")
        ))
    except:
        raise Exception("Password polje se nije pojavilo (bot protection ili flow promijenjen)")

    password.send_keys(password_value)

    driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

    time.sleep(5)


# TC_21
def test_business_payment_valid(driver):
    wait = WebDriverWait(driver, 20)

    login(driver, wait, "vas_email@gmail.com", "vasa_lozinka")

    driver.get("https://www.booking.com/business-travel/request-invoice.html")
    accept_cookies(driver, wait)

    company = wait.until(EC.visibility_of_element_located((
        By.XPATH, "//input[contains(@name,'company') or contains(@id,'company')]"
    )))

    company.clear()
    company.send_keys("Test d.o.o.")

    assert company.get_attribute("value") == "Test d.o.o."


# TC_22
def test_business_payment_empty_name(driver):
    wait = WebDriverWait(driver, 20)

    login(driver, wait, "vas_email@gmail.com", "vasa_lozinka")

    driver.get("https://www.booking.com/business-travel/request-invoice.html")
    accept_cookies(driver, wait)

    submit = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']")))
    driver.execute_script("arguments[0].click();", submit)

    error = wait.until(EC.visibility_of_element_located((
        By.XPATH, "//*[contains(@class,'error') or @role='alert']"
    )))

    assert error.is_displayed()


# TC_23
def test_business_payment_invalid_vat(driver):
    wait = WebDriverWait(driver, 20)

    login(driver, wait, "vas_email@gmail.com", "vasa_lozinka")

    driver.get("https://www.booking.com/business-travel/request-invoice.html")
    accept_cookies(driver, wait)

    vat = wait.until(EC.visibility_of_element_located((
        By.XPATH, "//input[contains(@name,'vat') or contains(@name,'tax') or contains(@id,'vat')]"
    )))

    vat.clear()
    vat.send_keys("XXXX")

    submit = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']")))
    driver.execute_script("arguments[0].click();", submit)

    error = wait.until(EC.visibility_of_element_located((
        By.XPATH, "//*[contains(@class,'error') or @role='alert']"
    )))

    assert error.is_displayed()
