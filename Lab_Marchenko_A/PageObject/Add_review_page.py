from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from PageObject.Base_Page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement


class AddReviewPage(BasePage):

    default_timeout = 5

    def get_url(self) -> str:
        return "http://54.183.112.233/index.php?route=product/product&product_id=42"

    def find_reviews_tab(self) -> WebElement:
        xpath = "//div[@class='col-sm-8']/ul[@class='nav nav-tabs']/li/a[@href='#tab-review']"
        WebDriverWait(self.driver, timeout=self.default_timeout) \
            .until(expected_conditions.presence_of_element_located((By.XPATH, xpath)))
        reviews_tab = self.driver.find_element(By.XPATH, xpath)

        return reviews_tab

    def open_reviews_tab(self):
        self.find_reviews_tab().click()

    def find_button_review(self) -> WebElement:
        button_id = "button-review"
        WebDriverWait(self.driver, timeout=self.default_timeout) \
            .until(expected_conditions.presence_of_element_located((By.ID, button_id)))
        button_review = self.driver.find_element(By.ID, button_id)

        return button_review

    def click_button_review(self):
        self.find_button_review().click()

    def get_alert_message(self) -> str:
        xpath = "//div[@id='tab-review']/form[@id='form-review']/div[@class='alert alert-danger alert-dismissible']"
        WebDriverWait(self.driver, timeout=self.default_timeout) \
            .until(expected_conditions.text_to_be_present_in_element((By.XPATH, xpath),
                                                                     "Warning: Please select a review rating!"))
        alert_message = self.driver.find_element(By.XPATH, xpath)

        return alert_message.text

    def find_rating(self) -> WebElement:
        xpath = "//div[@class='col-sm-12']/input[@value='5']"
        rating_button = self.driver.find_element(By.XPATH, xpath)

        return rating_button

    def click_rating(self):
        self.find_rating().click()

    def find_your_name(self) -> WebElement:
        xpath = "//div[@class='col-sm-12']/input[@name='name']"
        your_name = self.driver.find_element(By.XPATH, xpath)

        return your_name

    def enter_name(self, name):
        self.find_your_name().send_keys(name)

    def find_your_review(self) -> WebElement:
        xpath = "//div[@class='col-sm-12']/textarea[@name='text']"
        WebDriverWait(self.driver, timeout=self.default_timeout) \
            .until(expected_conditions.presence_of_element_located((By.XPATH, xpath)))
        your_review = self.driver.find_element(By.XPATH, xpath)

        return your_review

    def enter_your_review(self, review):
        self.find_your_review().clear()
        self.find_your_review().send_keys(review)

    def get_warning_less_symbols(self) -> str:
        xpath = "//div[@id='tab-review']/form[@id='form-review']/div[@class='alert alert-danger alert-dismissible']"
        WebDriverWait(self.driver, timeout=self.default_timeout) \
            .until(expected_conditions.text_to_be_present_in_element((By.XPATH, xpath),
                                                                     "Warning: Review Text must be between 25 and 1000 characters!"))
        warning_less_symbols = self.driver.find_element(By.XPATH, xpath)

        return warning_less_symbols.text

    def get_success_message(self) -> str:
        xpath = "//div[@id='tab-review']/form[@id='form-review']/div[@class='alert alert-success alert-dismissible']"
        WebDriverWait(self.driver, timeout=self.default_timeout) \
            .until(expected_conditions.presence_of_element_located((By.XPATH, xpath)))
        success_message = self.driver.find_element(By.XPATH, xpath)

        return success_message.text
