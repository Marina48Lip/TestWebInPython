import logging
import yaml
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

with open('config.yaml') as f:
    testdata = yaml.safe_load(f)

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.base_url = testdata['address']

    def find_element(self, locator, time=10):
        try:
            element = WebDriverWait(self.driver, time).until(expected_conditions.presence_of_element_located(locator), message=f'Элемент {locator} не найден')
        except:
            logging.exception('Find element exception')
            element = None
        return element


    def get_element_property(self, mode, locator, property):
        element = self.find_element(mode, locator)
        if element:
            return element.value_of_css_property(property)
        else:
            logging.error(f'Property {property} not found in element whis locator {locator}')
            return None
    def go_to_site(self):
        try:
            start_browsing = self.driver.get(self.base_url)
        except:
            logging.exception('Exception while open site')
            start_browsing = None
        return start_browsing

    def get_alert_text(self):
        try:
            alert = self.driver.switch_to.alert
            return alert.text
        except:
            logging.exception('Exception whith alert')
            return None

    def close(self):
        self.driver.close()




