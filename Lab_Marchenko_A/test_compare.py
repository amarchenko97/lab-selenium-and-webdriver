import unittest
from PageObject.Compare_Page import ComparePage
from webdriver_factory import WebDriverFactory


class CompareTest(unittest.TestCase):
    driver = None
    comparePage = None
    expected_data: list[str] = ['Apple Cinema 30"', 'Samsung SyncMaster 941BW']

    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = WebDriverFactory.get_driver()
        cls.comparePage = ComparePage(cls.driver)

    def tearDown(self) -> None:
        self.driver.save_screenshot('test-reports/' + self.id() + '.png')

    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.quit()

    def test_add_product_to_compare_list(self):
        message = 'Success: You have added Apple Cinema 30" to your product comparison!'
        self.comparePage.open_product_page("http://54.183.112.233/index.php?route=product/product&product_id=42")
        self.comparePage.click_compare_button()
        self.assertEqual(message, self.comparePage.get_success_add_message())

    def test_all_added_products_presence_on_compare_page(self):
        self.comparePage.open_product_page("http://54.183.112.233/index.php?route=product/product&product_id=33")
        self.comparePage.click_compare_button()
        self.comparePage.open()
        self.assertEqual(self.expected_data, self.comparePage.get_compared_products_names())

    def test_deleting_all_products_from_compare_list(self):
        message = "You have not chosen any products to compare."
        self.comparePage.delete_products_from_compare_list()
        self.assertEqual(message, self.comparePage.get_empty_compare_list_message())
