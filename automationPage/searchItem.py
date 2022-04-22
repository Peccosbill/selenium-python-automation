from requests import options
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import unittest
import time
from pageIndex import PageIndex
from pageItems import PageItems
from pageItem import PageItem


class SearchCases(unittest.TestCase):

    def setUp(self):
        option = Options()
        # option.add_argument('start-maximized')
        # option.add_argument('incognito')
        option.add_argument('--headless')
        # option.add_argument('--disable-gpu')
        self.driver = webdriver.Chrome(
            'drivers\chromedriver.exe', chrome_options=option)
        self.driver.get('http://automationpractice.com/index.php')
        self.driver.implicitly_wait(5)
        # self.driver.maximize_window()
        # self.driver.set_window_size(200, 240)
        self.indexPage = PageIndex(self.driver)
        self.itemsPage = PageItems(self.driver)
        self.itemPage = PageItem(self.driver)

    def test_search_no_elements(self):
        try:
            self.indexPage.search('pepe')
            self.assertEqual(self.itemsPage.return_no_element_text(),
                            'No results were found for your search "hola"')
        except:
            self.driver.save_screenshot('error.jpg')


    def test_search_find_dresses(self):
        self.indexPage.search('dress')
        self.assertTrue('DRESS' in self.itemsPage.return_section_titles())

    def test_search_find_tshirts(self):
        self.indexPage.search('t-shirt')
        self.assertTrue('T-SHIRT' in self.itemsPage.return_section_titles())

    def test_tarea(self):
        self.indexPage.search('t-shirt')
        self.itemsPage.select_color()
        self.itemPage.enter_quantity('25')
        self.itemPage.increment_per_one(3)
        number = self.itemPage.get_number_of_element()
        self.assertTrue(number, '28')

    def test_selections(self):
        self.indexPage.search('t-shirt')
        self.itemsPage.select_by_text('Product Name: Z to A')
        self.itemsPage.select_by_value('reference:asc')
        self.itemsPage.select_by_index(4)
        time.sleep

    def tearDown(self):
        self.driver.close()
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
