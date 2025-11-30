import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service


@pytest.fixture
def driver():
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    driver.maximize_window()
    yield driver
    driver.quit()


def login(driver, username, password):
    driver.get("https://www.saucedemo.com/")
    driver.find_element(By.ID, "user-name").send_keys(username)
    driver.find_element(By.ID, "password").send_keys(password)
    driver.find_element(By.ID, "login-button").click()


def test_valid_login(driver):
    login(driver, "standard_user", "secret_sauce")
    assert "inventory" in driver.current_url


def test_invalid_login(driver):
    login(driver, "wrong_pass", "wrong_pass")
    error = driver.find_element(By.CSS_SELECTOR, '[data-test="error"]')
    assert error.is_displayed()


def test_add_to_cart(driver):
    login(driver, "standard_user", "secret_sauce")
    driver.find_element(By.CSS_SELECTOR, '[data-test="add-to-cart-sauce-labs-backpack"]').click()
    badge = driver.find_element(By.CLASS_NAME, "shopping_cart_badge")
    assert badge.text == "1"


def test_checkout(driver):
    login(driver, "visual_user", "secret_sauce")
    driver.find_element(By.CSS_SELECTOR, '[data-test="add-to-cart-sauce-labs-backpack"]').click()
    driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
    driver.find_element(By.CSS_SELECTOR, '[data-test="checkout"]').click()
    driver.find_element(By.CSS_SELECTOR, '[data-test="firstName"]').send_keys("Jan")
    driver.find_element(By.CSS_SELECTOR, '[data-test="lastName"]').send_keys("Niscak")
    driver.find_element(By.CSS_SELECTOR, '[data-test="postalCode"]').send_keys("12345")
    driver.find_element(By.CSS_SELECTOR, '[data-test="continue"]').click()
    driver.find_element(By.CSS_SELECTOR, '[data-test="finish"]').click()
    complete = driver.find_element(By.CLASS_NAME, "complete-header")
    assert "Thank you for your order!" in complete.text
