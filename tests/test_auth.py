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

# TC_02 - Registracija nevalidan email
def test_register_invalid_email(driver):
    driver.get("https://www.booking.com")
    wait = WebDriverWait(driver, 15)
    accept_cookies(driver, wait)
    driver.get("https://account.booking.com/sign-in")
    email = wait.until(EC.presence_of_element_located((By.ID, "username")))
    email.send_keys("nevalidan-email")
    btn = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']")))
    driver.execute_script("arguments[0].click();", btn)
    error = wait.until(EC.presence_of_element_located(
        (By.CSS_SELECTOR, "[class*='error'], [class*='Error'], [role='alert']")))
    assert error is not None

# TC_03 - Login validan
def test_login_valid(driver):
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
    wait.until(EC.url_contains("booking.com"))
    assert "sign-in" not in driver.current_url

# TC_04 - Login pogrešan password
def test_login_wrong_password(driver):
    driver.get("https://account.booking.com/sign-in")
    wait = WebDriverWait(driver, 15)
    email = wait.until(EC.presence_of_element_located((By.ID, "username")))
    email.send_keys("vas_email@gmail.com")  # zamijeni
    btn = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']")))
    driver.execute_script("arguments[0].click();", btn)
    password = wait.until(EC.presence_of_element_located((By.ID, "password")))
    password.send_keys("pogresna_lozinka_123")
    btn2 = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']")))
    driver.execute_script("arguments[0].click();", btn2)
    error = wait.until(EC.presence_of_element_located(
        (By.CSS_SELECTOR, "[class*='error'], [role='alert']")))
    assert error is not None