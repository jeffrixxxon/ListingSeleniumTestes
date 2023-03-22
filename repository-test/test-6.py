import time
from math import log, sin
from selenium import webdriver
from selenium.webdriver.common.by import By


def calc(x_):
    return log(abs(12 * sin(int(x_))))


try:
    browser = webdriver.Chrome()
    browser.get('http://suninjuly.github.io/alert_accept.html')

    browser.find_element(By.CSS_SELECTOR, ".btn").click()
    alert = browser.switch_to.alert
    alert.accept()
    x = browser.find_element(By.CSS_SELECTOR, '[id="input_value"]').text
    browser.find_element(By.CSS_SELECTOR, '[id="answer"]').send_keys(str(calc(x)))
    browser.find_element(By.CSS_SELECTOR, '.btn').click()

finally:
    time.sleep(15)
    browser.switch_to.alert.accept()
    browser.quit()


if __name__ == "__main__":
    pass
