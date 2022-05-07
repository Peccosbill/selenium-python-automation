from selenium import webdriver
import unittest
import HtmlTestRunner
from selenium.webdriver.chrome.options import Options
from pageObjects.pageIndex import PageIndex
from pageObjects.pageGame import PageGame


class SearchGame(unittest.TestCase):

    def setUp(self):
        option = Options()
        option.add_argument('headless')
        self.driver = webdriver.Chrome('./drivers/chromedriver.exe', options=option)
        self.driver.get('https://www.gamestorrents.fm')
        self.driver.implicitly_wait(5)
        self.page_index = PageIndex(self.driver)
        self.page_game = PageGame(self.driver)
    
    def test_filter_category(self):
        self.page_index.enter()
        self.page_game.filter_category()
        game_title = self.page_game.verify_title_game()
        self.assertEqual(
            game_title, 'Descargar Jurassic World Evolution 2 por Torrent')

    def test_search_game(self):
        self.page_index.search_game('need for speed')
        game_title = self.page_game.select_game()
        self.assertEqual(
            game_title, 'Descargar Need For Speed Payback Deluxe Edition por Torrent')

    def tearDown(self):
        self.driver.close()
        self.driver.quit()


if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='myreport'))
