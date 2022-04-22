from selenium.webdriver.common.by import By


class PageItem:
    def __init__(self, driver):
        self.driver = driver
        self.quantity = (By.ID, 'quantity_wanted')
        self.button_plus = (By.XPATH, '//*[@id="quantity_wanted_p"]/a[2]/span/i')

    def enter_quantity(self, quantity):
        self.driver.find_element(*self.quantity).clear()
        self.driver.find_element(*self.quantity).send_keys(quantity)

    def increment_per_one(self, quantity):
        for i in range(quantity):
            self.driver.find_element(*self.button_plus).click()

    def get_number_of_element(self):
        return self.driver.find_element(*self.quantity).get_attribute('value')

