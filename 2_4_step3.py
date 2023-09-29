from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import math
import time


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


try:
    browser = webdriver.Chrome()

    browser.get("http://suninjuly.github.io/explicit_wait2.html")

    WebDriverWait(browser, 15).until(
            EC.text_to_be_present_in_element((By.ID, "price"), '100')
        )
    button = browser.find_element(By.CSS_SELECTOR, '#book')
    button.click()

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