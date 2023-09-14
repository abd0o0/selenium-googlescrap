import logging
import pickle
import random
import time

from selenium import webdriver
from selenium.common import exceptions
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait


class Driver(webdriver.Remote):

    def __init__(self):
        options = webdriver.ChromeOptions()
        #options.add_argument("user-data-dir=C:\\Users\\Nutzer\\AppData\\Local\\Google\\Chrome\\User Data\\profile 2")

        options.add_experimental_option("useAutomationExtension",
                                        False)  # Adding Argument to Not Use Automation Extension
        options.add_experimental_option("excludeSwitches", ["enable-automation"])  # Excluding enable-automation Switch
        options.add_argument("disable-popup-blocking")
        options.add_argument("disable-notifications")
        options.add_argument("disable-gpu")
      #  options.add_argument("--lang=en")
        desiredCapabilities = {
            "browserName": "chrome"
        }
        webdriver.Remote.__init__(self, command_executor='http://localhost:4444/wd/hub',desired_capabilities = desiredCapabilities, options=options)

    '''

    it will returns the cookies as a list

    '''

    def get_all_cookies(self) -> list:
        return self.get_cookies()

    '''
    add cookies to the driver, takes 1 parameter which are the cookies
    '''

    def add_all_cookies(self, cookies):
        for cookie in cookies:
            try:
                self.add_cookie(cookie)
            except exceptions.InvalidCookieDomainException as e:
                print(e.msg)
        print('Cookies added successfully')

    def safe_find(self, by, attribute, value):
        try:
            return self.find_element(By.XPATH,
                                     '//{by}[@{attribute}="{value}"]'.format(by=by, attribute=attribute, value=value))
        except exceptions.NoSuchElementException or exceptions.ElementNotVisibleException as e:
            return False

    def wait_find(self, by, attribute, value):
        try:
            el = WebDriverWait(self, 10).until(lambda d: self.find_element(By.XPATH,
                                                                           '//{by}[{attribute}="{value}"]'.format(
                                                                               by=by, attribute=attribute,
                                                                               value=value)))
            return el
        except exceptions.TimeoutException as e:
            print(e.msg)
            print()
            return False

    def wait_find_elements(self, by, attribute, value):
        try:
            el = WebDriverWait(self, 10).until(lambda d: self.find_elements(By.XPATH,
                                                                           '//{by}[@{attribute}="{value}"]'.format(
                                                                               by=by, attribute=attribute,
                                                                               value=value)))
            return el
        except exceptions.TimeoutException as e:
            print(e.msg)
            return False

    def go_to(self, element):
        webdriver.ActionChains(self).move_to_element(element).perform()

    def move_by_offset(self, x_offset, y_offset):
        webdriver.ActionChains(self).scroll(0, 0, x_offset, y_offset).perform()
