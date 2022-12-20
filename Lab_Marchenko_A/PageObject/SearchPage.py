from selenium.common import NoSuchElementException
from selenium.webdriver.chrome import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from PageObject.Base_Page import BasePage


class SearchPage(BasePage):

    def get_url(self) -> str:
        return "http://54.183.112.233/index.php?route=product/search"

    def find_search_field(self) -> WebElement:
        search_field = self.driver.find_element(By.ID, "input-search")

        return search_field

    def input_to_search_field(self, search_request):
        self.find_search_field()
        self.find_search_field().clear()
        self.find_search_field().send_keys(search_request)

    def find_search_button(self) -> WebElement:
        search_button = self.driver.find_element(By.ID, "button-search")

        return search_button

    def click_search_button(self):
        self.find_search_button().click()

    def find_product_details(self) -> list:
        product_details: list[str] = []
        xpath_name = "//div[@class='caption']/h4/a"
        xpath_new_price = "//p[@class='price']/span[@class='price-new']"
        xpath_price = "//div[@class='caption']/p[class='price']"

        name = self.driver.find_element(By.XPATH, xpath_name).text

        if self.check_exists_by_xpath(xpath_price):
            price = self.driver.find_element(By.XPATH, xpath_price).text
        else:
            price = self.driver.find_element(By.XPATH, xpath_new_price).text

        product_details.append(name)
        product_details.append(price)

        return product_details

    def check_exists_by_xpath(self, xpath) -> bool:
        try:
            self.driver.find_element(By.XPATH, xpath)
        except NoSuchElementException:
            return False
        return True

    def find_message(self) -> str:
        xpath = "//div[@class='col-sm-12']/p[2]"
        message = self.driver.find_element(By.XPATH, xpath)

        return message.text

    def find_option(self) -> WebElement:
        xpath = "//div[@class='col-sm-12']/p/label[@class='checkbox-inline']/input[@id='description']"
        option_check_box = self.driver.find_element(By.XPATH, xpath)

        return option_check_box

    def check_option(self):
        self.find_option()
        self.find_option().click()

    def find_several_products(self) -> tuple[str, str]:
        xpath = "//div[@class='row']/div/div[@class='product-thumb']/div/div[@class='caption']/h4/a"
        products: list[WebElement] = self.driver.find_elements(By.XPATH, xpath)
        first, second = products
        return first.text, second.text
