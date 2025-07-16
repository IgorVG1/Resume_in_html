import time
import pytest

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support.ui import Select

base_url = 'https://suninjuly.github.io/selects1.html'

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

    # Посчитать сумму заданных чисел
    a = int(driver.find_element(By.ID,'num1').text)
    b = int(driver.find_element(By.ID,'num2').text)
    sum = a + b
    # Выбрать в выпадающем списке значение равное расчитанной сумме
    Select(driver.find_element(By.ID,'dropdown')).select_by_visible_text(str(sum))

    # Нажать кнопку "Submit"
    driver.find_element(By.TAG_NAME,'button').click()

    assert driver.switch_to.alert

    time.sleep(5)
