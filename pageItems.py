class PageItems:
    def __init__(self, driver):
        self.no_results_banner = '//*[@id="center_column"]/p'
        self.title_banner = '//*[@id="center_column"]/h1/span[1]'
        self.driver = driver

    def return_no_element_text(self):
        return self.driver.find_element_by_xpath(self.no_results_banner).text

    def return_section_titles(self):
        return self.driver.find_element_by_xpath(self.title_banner).text
