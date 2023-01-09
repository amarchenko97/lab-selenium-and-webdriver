import unittest
from PageObject.SearchPage import SearchPage
from webdriver_factory import WebDriverFactory


class SearchPageTest(unittest.TestCase):
    driver = None
    searchPage = None
    test_data = ['apple', 'sony', 'nokia', 'stunning']
    expected_data = [['Apple Cinema 30"', '$110.00'], ['Sony VAIO', '$1,202.00'], 'There is no product that matches the search criteria.', ('HP LP3065', 'iMac')]

    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = WebDriverFactory.get_driver()
        cls.searchPage = SearchPage(cls.driver)
        cls.searchPage.open()

    def tearDown(self) -> None:
        self.driver.save_screenshot('test-reports/' + self.id() + '.png')

    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.quit()

    def test_search_product(self):
        number_of_alone_products: int = 2

        for i in range(number_of_alone_products - 1):
            self.searchPage.input_to_search_field(self.test_data[i])
            self.searchPage.click_search_button()

            self.assertEqual(self.searchPage.find_product_details(), self.expected_data[i])

    def test_search_several_products(self):
        self.searchPage.input_to_search_field(self.test_data[2])
        self.searchPage.click_search_button()
        self.assertEqual(self.expected_data[2], self.searchPage.find_message())

    def test_search_not_existed(self):
        self.searchPage.find_option()
        self.searchPage.check_option()
        self.searchPage.input_to_search_field(self.test_data[3])
        self.searchPage.click_search_button()
        self.assertEqual(self.searchPage.find_several_products(), self.expected_data[3])
