import time
from selenium.common import NoSuchElementException
from selenium import webdriver
from selenium.webdriver.common.by import By


def test_link_sel(link: str):
    try:
        browser: webdriver = webdriver.Chrome()
        browser.get(link)
        REQUIRED: list = [
            'Input your first name',
            'Input your last name',
            'Input your email'
        ]

        for el in REQUIRED:
            tag = browser.find_element(By.XPATH, f'//input[@placeholder="{el}"]')
            tag.send_keys(el)

        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()

        time.sleep(1)

        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
        welcome_text = welcome_text_elt.text

        assert "Congratulations! You have successfully registered!" == welcome_text
    except NoSuchElementException as err:
        print(err.msg)

    finally:
        time.sleep(10)
        browser.quit()


if __name__ == "__main__":
    test_link_sel('http://suninjuly.github.io/registration1.html')
    test_link_sel('http://suninjuly.github.io/registration2.html')