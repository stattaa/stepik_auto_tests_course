from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os

try:
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Ваш код, который заполняет обязательные поля
    input1 = browser.find_element(By.CSS_SELECTOR, 'input[name="firstname"]')
    input1.send_keys("Tatyana")
    input2 = browser.find_element(By.CSS_SELECTOR, 'input[name="lastname"]')
    input2.send_keys("Sergeyeva")
    input3 = browser.find_element(By.CSS_SELECTOR, 'input[name="email"]')
    input3.send_keys("Tatyana@mail.com")

    input4 = browser.find_element(By.CSS_SELECTOR, 'input[type=file]')
    current_dir = os.path.abspath(os.path.dirname(__file__))  # получаем путь к директории текущего исполняемого файла
    file_path = os.path.join(current_dir, 'doc1.txt')  # добавляем к этому пути имя файла
    input4.send_keys(file_path)
    # Отправляем заполненную форму
    button = browser.find_element(By.XPATH, '//button[@type="submit"]')
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()