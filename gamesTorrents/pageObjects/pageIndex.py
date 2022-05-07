from selenium.webdriver.common.by import By


class PageIndex:

    def __init__(self, driver):
        self.button_enter = (By.XPATH, '//*[@id="main"]/div/div/div[3]/a')
        self.search_bar = (By.XPATH, '//*[@id="buscador"]/input')
        self.search_button = (By.XPATH, '//*[@id="buscador"]/a')
        self.driver = driver

    def enter(self):
        self.driver.find_element(*self.button_enter).click()

    def search_game(self, item):
        self.driver.find_element(*self.search_bar).send_keys(item)
        self.driver.find_element(*self.search_button).click()
