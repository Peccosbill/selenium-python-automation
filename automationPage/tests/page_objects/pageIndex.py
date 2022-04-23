from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class PageIndex:

    def __init__(self, driver):
        self.query_top = (By.ID, 'search_query_top')
        self.query_button = (By.NAME, 'submit_search')
        self.dresses_link = (By.XPATH, '//*[@title="Dresses"]')
        self.driver = driver

    def search(self, item):
        try:
            search_box = WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located(self.query_top))
            search_box.send_keys(item)
            search_button = WebDriverWait(self.driver, 4).until(
                EC.element_to_be_clickable(self.query_button))
            search_button.click()
        except:
            print('No se encuentra el elemento')
    
    def click_dresses(self):
        self.driver.find_elements(*self.dresses_link)[1].click()
