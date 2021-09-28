from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.remote.webdriver import WebDriver #driver: WebDriver as arugment
import Reservation.constants as const
from Reservation.login import Login
from Reservation.reservation_manager  import Reservation_Manager 

class Reservation:
    def __init__(self, teardown=False):
        self.driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
        self.teardown = teardown
        super(Reservation, self).__init__()

        self.driver.maximize_window()

    def __enter__(self):
        pass

    def __exit__(self, *args) -> None:
        if self.teardown:
            self.quit()
    
    def land_first_page(self):
        self.driver.get(const.BASE_URL)

    def do_login(self):
        login = Login(driver=self.driver)
        login.slide()
        login.credentials()

    def do_reservation(self):
        reservation_manager = Reservation_Manager(driver=self.driver)
        reservation_manager.new_reservation()
        lesson_ids = reservation_manager.get_lessons()
        reservation_manager.make_reservation(lesson_ids)


    

    