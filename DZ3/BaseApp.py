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
        return WebDriverWait(self.driver, time).until(expected_conditions.presence_of_element_located(locator), message=f'Элемент {locator} не найден')

    def get_element_property(self, mode, locator, property):
        element = self.find_element(mode, locator)
        return element.value_of_css_property(property)

    def go_to_site(self):
        return self.driver.get(self.base_url)

    def close(self):
        self.driver.close()


