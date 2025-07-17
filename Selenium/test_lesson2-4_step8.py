import pytest
import math

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as EC

link = 'http://suninjuly.github.io/explicit_wait2.html'

@pytest.fixture()
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(5)
    yield driver
    driver.quit()

def test_1(driver):
    # Открыть страницу http://suninjuly.github.io/explicit_wait2.html
    driver.get(link)

    # Дождаться, когда цена дома уменьшится до $100 (ожидание нужно установить не меньше 12 секунд)
    price_100 = wait(driver,5).until(EC.text_to_be_present_in_element((By.ID,'price'),'$100'))

    # Нажать на кнопку "Book"
    button_click = driver.find_element(By.ID,'book').click()

    # Решить уже известную нам математическую задачу (используйте ранее написанный код) и отправить решение
    def calc(n):
        return str(math.log(abs(12 * math.sin(n))))

    x = int(driver.find_element(By.ID,'input_value').text)

    driver.find_element(By.ID,'answer').send_keys(calc(x))

    driver.find_element(By.ID,'solve').click()

    # Выполнить проверку
    assert driver.switch_to.alert

    print(driver.switch_to.alert.text)
