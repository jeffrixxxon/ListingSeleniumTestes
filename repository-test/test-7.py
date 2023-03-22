import time
from math import log, sin
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver


def calc(x_):
    return log(abs(12 * sin(int(x_))))


with webdriver.Chrome() as browser:
    browser.get("http://suninjuly.github.io/explicit_wait2.html")

    WebDriverWait(browser, 12).until(
            EC.text_to_be_present_in_element((By.ID, "price"), '$100')
        )

    browser.find_element(By.CSS_SELECTOR, '.btn').click()
    x = browser.find_element(By.CSS_SELECTOR, '[id="input_value"]').text
    browser.find_element(By.CSS_SELECTOR, '[id="answer"]').send_keys(str(calc(x)))
    browser.find_element(By.CSS_SELECTOR, '[id="solve"]').click()
    time.sleep(15)
