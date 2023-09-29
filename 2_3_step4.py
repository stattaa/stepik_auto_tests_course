from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


try:
    link = "http://suninjuly.github.io/alert_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)

    button = browser.find_element(By.XPATH, '//button[@type="submit"]')
    button.click()

    confirm = browser.switch_to.alert
    confirm.accept()

    x = browser.find_element(By.CSS_SELECTOR, '#input_value').text
    y = calc(x)

    el1 = browser.find_element(By.CSS_SELECTOR, '#answer')
    el1.send_keys(y)

    button = browser.find_element(By.XPATH, '//button[@type="submit"]')
    button.click()
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()