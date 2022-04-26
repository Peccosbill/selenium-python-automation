from selenium import webdriver
import unittest
from selenium.webdriver.chrome.options import Options
from pageObjects.pageIndex import PageIndex
from pageObjects.pageGame import PageGame


class SearchGame(unittest.TestCase):

    def setUp(self):
        option = Options()
        option.add_argument('headless')
        self.driver = webdriver.Chrome('drivers/chromedriver.exe', options=option)
        self.driver.get('https://www.gamestorrents.fm')
        self.driver.implicitly_wait(5)
        self.pageIndex = PageIndex(self.driver)
        self.pageGame = PageGame(self.driver)

    def test_filter_category(self):
        self.pageIndex.enter()
        self.pageGame.filter_category()
        game_title = self.pageGame.verify_title_game()
        self.assertEqual(game_title, 'Descargar Jurassic World Evolution 2 por Torrent')

    def test_search_game(self):
        self.pageIndex.search_game('need for speed')
        game_title = self.pageGame.select_game()
        self.assertEqual(game_title, 'Descargar Need For Speed Payback Deluxe Edition por Torrent')

    def tearDown(self):
        self.driver.close()
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
