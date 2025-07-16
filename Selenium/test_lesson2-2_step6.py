import math
import time
import pytest

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support.ui import Select

base_url = 'https://suninjuly.github.io/execute_script.html'

@pytest.fixture(scope='session')
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(3)
    yield driver
    driver.quit()

def test_1(driver):
    # Открыть страницу https://SunInJuly.github.io/execute_script.html.
    driver.get(base_url)

    # Считать значение для переменной x.
    x = int(driver.find_element(By.ID,'input_value').text)
    # Посчитать математическую функцию от x.
    def calc(N):
        return math.log(abs(12*math.sin(N)))

    # Проскроллить страницу вниз.
    driver.execute_script('window.scrollBy(0, 100);')

    # Ввести ответ в текстовое поле.
    driver.find_element(By.ID, 'answer').send_keys(str(calc(x)))

    # Выбрать checkbox "I'm the robot".
    driver.find_element(By.ID,'robotCheckbox').click()

    # Переключить radiobutton "Robots rule!".
    driver.find_element(By.ID,'robotsRule').click()

    # Нажать на кнопку "Submit".
    driver.find_element(By.TAG_NAME, 'button').click()

    assert driver.switch_to.alert

    time.sleep(3)