from selenium import webdriver
from selenium.webdriver.common.by import By
import time 
import math

link = "http://suninjuly.github.io/find_xpath_form"

try:
    # str1 = str(math.ceil(math.pow(math.pi, math.e) * 10000))

    browser = webdriver.Chrome()
    browser.get(link)

    # link = browser.find_element(By.PARTIAL_LINK_TEXT, str1)
    # link.click()

    input1 = browser.find_element(By.TAG_NAME, 'input')
    input1.send_keys("Tatyana")
    input2 = browser.find_element(By.NAME, 'last_name')
    input2.send_keys("Sergeyeva")
    input3 = browser.find_element(By.CLASS_NAME, 'city')
    input3.send_keys("Tomsk")
    input4 = browser.find_element(By.ID, "country")
    input4.send_keys("Russia")
    button = browser.find_element(By.XPATH, '//button[@type="submit"]')
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла
