import time

from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from PageObject.Base_Page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement


class CartPage(BasePage):
    default_timeout = 5

    def get_url(self) -> str:
        return "http://54.183.112.233/index.php?route=checkout/cart"

    def open_product_page(self, page: str):
        self.driver.get(page)

    def find_qty_field(self) -> WebElement:
        xpath = "//div[@class='form-group']/input[@name='quantity']"
        qty_field = self.driver.find_element(By.XPATH, xpath)

        return qty_field

    def enter_data_to_qty_field(self, number):
        field = self.find_qty_field()
        field.clear()
        field.send_keys(number)

    def find_add_to_cart_button(self) -> WebElement:
        button_id = "button-cart"
        add_to_cart_button = self.driver.find_element(By.ID, button_id)

        return add_to_cart_button

    def click_add_to_cart_button(self):
        self.find_add_to_cart_button().click()

    def get_success_message_after_adding_to_cart(self) -> str:
        xpath = "//div[@class='alert alert-success alert-dismissible']"
        WebDriverWait(self.driver, timeout=self.default_timeout) \
            .until(expected_conditions.presence_of_element_located((By.XPATH, xpath)))
        message = self.driver.find_element(By.XPATH, xpath)

        return message.text[:-2]

    def get_data_from_cart(self) -> list[list]:
        xpath_names = "//table[@class='table table-bordered']/tbody/tr/td[@class='text-left']/a"
        xpath_total_sum = "//table[@class='table table-bordered']/tbody/tr/td[@class='text-right']"
        product_elements = self.driver.find_elements(By.XPATH, xpath_names)
        sum_elements = self.driver.find_elements(By.XPATH, xpath_total_sum)
        total = sum_elements[-1]
        product_names: list[str] = []
        for i in range(len(product_elements)):
            product_names.append(product_elements[i].text)

        return [product_names, total.text]

    def find_remove_product_from_cart_buttons(self) -> list[WebElement]:
        xpath = "//button[@data-original-title='Remove']"
        WebDriverWait(self.driver, timeout=self.default_timeout) \
            .until(expected_conditions.presence_of_all_elements_located((By.XPATH, xpath)))
        remove_buttons = self.driver.find_elements(By.XPATH, xpath)

        return remove_buttons

    def click_remove_product_button(self):
        buttons = self.find_remove_product_from_cart_buttons()
        counter = len(buttons)-1
        for i in range(counter, -1, -1):
            buttons[i].click()
            if i != 0:
                WebDriverWait(self.driver, timeout=self.default_timeout) \
                    .until(expected_conditions.presence_of_all_elements_located((By.XPATH, self.get_remove_from_shopping_cart_button_xpath())))
                buttons = self.find_remove_product_from_cart_buttons()

    def get_success_removed_message(self) -> str:
        xpath = "//div[@id='content']/p"
        WebDriverWait(self.driver, timeout=self.default_timeout) \
            .until(expected_conditions.text_to_be_present_in_element((By.XPATH, xpath), "Your shopping cart is empty!"))
        success_removed_message = self.driver.find_element(By.XPATH, xpath)

        return success_removed_message.text

    def is_cart_page_opened(self) -> bool:
        url = self.driver.current_url
        if url == "http://54.183.112.233/index.php?route=checkout/cart":
            return True
        else:
            return False

    def get_remove_from_shopping_cart_button_xpath(self) -> str:
        return "//button[@data-original-title='Remove']"
