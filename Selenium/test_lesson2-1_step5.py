import math
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as EC

base_url = 'https://suninjuly.github.io/math.html'

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(3)

driver.get(base_url)

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

try:
    x = driver.find_element(By.CSS_SELECTOR, 'span#input_value').text
    y = calc(x)

    input_answer = driver.find_element(By.ID, 'answer').send_keys(y)

    # Нажимаем кнопку отправки
    driver.find_element(By.ID, 'robotCheckbox').click()
    driver.find_element(By.ID, 'robotsRule').click()
    driver.find_element(By.CSS_SELECTOR, '[type="submit"]').click()

finally:
    time.sleep(10)
    driver.quit()