import math
import time
import pytest

from selenium import webdriver
from selenium.webdriver.common.by import By

link = 'http://suninjuly.github.io/alert_accept.html'

@pytest.fixture()
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(3)
    yield driver
    driver.quit()

def test_1(driver):
    # Открыть страницу http://suninjuly.github.io/alert_accept.html
    driver.get(link)

    # Нажать на кнопку
    driver.find_element(By.CSS_SELECTOR,'button.btn').click()

    # Принять confirm
    confirm = driver.switch_to.alert
    confirm.accept()

    # На новой странице решить капчу для роботов, чтобы получить число с ответом
    def calc(N):
        return str(math.log(abs(12 * math.sin(N))))
    x = int(driver.find_element(By.ID,'input_value').text)
    input_answer = driver.find_element(By.ID,'answer').send_keys(calc(x))
    button = driver.find_element(By.TAG_NAME,'button').click()

    text_alert = driver.switch_to.alert.text
    print(text_alert)

    assert driver.switch_to.alert