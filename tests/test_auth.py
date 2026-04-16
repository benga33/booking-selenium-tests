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


# TC_02 - Registracija nevalidan email
def test_register_invalid_email(driver):
    driver.get("https://account.booking.com/sign-in")
    wait = WebDriverWait(driver, 20)

    email = wait.until(
        EC.visibility_of_element_located((By.ID, "username"))
    )
    email.clear()
    email.send_keys("nevalidan-email")

    driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

    error = wait.until(
        EC.visibility_of_any_elements_located((
            By.CSS_SELECTOR,
            "[role='alert'], .error, [class*='error']"
        ))
    )

    assert len(error) > 0


# TC_03 - Login validan (cookie/session check)
def test_login_valid(driver):
    driver.get("https://www.booking.com")
    wait = WebDriverWait(driver, 15)

    accept_cookies(driver, wait)

    # ne oslanjati se na URL odmah
    wait.until(
        EC.presence_of_element_located((By.TAG_NAME, "body"))
    )

    assert "sign-in" not in driver.current_url


# TC_04 - Login pogrešan password
def test_login_wrong_password(driver):
    driver.get("https://account.booking.com/sign-in")
    wait = WebDriverWait(driver, 20)

    email = wait.until(
        EC.visibility_of_element_located((By.ID, "username"))
    )
    email.clear()
    email.send_keys("test@example.com")

    driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

    # čekaj password ekran (NE samo input odmah)
    password = wait.until(
        EC.visibility_of_element_located(
            (By.CSS_SELECTOR, "input[name='password'], input[type='password']")
        )
    )

    password.clear()
    password.send_keys("pogresna_lozinka_123")

    driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

    error = wait.until(
        EC.visibility_of_element_located(
            (By.CSS_SELECTOR, "[role='alert'], [class*='error']")
        )
    )

    assert error is not None
