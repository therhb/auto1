from selenium.webdriver.common.by import By


class SearchPageLocators(object):
    """Class with search page locators, which allows to pick a filter"""
    MAKER_BUTTON = (By.ID, 'carMakeFilter')
    BASIC_BUTTON = (By.ID, 'basicFilter')


class BrandLocators(object):
    """Class with locator from Brand picking window"""
    VOLKSWAGEN_BUTTON = (By.XPATH, '//input[@data-qa-selector="905"]')


class BasicValuesLocators(object):
    """Class with locator from basic features filters window"""
    RANGE_END_25K_OPTION = (By.XPATH, '//*[@id="rangeEnd"]/option[3]')


class ActiveFilters(object):
    "Class with locators that lists, active filters"
    ACTIVE_FILTERS = (By.XPATH, '//div[@data-qa-selector="active-filter"]')