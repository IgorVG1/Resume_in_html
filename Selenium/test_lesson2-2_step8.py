import os
import time
import pytest

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support.ui import Select


link = 'https://suninjuly.github.io/file_input.html'

@pytest.fixture(scope='session')
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(3)
    yield driver
    driver.quit()

def test_1(driver):
    # Открыть страницу http: // suninjuly.github.io / file_input.html
    driver.get(link)

    # Заполнить текстовые поля: имя, фамилия, email
    driver.find_element(By.NAME,'firstname').send_keys('Igor')
    driver.find_element(By.NAME,'lastname').send_keys('Tester')
    driver.find_element(By.NAME,'email').send_keys('mail.ru')

    # Загрузить файл.
    file_path = "C:\\Users\\PCBOOST\\PycharmProjects\\stepik\\add_files\\file_0.txt"
    input_file = driver.find_element(By.ID,'file')
    #input_file.click()
    input_file.send_keys(file_path)

    # Нажать кнопку "Submit"
    driver.find_element(By.TAG_NAME,'button').click()

    assert driver.switch_to.alert

    time.sleep(3)