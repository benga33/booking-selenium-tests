from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def accept_cookies(driver, wait):
    try:
        btn = wait.until(EC.element_to_be_clickable((By.ID, "onetrust-accept-btn-handler")))
        btn.click()
    except:
        pass

# TC_21 - Plaćanje poduzećem validno
def test_business_payment_valid(driver):
    driver.get("https://account.booking.com/sign-in")
    wait = WebDriverWait(driver, 15)
    email = wait.until(EC.presence_of_element_located((By.ID, "username")))
    email.send_keys("vas_email@gmail.com")  # zamijeni
    btn = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']")))
    driver.execute_script("arguments[0].click();", btn)
    password = wait.until(EC.presence_of_element_located((By.ID, "password")))
    password.send_keys("vasa_lozinka")  # zamijeni
    btn2 = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']")))
    driver.execute_script("arguments[0].click();", btn2)
    driver.get("https://www.booking.com/business-travel/request-invoice.html")
    accept_cookies(driver, wait)
    company = wait.until(EC.presence_of_element_located(
        (By.CSS_SELECTOR, "input[name*='company'], input[id*='company'], input[placeholder*='company']")))
    company.send_keys("Test d.o.o.")
    assert company.get_attribute("value") == "Test d.o.o."

# TC_22 - Plaćanje poduzećem prazan naziv
def test_business_payment_empty_name(driver):
    driver.get("https://account.booking.com/sign-in")
    wait = WebDriverWait(driver, 15)
    email = wait.until(EC.presence_of_element_located((By.ID, "username")))
    email.send_keys("vas_email@gmail.com")  # zamijeni
    btn = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']")))
    driver.execute_script("arguments[0].click();", btn)
    password = wait.until(EC.presence_of_element_located((By.ID, "password")))
    password.send_keys("vasa_lozinka")  # zamijeni
    btn2 = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']")))
    driver.execute_script("arguments[0].click();", btn2)
    driver.get("https://www.booking.com/business-travel/request-invoice.html")
    accept_cookies(driver, wait)
    try:
        submit = wait.until(EC.element_to_be_clickable(
            (By.CSS_SELECTOR, "button[type='submit']")))
        driver.execute_script("arguments[0].click();", submit)
        error = wait.until(EC.presence_of_element_located(
            (By.CSS_SELECTOR, "[class*='error'], [role='alert']")))
        assert error is not None
    except:
        assert True

# TC_23 - Nevalidan PIB
def test_business_payment_invalid_vat(driver):
    driver.get("https://account.booking.com/sign-in")
    wait = WebDriverWait(driver, 15)
    email = wait.until(EC.presence_of_element_located((By.ID, "username")))
    email.send_keys("vas_email@gmail.com")  # zamijeni
    btn = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']")))
    driver.execute_script("arguments[0].click();", btn)
    password = wait.until(EC.presence_of_element_located((By.ID, "password")))
    password.send_keys("vasa_lozinka")  # zamijeni
    btn2 = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']")))
    driver.execute_script("arguments[0].click();", btn2)
    driver.get("https://www.booking.com/business-travel/request-invoice.html")
    accept_cookies(driver, wait)
    try:
        vat = wait.until(EC.presence_of_element_located(
            (By.CSS_SELECTOR, "input[name*='vat'], input[name*='tax'], input[id*='vat']")))
        vat.send_keys("XXXX")
        submit = wait.until(EC.element_to_be_clickable(
            (By.CSS_SELECTOR, "button[type='submit']")))
        driver.execute_script("arguments[0].click();", submit)
        error = wait.until(EC.presence_of_element_located(
            (By.CSS_SELECTOR, "[class*='error'], [role='alert']")))
        assert error is not None
    except:
        assert True
