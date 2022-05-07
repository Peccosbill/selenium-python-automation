from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class PageGame:

    def __init__(self, driver):
        self.driver = driver
        self.select_platform = (By.XPATH, '//*[@id="header"]/div[4]/div/div[1]/ul/li[1]/a')
        self.select_category = (By.XPATH, '//*[@id="collapseJuegosPC"]/ul/li[6]/a')
        self.card_game = (By.XPATH, '//*[@id="home"]/div[31]/div/div/h6/a')
        self.game_title = (By.XPATH, '//*[@id="header"]/div[3]/div[2]/h1')
        self.game_in_list = (By.LINK_TEXT, 'Need For Speed Payback Deluxe Edition')

    def filter_category(self):
        self.driver.find_element(*self.select_platform).click()
        self.driver.find_element(*self.select_category).click()
        card_game = WebDriverWait(self.driver, 4).until(EC.element_to_be_clickable(self.card_game))
        card_game.click()

    def verify_title_game(self):
        game_title = WebDriverWait(self.driver, 4).until(EC.presence_of_element_located(self.game_title))
        return game_title.text

    def select_game(self):
        game = WebDriverWait(self.driver, 4).until(EC.presence_of_element_located(self.game_in_list))
        game.click()
        game_title = WebDriverWait(self.driver, 4).until(EC.presence_of_element_located(self.game_title))
        return game_title.text

