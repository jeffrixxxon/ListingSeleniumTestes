import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By


def listing_test_1(link):
    database = {'first name': 'Mark', 'last name': 'Shemter', 'email': 'jeffrixxxon@mail.ru'}

    with webdriver.Chrome() as browser:
        browser.get(link)
        for key, val in database.items():
            browser.find_element(By.CSS_SELECTOR, f'input[placeholder*="{key}"]').send_keys(val)
        browser.find_element(By.CSS_SELECTOR, "button.btn").click()
        return browser.find_element(By.TAG_NAME, "h1").text


class MyUnitTestes(unittest.TestCase):
    def test_1(self):
        wait_text = "Congratulations! You have successfully registered!"
        self.assertEqual(listing_test_1('http://suninjuly.github.io/registration1.html'), wait_text)

    def test_2(self):
        wait_text = "Congratulations! You have successfully registered!"
        self.assertEqual(listing_test_1('http://suninjuly.github.io/registration2.html'), wait_text)


if __name__ == "__main__":
    unittest.main()
