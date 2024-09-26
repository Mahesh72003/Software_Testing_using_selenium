from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
import time

def setup_driver():
    driver = webdriver.Chrome()  # Make sure to have chromedriver installed and in PATH
    driver.implicitly_wait(10)
    return driver

def test_homepage_load(driver):
    driver.get('https://www.zomato.com/')
    assert "Zomato" in driver.title
    print("Homepage loaded successfully.")

def test_search_restaurant(driver):
    driver.get('https://www.zomato.com/')
    search_box = driver.find_element(By.NAME, 'q')
    search_box.send_keys("Pizza")
    search_box.send_keys(Keys.RETURN)
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//div[@class="result"]')))
    print("Search functionality is working.")

def test_view_restaurant_details(driver):
    driver.get('https://www.zomato.com/')
    search_box = driver.find_element(By.NAME, 'q')
    search_box.send_keys("Pizza")
    search_box.send_keys(Keys.RETURN)
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//div[@class="result"]')))
    first_restaurant = driver.find_element(By.XPATH, '//div[@class="result"]//a')
    first_restaurant.click()
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//div[@class="restaurant-details"]')))
    print("Restaurant details are visible.")

def test_user_registration(driver):
    driver.get('https://www.zomato.com/')
    login_button = driver.find_element(By.XPATH, '//a[text()="Login"]')
    login_button.click()
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//a[text()="Sign Up"]')))
    sign_up_button = driver.find_element(By.XPATH, '//a[text()="Sign Up"]')
    sign_up_button.click()
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, 'name')))
    name_field = driver.find_element(By.NAME, 'name')
    email_field = driver.find_element(By.NAME, 'email')
    password_field = driver.find_element(By.NAME, 'password')
    name_field.send_keys('Test User')
    email_field.send_keys('testuser@example.com')
    password_field.send_keys('password123')
    submit_button = driver.find_element(By.XPATH, '//button[text()="Sign Up"]')
    submit_button.click()
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//a[text()="Profile"]')))
    print("User registration successful.")

def test_user_login(driver):
    driver.get('https://www.zomato.com/')
    login_button = driver.find_element(By.XPATH, '//a[text()="Login"]')
    login_button.click()
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, 'email')))
    email_field = driver.find_element(By.NAME, 'email')
    password_field = driver.find_element(By.NAME, 'password')
    email_field.send_keys('testuser@example.com')  # Replace with actual registered email
    password_field.send_keys('password123')  # Replace with actual registered password
    submit_button = driver.find_element(By.XPATH, '//button[text()="Login"]')
    submit_button.click()
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//a[text()="Profile"]')))
    print("User login successful.")

def run_tests():
    driver = setup_driver()
    try:
        test_homepage_load(driver)
        test_search_restaurant(driver)
        test_view_restaurant_details(driver)
        test_user_registration(driver)
        test_user_login(driver)
    finally:
        driver.quit()

if __name__ == "__main__":
    run_tests()
