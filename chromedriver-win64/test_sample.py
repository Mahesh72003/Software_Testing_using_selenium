import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
driver = webdriver.Chrome(r'C:\Program Files (x86)\Google\Chrome\Application\chrome.exe'
driver.get('https://www.facebook.com')
time.sleep(5)
driver.quit()