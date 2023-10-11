from BaseApp import BasePage
from selenium.webdriver.common.by import By

class TestSearchLocators:
    LOCATOR_INPUT_USERNAME = (By.XPATH, '''//*[@id="login"]/div[1]/label/input''')
    LOCATOR_INPUT_PASSWORD = (By.XPATH, '''//*[@id="login"]/div[2]/label/input''')
    LOCATOR_LOGIN_BUTTON = (By.CSS_SELECTOR, '''#login > div.submit.svelte-uwkxn9 > button''')
    LOCATOR_CONTACT_BUTTON = (By.XPATH, '''//*[@id="app"]/main/nav/ul/li[2]/a''')
    LOCATOR_CONTACT_US_BUTTON = (By.XPATH, '''//*[@id="contact"]/div[4]/button''')


class OperationsHelper(BasePage):
    def enter_login(self, word):
        login_field = self.find_element(TestSearchLocators.LOCATOR_INPUT_USERNAME)
        login_field.clear()
        login_field.send_keys(word)

    def enter_password(self, word):
        login_field = self.find_element(TestSearchLocators.LOCATOR_INPUT_PASSWORD)
        login_field.clear()
        login_field.send_keys(word)

    def enter_button(self):
        login_field = self.find_element(TestSearchLocators.LOCATOR_LOGIN_BUTTON)
        login_field.click()

    def enter_contact(self):
        login_field = self.find_element(TestSearchLocators.LOCATOR_CONTACT_BUTTON)
        login_field.click()

    def enter_contact_us(self):
        login_field = self.find_element(TestSearchLocators.LOCATOR_CONTACT_US_BUTTON)
        login_field.click()

    def alert(self):
        alert = self.driver.switch_to.alert
        return alert.text()

