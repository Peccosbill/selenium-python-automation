from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import unittest
from page_objects.pageIndex import PageIndex
from page_objects.pageItems import PageItems
from page_objects.pageItem import PageItem


class SearchCases(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print('Creando base de datos')
        print('BD creada')

    @classmethod
    def tearDownClass(cls):
        print('Eliminando BD...')
        print('BD eliminada...')

    def setUp(self):
        option = Options()
        option.add_argument('headless')
        self.driver = webdriver.Chrome(
            'drivers/chromedriver.exe', options=option)
        self.driver.get('http://automationpractice.com/index.php')
        self.driver.implicitly_wait(5)
        self.indexPage = PageIndex(self.driver)
        self.itemsPage = PageItems(self.driver)
        self.itemPage = PageItem(self.driver)

    
    def test_search_no_elements(self):
        try:
            self.indexPage.search('hola')
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

    def test_desses_options(self):
        self.indexPage.click_dresses()
        self.itemsPage.click_checkbox(2)
        self.itemsPage.click_checkbox(4)
        self.itemsPage.click_colors(3)

    def tearDown(self):
        self.driver.close()
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
