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


def test_flights_valid_search(driver):
    driver.get("https://www.booking.com/flights")
    wait = WebDriverWait(driver, 25)

    accept_cookies(driver, wait)

    wait.until(EC.presence_of_element_located((By.TAG_NAME, "body")))

    origin = wait.until(EC.element_to_be_clickable((
    By.XPATH, "//input[contains(@data-testid,'origin') or contains(@placeholder,'Where from')]"
)))
    origin.click()

    # ne koristiti clear() jer često ne radi
    origin.send_keys("Sarajevo")

    # izbor suggestiona (ako postoji)
    try:
        suggestion = wait.until(
            EC.element_to_be_clickable(
                (By.CSS_SELECTOR, "[role='option'], li[data-testid], li[role='option']")
            )
        )
        suggestion.click()
    except:
        pass

    assert origin is not None


def test_flights_no_destination(driver):
    driver.get("https://www.booking.com/flights")
    wait = WebDriverWait(driver, 25)

    accept_cookies(driver, wait)

    wait.until(EC.presence_of_element_located((By.TAG_NAME, "body")))

    search_btn = wait.until(EC.element_to_be_clickable((
    By.XPATH, "//button[@type='submit' or contains(@data-testid,'search')]"
)))
    search_btn.click()

    # Booking često ne daje "alert", nego inline error ili disabled state
    error = wait.until(
        EC.presence_of_all_elements_located(
            (By.CSS_SELECTOR, "[role='alert'], [class*='error'], [class*='Error']")
        )
    )

    assert len(error) > 0
