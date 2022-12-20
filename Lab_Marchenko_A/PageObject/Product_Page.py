from selenium.webdriver.common.by import By
from PageObject.Base_Page import BasePage


class ProductPage(BasePage):

    def get_url(self) -> str:
        return "http://54.183.112.233/index.php?route=product/product&product_id=42"

    def find_name(self) -> str:
        xpath = "//div[@class='col-sm-4']/h1"
        name = self.driver.find_element(By.XPATH, xpath)

        return name.text

    def find_brand(self) -> str:
        xpath = "//div[@class='col-sm-4']/ul/li/a"
        brand = self.driver.find_element(By.XPATH, xpath)

        return brand.text

    def find_product_code(self) -> str:
        xpath = "//div[@class='col-sm-4']/ul/li[2]"
        product_code = self.driver.find_element(By.XPATH, xpath)

        return product_code.text

    def find_price(self) -> str:
        xpath = "//div[@class='col-sm-4']/ul[2]/li/h2"
        price = self.driver.find_element(By.XPATH, xpath)

        return price.text

    def find_description(self) -> str:
        xpath = "//div[@class='col-sm-8']/div/div/p/font/font[@face='Helvetica']"
        description = self.driver.find_element(By.XPATH, xpath)
        return description.text
