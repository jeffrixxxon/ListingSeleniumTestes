import os
import time
from selenium.webdriver.common.by import By
from selenium import webdriver


def sel_browser_pars():
    try:
        current_dir = os.path.abspath(os.path.dirname(__file__))
        file_path = os.path.join(current_dir, 'file.txt')
        os.mkdir(file_path)
        fields = {'firstname': 'Mark', 'lastname': 'Shemter', 'email': 'jeffrixxxon@mail.ru'}

        browser = webdriver.Chrome()
        browser.get('http://suninjuly.github.io/file_input.html')

        [browser.find_element(By.CSS_SELECTOR, f'[name="{key}"]'
                              ).send_keys(val) for key, val in fields.items()]

        element = browser.find_element(By.CSS_SELECTOR, '[type="file"]')
        element.send_keys(file_path)
        browser.find_element(By.CSS_SELECTOR, 'button.btn').click()
    finally:
        time.sleep(15)
        browser.quit()


def main():
    sel_browser_pars()


if __name__ == "__main__":
    main()
