import unittest
from PageObject.Product_Page import ProductPage
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


class ProductPageTests(unittest.TestCase):
    driver = None
    product_page = None

    @classmethod
    def setUpClass(cls) -> None:
        options = Options()
        options.add_argument("--disable-smooth-scrolling")
        cls.driver = webdriver.Chrome(
            options=options,
            service=Service(ChromeDriverManager().install())
        )
        cls.product_page = ProductPage(cls.driver)
        cls.product_page.open()

    def tearDown(self) -> None:
        self.driver.save_screenshot('test-reports/' + self.id() + '.png')

    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.quit()

    def test_name_presence(self):
        self.assertEqual(self.product_page.find_name(), 'Apple Cinema 30"')

    def test_brand_presence(self):
        self.assertEqual(self.product_page.find_brand(), 'Apple')

    def test_code_presence(self):
        self.assertEqual(self.product_page.find_product_code(), 'Product Code: Product 15')

    def test_price_presence(self):
        self.assertEqual(self.product_page.find_price(), '$110.00')

    def test_description_presence(self):
        self.assertIn('The 30-inch Apple Cinema HD Display delivers an amazing 2560 x 1600 pixel resolution.', self.product_page.find_description())
