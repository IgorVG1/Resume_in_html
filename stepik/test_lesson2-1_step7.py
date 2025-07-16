import math
import time
import pytest

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert

base_url = 'http://suninjuly.github.io/get_attribute.html'

@pytest.fixture(scope='session')
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(3)
    yield driver
    driver.quit()

def test_1(driver):
    # Открыть страницу
    driver.get(base_url)
    # Найти на ней элемент-картинку, который является изображением сундука с сокровищами
    # Взять у этого элемента значение атрибута valuex, которое является значением x для задачи
    x = driver.find_element(By.ID,'treasure').get_attribute('valuex')

    # Посчитать математическую функцию от x (сама функция остаётся неизменной)
    def calc(N):
        return str(math.log(abs(12 * math.sin(int(N)))))

    # Ввести ответ в текстовое поле
    answer = calc(x)
    driver.find_element(By.ID,'answer').send_keys(answer)
    # Отметить checkbox "I'm the robot"
    driver.find_element(By.ID,'robotCheckbox').click()
    # Выбрать radiobutton "Robots rule!"
    driver.find_element(By.ID,'robotsRule').click()
    # Нажать на кнопку "Submit"
    driver.find_element(By.TAG_NAME,'button').click()

    assert driver.switch_to.alert

    time.sleep(5)