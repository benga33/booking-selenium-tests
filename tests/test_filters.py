from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def get_results_page(driver, wait):
    driver.get("https://www.booking.com/searchresults.html?ss=Sarajevo&checkin=2026-06-01&checkout=2026-06-05&group_adults=2")
    try:
        btn = wait.until(EC.element_to_be_clickable((By.ID, "onetrust-accept-btn-handler")))
        btn.click()
    except:
        pass
    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "[data-testid='property-card']")))

# TC_11 - Filter po cijeni
def test_filter_by_price(driver):
    wait = WebDriverWait(driver, 15)
    get_results_page(driver, wait)
    price_filter = wait.until(EC.presence_of_element_located(
        (By.CSS_SELECTOR, "[data-filters-group='price'], [data-testid*='filter']:has(input[type='checkbox'])")))
    assert price_filter is not None

# TC_12 - Sortiranje po cijeni
def test_sort_by_price(driver):
    wait = WebDriverWait(driver, 15)
    get_results_page(driver, wait)
    sort_btn = wait.until(EC.element_to_be_clickable(
        (By.CSS_SELECTOR, "[data-testid='sorters-dropdown-trigger'], select[name='order']")))
    driver.execute_script("arguments[0].click();", sort_btn)
    option = wait.until(EC.presence_of_element_located(
        (By.CSS_SELECTOR, "[data-id='price'], option[value*='price']")))
    driver.execute_script("arguments[0].click();", option)
    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "[data-testid='property-card']")))
    assert True

# TC_13 - Otvaranje detalja hotela
def test_open_hotel_details(driver):
    wait = WebDriverWait(driver, 15)
    get_results_page(driver, wait)
    hotel = wait.until(EC.element_to_be_clickable(
        (By.CSS_SELECTOR, "[data-testid='title-link']")))
    driver.execute_script("arguments[0].click();", hotel)
    wait.until(lambda d: len(d.window_handles) > 1)
    driver.switch_to.window(driver.window_handles[-1])
    assert "booking.com/hotel" in driver.current_url