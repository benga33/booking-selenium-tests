from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# TC_18 - Pretraga atrakcija
def test_attractions_search(driver):
    driver.get("https://www.booking.com/attractions")
    wait = WebDriverWait(driver, 15)
    try:
        btn = wait.until(EC.element_to_be_clickable((By.ID, "onetrust-accept-btn-handler")))
        btn.click()
    except:
        pass
    search = wait.until(EC.presence_of_element_located(
        (By.CSS_SELECTOR, "input[type='search'], input[placeholder*='Search'], input[name*='search']")))
    search.clear()
    search.send_keys("Sarajevo")
    driver.execute_script("arguments[0].form.submit();", search)
    results = wait.until(EC.presence_of_element_located(
        (By.CSS_SELECTOR, "[data-testid*='card'], [class*='card'], [class*='result']")))
    assert results is not None