from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

class Login:
    def __init__(self, driver: WebDriver):
        self.driver = driver

    def slide(self):
        slider_element = self.driver.find_element_by_class_name('slider.round')
        slider_element.click()

    def credentials(self):
        login_element = self.driver.find_element_by_id('oauth_btn')
        login_element.click()

        username_element = WebDriverWait(self.driver, 10).until(
        EC.presence_of_element_located((By.ID, "username"))
        )
        username_element.send_keys('l.cameron@campus.unimib.it')

        password_element = self.driver.find_element_by_id('password')
        password_element.send_keys('Vostro1710\\')

        login_button_element = self.driver.find_element_by_css_selector(
            'button[name="_eventId_proceed"]'
        )
        login_button_element.click()