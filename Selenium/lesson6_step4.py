import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.implicitly_wait(3)

try:
    driver.get('https://suninjuly.github.io/simple_form_find_task.html')

    input_First_name = driver.find_element(By.NAME, "first_name").send_keys('name')
    input_Last_name = driver.find_element(By.NAME, 'last_name').send_keys('lastname')
    input_City = driver.find_element(By.CLASS_NAME, 'city').send_keys('city')
    input_Country = driver.find_element(By.ID, 'country').send_keys('country')

    driver.find_element(By.ID, 'submit_button').click()

finally:
    time.sleep(10)
    driver.quit()
