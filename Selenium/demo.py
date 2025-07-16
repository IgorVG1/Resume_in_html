from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
link = "https://suninjuly.github.io/execute_script.html"
driver.get(link)
button = driver.find_element(By.TAG_NAME, "button")
#driver.execute_script('return arguments[0].scrollIntoView();',button)
driver.execute_script("window.scrollBy(0, 100);")
#button.click()

time.sleep(3)