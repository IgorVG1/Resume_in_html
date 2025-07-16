import math
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.implicitly_wait(3)

base_url = 'https://suninjuly.github.io/find_link_text'
shifr = str(math.ceil(math.pow(math.pi, math.e)*10000))

try:
    driver.get(base_url)

    driver.find_element(By.LINK_TEXT, shifr).click()

    input_First_name = driver.find_element(By.NAME, "first_name").send_keys('name')
    input_Last_name = driver.find_element(By.NAME, 'last_name').send_keys('lastname')
    input_City = driver.find_element(By.CLASS_NAME, 'city').send_keys('city')
    input_Country = driver.find_element(By.ID, 'country').send_keys('country')

    driver.find_element(By.CSS_SELECTOR, '[type="submit"]').click()

finally:
    time.sleep(10)
    driver.quit()
