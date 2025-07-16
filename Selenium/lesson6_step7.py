import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.implicitly_wait(3)

base_url = 'http://suninjuly.github.io/huge_form.html'

try:
    driver.get(base_url)
    elements = driver.find_elements(By.TAG_NAME, 'input')
    number = 0

    for element in elements:
        number = number + 1
        element.send_keys(str(number))

    driver.find_element(By.TAG_NAME, 'button').click()

finally:
    time.sleep(30)
    driver.quit()
