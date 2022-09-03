import os
from selenium import webdriver


def login(username, password, login_url):
    driver = webdriver.Edge()
    driver.minimize_window()
    try:
        driver.get(login_url)
        driver.find_element_by_name("username").send_keys(username)
        driver.find_element_by_name("password").send_keys(password)
        driver.find_element_by_class_name("login100-form-btn").click()
    finally:
        driver.quit()

    if driver is not None:
        driver.quit()


if __name__ == '__main__':
    # Change USERNAME and PASSWORD to your credentials
    USERNAME = "user"
    PASSWORD = "pass"
    LOGIN_URL = "https://net2.sharif.edu/login"
    login(USERNAME, PASSWORD, LOGIN_URL)

