from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


class BasePage:
    driver: WebDriver

    def __init__(self, driver_param: WebDriver):
        self.driver = driver_param

    def get_url(self) -> str:
        raise NotImplementedError

    def open(self):
        self.driver.get(self.get_url())
