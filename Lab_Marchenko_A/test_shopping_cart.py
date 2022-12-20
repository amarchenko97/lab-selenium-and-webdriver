import unittest

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from PageObject.Shopping_cart_Page import CartPage


class ShoppingCartTest(unittest.TestCase):
    driver = None
    cartPage = None
    expected_data: list[list[str]] = [["Samsung SyncMaster 941BW", "HP LP3065"], "$606.00"]

    @classmethod
    def setUpClass(cls) -> None:
        options = Options()
        options.add_argument("--disable-smooth-scrolling")
        cls.driver = webdriver.Chrome(
            options=options,
            service=Service(ChromeDriverManager().install())
        )
        cls.cartPage = CartPage(cls.driver)

    def tearDown(self) -> None:
        self.driver.save_screenshot('test-reports/' + self.id() + '.png')

    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.quit()

    def test_add_product_with_changed_qty(self):
        self.cartPage.open_product_page("http://54.183.112.233/index.php?route=product/product&product_id=33")
        self.cartPage.enter_data_to_qty_field(2)
        self.cartPage.click_add_to_cart_button()
        self.assertEqual("Success: You have added Samsung SyncMaster 941BW to your shopping cart!",
                         self.cartPage.get_success_message_after_adding_to_cart())

    def test_add_product(self):
        self.cartPage.open_product_page("http://54.183.112.233/index.php?route=product/product&product_id=47")
        self.cartPage.click_add_to_cart_button()
        self.assertEqual("Success: You have added HP LP3065 to your shopping cart!",
                         self.cartPage.get_success_message_after_adding_to_cart())

    def test_attendance_products_in_cart(self):
        self.cartPage.open()
        self.assertEqual(self.expected_data, self.cartPage.get_data_from_cart())

    def test_cleaning_cart(self):
        if not self.cartPage.is_cart_page_opened():
            self.cartPage.open()
        self.cartPage.click_remove_product_button()
        self.assertEqual("Your shopping cart is empty!", self.cartPage.get_success_removed_message())
