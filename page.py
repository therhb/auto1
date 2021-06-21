from selenium.webdriver.common.by import By
from locators import SearchPageLocators, BrandLocators, BasicValuesLocators, ActiveFilters
import time


class BasePage(object):

    def __init__(self, driver):
        self.driver = driver


class SearchPage(BasePage):
    """
    Contains scripts that can be performed on the search page
    """

    def is_title_matches(self):
        return "Jetzt Top-Gebrauchtwagen online kaufen | Autohero.com" in self.driver.title

    def click_maker_and_pick_volkswagen(self, model):
        """
        Click maker filter, pick volkswagen, then pick chosen model
        """
        self.driver.find_element(*SearchPageLocators.MAKER_BUTTON).click()
        self.driver.find_element(*BrandLocators.VOLKSWAGEN_BUTTON).click()
        time.sleep(1)
        self.driver.find_element(By.XPATH, f"//input[@data-qa-selector-value='{model}']").click()

    def choose_mileage_up_to25k(self):
        """
        Click basic filter, pick mileage up to 25 000 km
        """
        self.driver.find_element(*SearchPageLocators.BASIC_BUTTON).click()
        self.driver.find_element(*BasicValuesLocators.RANGE_END_25K_OPTION).click()

    def return_list_of_active_filters(self):
        """
        List active filters then append text from boxes into list
        :return: list of text from filter boxes
        """
        filters = []
        for record in self.driver.find_elements(*ActiveFilters.ACTIVE_FILTERS):
            filters.append(record.text)
        return filters



