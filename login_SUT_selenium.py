import os
from selenium import webdriver
from selenium.webdriver.common.by import By


def login(username, password, login_url, driver):
    driver.minimize_window()
    try:
        driver.get(login_url)
        driver.find_element(by=By.NAME, value='username').send_keys(username)
        driver.find_element(by=By.NAME, value='password').send_keys(password)
        driver.find_element(by=By.CLASS_NAME, value="login100-form-btn").click()
    finally:
        driver.quit()
        quit()

    if driver is not None:
        driver.quit()
        quit()


if __name__ == '__main__':
    # Change USERNAME and PASSWORD to your credentials
    USERNAME = "user"
    PASSWORD = "pass"
    LOGIN_URL = "https://net2.sharif.edu/login"
    OPTIONS = webdriver.EdgeOptions()
    #OPTIONS.add_argument('--disable-gpu')
    OPTIONS.add_argument('--disable-dev-shm-usage')
    OPTIONS.add_experimental_option('excludeSwitches', ['enable-logging'])
    DRIVER = webdriver.Edge(options=OPTIONS)
    login(USERNAME, PASSWORD, LOGIN_URL, DRIVER)
