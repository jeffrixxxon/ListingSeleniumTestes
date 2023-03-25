import time
from math import log, sin
from selenium import webdriver
from selenium.webdriver.common.by import By


def calc(x_):
    return log(abs(12 * sin(int(x_))))


with webdriver.Chrome() as browser:
    browser.get('http://suninjuly.github.io/redirect_accept.html')
    browser.find_element(By.CSS_SELECTOR, 'button').click()
    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)
    x = browser.find_element(By.CSS_SELECTOR, '[id="input_value"]').text
    browser.find_element(By.CSS_SELECTOR, '[id="answer"]').send_keys(str(calc(x)))
    browser.find_element(By.CSS_SELECTOR, '.btn').click()
    time.sleep(15)

if __name__ == "__main__":
    pass








