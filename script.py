from selenium import webdriver
import unittest


class ButtonClick(unittest.TestCase):

    def setUp(self):
        driver = webdriver.Chrome('chromedriver.exe')
        self.driver = driver
        self.driver.get('https://cssreference.io/')
        self.driver.implicitly_wait(5)

    def test_click(self):
        try:
            self.driver.find_element_by_xpath(
                '/html/body/main/nav/a[1]').click()
            title = self.driver.find_element_by_class_name(
                'heading-title').text
            self.assertEqual(title, 'Animations in CSS')
        except:
            self.driver.save_screenshot('error.jpg')

    def tearDown(self):
        self.driver.close()
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
