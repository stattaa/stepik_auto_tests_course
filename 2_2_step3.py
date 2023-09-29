from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

import math


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


try:
    link = "https://suninjuly.github.io/selects2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    x1 = browser.find_element(By.CSS_SELECTOR, '#num1').text
    x2 = browser.find_element(By.CSS_SELECTOR, '#num2').text

    select = Select(browser.find_element(By.TAG_NAME, "select"))
    select.select_by_value(str(int(x1) + int(x2)))

    button = browser.find_element(By.XPATH, '//button[@type="submit"]')
    button.click()
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()