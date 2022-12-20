import unittest

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from PageObject.Add_review_page import AddReviewPage


class AddReviewTest(unittest.TestCase):
    driver = None
    addReviewPage = None

    @classmethod
    def setUpClass(cls) -> None:
        options = Options()
        options.add_argument("--disable-smooth-scrolling")
        cls.driver = webdriver.Chrome(
            options=options,
            service=Service(ChromeDriverManager().install())
        )
        cls.addReviewPage = AddReviewPage(cls.driver)
        cls.addReviewPage.open()
        cls.addReviewPage.open_reviews_tab()

    def tearDown(self) -> None:
        self.driver.save_screenshot('test-reports/' + self.id() + '.png')

    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.quit()

    def test_empty_review(self):
        alert_message = "Warning: Please select a review rating!"

        self.addReviewPage.click_button_review()
        self.assertEqual(alert_message, self.addReviewPage.get_alert_message())

    def test_input_less_than_minimum_review(self):
        alert_massage = "Warning: Review Text must be between 25 and 1000 characters!"

        self.addReviewPage.click_rating()
        self.addReviewPage.enter_name('John')
        self.addReviewPage.enter_your_review('qwertyuiopasdfghjklzxcv')
        self.addReviewPage.click_button_review()

        self.assertEqual(alert_massage, self.addReviewPage.get_warning_less_symbols())

    def test_send_review(self):
        approval_text = "Thank you for your review. It has been submitted to the webmaster for approval."
        self.addReviewPage.enter_your_review("qazwsx edcrfv tgbyhn ujmiklop")
        self.addReviewPage.click_button_review()

        self.assertEqual(approval_text, self.addReviewPage.get_success_message())
