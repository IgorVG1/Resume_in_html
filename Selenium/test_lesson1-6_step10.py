import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as EC

base_url = 'http://suninjuly.github.io/registration1.html'
base_url2 = 'https://suninjuly.github.io/registration2.html'

@pytest.fixture()
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(3)
    yield driver
    driver.quit()

# Test 1: Регистрация с заполнением только обязательных полей
def test_1(driver):
    try:
        driver.get(base_url)

        input_First_block = driver.find_elements(By.CSS_SELECTOR, 'div.first_block input')
        for input in input_First_block:
            input.send_keys('abc')

        driver.find_element(By.XPATH, '//button[text()="Submit"]').click()

        wait(driver,5).until(EC.visibility_of_element_located((By.TAG_NAME, 'h1')))

        text_actual = driver.find_element(By.TAG_NAME, 'h1').text
        text_passed = 'Congratulations! You have successfully registered!'
        assert text_actual == text_passed

    finally:
        time.sleep(0.5)

# Test 2: Регистрация с заполнением всех полей
def test_2(driver):
    try:
        driver.get(base_url)

        input_First_block = driver.find_elements(By.CSS_SELECTOR, 'div.first_block input')
        input_Second_block = driver.find_elements(By.CSS_SELECTOR, 'div.second_block input')

        for input1 in input_First_block:
            input1.send_keys('abc')

        for input2 in input_Second_block:
            input2.send_keys("123")

        driver.find_element(By.XPATH, '//button[text()="Submit"]').click()

        wait(driver, 5).until(EC.visibility_of_element_located((By.TAG_NAME, 'h1')))

        text_actual = driver.find_element(By.TAG_NAME, 'h1').text
        text_passed = 'Congratulations! You have successfully registered!'
        assert text_actual == text_passed

    finally:
        time.sleep(0.5)

# Test 3: Регистрация с заполнением только необязательных полей
def test_3(driver):
    try:
        driver.get(base_url)

        input_Second_block_ = driver.find_elements(By.CSS_SELECTOR, 'div.second_block input')

        for input2 in input_Second_block_:
            input2.send_keys("123")

        click_button = driver.find_element(By.XPATH, '//button[text()="Submit"]').click()

        assert driver.find_element(By.CSS_SELECTOR, 'div.first_block input.first').is_enabled()

    finally:
        time.sleep(0.5)

# Test 4: Проверка тестовых данных из test_lesson1-6_step11.py
def test_4(driver):
    try:
        driver.get(base_url)

        # Заполняем все поля ввода
        input_First_name = driver.find_element(By.CSS_SELECTOR, '[placeholder="Input your first name"]').send_keys('abc123')
        input_Last_name = driver.find_element(By.CSS_SELECTOR, '[placeholder="Input your last name"]').send_keys('abc123')
        input_Email = driver.find_element(By.CSS_SELECTOR, '[placeholder="Input your email"]').send_keys('abc123')

        # Нажимаем кнопку отправки
        driver.find_element(By.TAG_NAME, 'button').click()

        # Проверка валидности
        wait(driver, 5).until(EC.visibility_of_element_located((By.TAG_NAME, 'h1')))

        text_actual = driver.find_element(By.TAG_NAME, 'h1').text
        text_passed = 'Congratulations! You have successfully registered!'
        assert text_actual == text_passed

    finally:
        time.sleep(2)