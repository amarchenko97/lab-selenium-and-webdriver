from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from PageObject.Base_Page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement


class ComparePage(BasePage):
    default_timeout = 5

    def get_url(self) -> str:
        return "http://54.183.112.233/index.php?route=product/compare"

    def is_compare_page_loaded(self) -> bool:
        xpath = "//div[@id='content']/h1"
        page_name = self.driver.find_elements(By.XPATH, xpath)
        if page_name:
            return True
        else:
            WebDriverWait(self.driver, timeout=self.default_timeout) \
                .until(expected_conditions.presence_of_all_elements_located((By.XPATH, xpath)))
            return True

    def find_compare_button(self) -> WebElement:
        xpath = "//div[@class='col-sm-4']/div[@class='btn-group']/button[@data-original-title='Compare this Product']"
        WebDriverWait(self.driver, timeout=self.default_timeout) \
            .until(expected_conditions.presence_of_all_elements_located((By.XPATH, xpath)))
        compare_button = self.driver.find_element(By.XPATH, xpath)

        return compare_button

    def click_compare_button(self):
        self.find_compare_button().click()

    def get_success_add_message(self) -> str:
        xpath = "//div[@id='product-product']/div[@class='alert alert-success alert-dismissible']"
        WebDriverWait(self.driver, timeout=self.default_timeout) \
            .until(expected_conditions.presence_of_all_elements_located((By.XPATH, xpath)))
        success_message = self.driver.find_element(By.XPATH, xpath)

        return success_message.text[:-2]

    def open_product_page(self, page: str):
        self.driver.get(page)

    def get_compared_products_names(self) -> list[str]:
        self.is_compare_page_loaded()
        xpath = "//table[@class='table table-bordered']/tbody/tr/td/a/strong"
        WebDriverWait(self.driver, timeout=self.default_timeout) \
            .until(expected_conditions.presence_of_all_elements_located((By.XPATH, xpath)))
        compared_products = self.driver.find_elements(By.XPATH, xpath)
        compared_products_names: list[str] = []
        for product in range(len(compared_products)):
            compared_products_names.append(compared_products[product].text)

        return compared_products_names

    def delete_products_from_compare_list(self):
        xpath = "//table[@class='table table-bordered']/tbody/tr/td/a[@class='btn btn-danger btn-block']"
        WebDriverWait(self.driver, timeout=self.default_timeout) \
            .until(expected_conditions.presence_of_all_elements_located((By.XPATH, xpath)))
        delete_buttons = self.driver.find_elements(By.XPATH, xpath)
        length = len(delete_buttons)-1
        for i in range(length, -1, -1):
            delete_buttons[i].click()
            if i != 0:
                WebDriverWait(self.driver, timeout=self.default_timeout) \
                    .until(expected_conditions.presence_of_all_elements_located((By.XPATH, xpath)))
                delete_buttons = self.driver.find_elements(By.XPATH, xpath)

    def get_empty_compare_list_message(self) -> str:
        xpath = "//div[@id='content']/p"
        WebDriverWait(self.driver, timeout=self.default_timeout) \
            .until(expected_conditions.presence_of_element_located((By.XPATH, xpath)))
        message = self.driver.find_element(By.XPATH, xpath)

        return message.text
