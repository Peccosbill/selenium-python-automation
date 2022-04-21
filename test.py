from selenium import webdriver
import unittest
import time

tc = unittest.TestCase('__init__')
driver = webdriver.Chrome('chromedriver.exe')
driver.get('http://automationpractice.com/index.php')
driver.find_element('search_query_top').send_keys('hola')
driver.find_element(by=By.NAME, value='submit_search').click()
time.sleep(5)
tc.assertEqual('No results were found for your search "hola"', driver.find_element(by=By.XPATH, value='//*[@id="center_column"]/p').text)

driver.close()
driver.quit()
