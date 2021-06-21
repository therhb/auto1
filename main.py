import time
import unittest
from selenium import webdriver
import page


class UITestApteline(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.get("https://www.autohero.com/de/search/")

    def test_set_up_auto_search(self):
        """"
        Test if selected filter applies

        Steps:
        1. Check if page title match
        2. From brands filter pick Volkswagen, then select Golf
        3. From basic filter menu pick mileage up to 25 000 km
        4. Check if all the filters are applied
        """
        main_page = page.SearchPage(self.driver)
        assert main_page.is_title_matches(), "Title does not match"
        main_page.click_maker_and_pick_volkswagen('Golf')
        main_page.choose_mileage_up_to25k()
        filters = main_page.return_list_of_active_filters()
        assert "Marke: Volkswagen" in filters
        assert "Modell: Golf" in filters
        assert "Kilometer: Bis 25.000 km" in filters

    def tearDown(self):
        self.driver.close()


if __name__ == '__main__':
    unittest.main()
