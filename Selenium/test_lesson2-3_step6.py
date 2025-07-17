import math

import pytest

from selenium import webdriver
from selenium.webdriver.common.by import By

link_1 = 'http://suninjuly.github.io/redirect_accept.html'
link_2 = 'https://suninjuly.github.io/wait1.html'

@pytest.fixture()
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(3)
    yield driver
    driver.quit()

def test_1(driver):
    # Открыть страницу http://suninjuly.github.io/redirect_accept.html
    driver.get(link_1)

    # Нажать на кнопку
    driver.find_element(By.TAG_NAME,'button').click()
    # Переключиться на новую вкладку
    window_0_button = driver.window_handles[0]
    window_1_form = driver.window_handles[1]
    driver.switch_to.window(window_1_form)

    # Пройти капчу для робота и получить число-ответ
    def calc(n):
        return str(math.log(abs(12 * math.sin(n))))

    x = int(driver.find_element(By.ID,'input_value').text)
    driver.find_element(By.ID,'answer').send_keys(calc(x))

    driver.find_element(By.TAG_NAME,'button').click()

    # Проводим проверку на появления окна уведомления с ключом
    assert driver.switch_to.alert

    key_value = driver.switch_to.alert.text
    print(key_value)

def test_2(driver):
    # Открыть страницу http://suninjuly.github.io/wait1.html
    driver.get(link_2)

    # Нажать на кнопку "Verify"
    driver.find_element(By.ID,'verify').click()

    # Проверить, что появилась надпись "Verification was successful!"
    message = driver.find_element(By.ID,'verify_message').text
    assert message == 'Verification was successful!'
    print(message)