from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

import math


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


try:
    browser = webdriver.Chrome()
    link = "https://SunInJuly.github.io/execute_script.html"
    browser.get(link)

    x = browser.find_element(By.CSS_SELECTOR, '#input_value').text
    y = calc(x)

    el1 = browser.find_element(By.CSS_SELECTOR, 'input[id="answer"]')
    el1.send_keys(y)

    el2 = browser.find_element(By.CSS_SELECTOR, 'input[id="robotCheckbox"]')
    browser.execute_script("return arguments[0].scrollIntoView(true);", el2)
    el2.click()

    el3 = browser.find_element(By.CSS_SELECTOR, 'input[id="robotsRule"]')
    browser.execute_script("return arguments[0].scrollIntoView(true);", el3)
    el3.click()

    button = browser.find_element(By.TAG_NAME, "button")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    button.click()
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()