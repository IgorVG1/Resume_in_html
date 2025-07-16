from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as EC

base_url = 'https://suninjuly.github.io/registration2.html'

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(3)

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
    driver.quit()