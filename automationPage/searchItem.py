from selenium import webdriver
import unittest
import time
from pageIndex import PageIndex
from pageItems import PageItems
from pageItem import PageItem


class SearchCases(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome('drivers\chromedriver.exe')
        self.driver.get('http://automationpractice.com/index.php')
        self.driver.implicitly_wait(5)
        self.indexPage = PageIndex(self.driver)
        self.itemsPage = PageItems(self.driver)
        self.itemPage = PageItem(self.driver)
    
    @unittest.skip('Not nedded now')
    def test_search_no_elements(self):
        self.indexPage.search('hola')
        time.sleep(5)
        self.assertEqual(self.itemsPage.return_no_element_text(),
                         'No results were found for your search "hola"')

    @unittest.skip('Not nedded now')
    def test_search_find_dresses(self):
        self.indexPage.search('dress')
        time.sleep(5)
        self.assertTrue('DRESS' in self.itemsPage.return_section_titles())

    @unittest.skip('Not nedded now')
    def test_search_find_tshirts(self):
        self.indexPage.search('t-shirt')
        time.sleep(5)
        self.assertTrue('T-SHIRT' in self.itemsPage.return_section_titles())

    @unittest.skip('Not nedded now')
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
        time.sleep(3)
        self.itemsPage.select_by_value('reference:asc')
        time.sleep(3)
        self.itemsPage.select_by_index(4)
        time.sleep

    def tearDown(self):
        self.driver.close()
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
