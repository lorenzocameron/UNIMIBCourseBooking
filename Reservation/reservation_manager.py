from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

class Reservation_Manager:
    def __init__(self, driver: WebDriver):
        self.driver = driver
    
    def new_reservation(self):
        reservation_element = WebDriverWait(self.driver,10).until(
              EC.element_to_be_clickable(
                  (By.CSS_SELECTOR, 'img[alt="Prenota il tuo posto a lezione"]'))
        )
        self.driver.execute_script("arguments[0].scrollIntoView(true);", reservation_element)
        reservation_element.click()

        new_reservation_element = self.driver.find_element_by_css_selector(
             'img[src="customer/sub_home_icons/easylesson_aggiungi.png"]'
        )
        new_reservation_element.click()

    def get_lessons(self):
        lessons_elements = self.driver.find_elements_by_css_selector(
            'a[title="Verifica e prenota il tuo posto"]'
        )
        lessons_elements_booked = self.driver.find_elements_by_css_selector(
            'a[title="Annulla la tua prenotazione"]'
        )

        lessons_id = [
            lessons_element.get_attribute("id") 
            for lessons_element in lessons_elements 
            if lessons_element.get_attribute("id") not in lessons_elements_booked
        ]

        return lessons_id
    
    def make_reservation(self, lessons_id: list):
        self.lessons_id = lessons_id

        for i in range(len(self.lessons_id)):
            link_element = self.driver.find_element_by_id(self.lessons_id[i])
            link_element.click()
            
            close_element = WebDriverWait(self.driver,10).until(
              EC.element_to_be_clickable(
                  (By.CSS_SELECTOR, 'button[class="mfp-close"]'))
                )
            close_element.click()
