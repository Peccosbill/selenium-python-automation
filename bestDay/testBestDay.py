from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


driver = webdriver.Chrome('drivers/chromedriver.exe')
driver.get('https://www.bestday.com.mx')
driver.implicitly_wait(5)


button_cockies = driver.find_element_by_xpath('//*[@id="lgpd-banner"]/div/a[2]')
button_cockies.click()

# Origen
cd_origen = driver.find_element_by_xpath('//*[@id="searchbox"]/div/div/div/div[3]/div[2]/div[2]/div[1]/div/div/div/input')
cd_origen.send_keys('San Blas de los Sauces, La Rioja, Argentina')
time.sleep(1)

cd_origen.send_keys(Keys.TAB)

# Destino
cd_destino = driver.find_element_by_xpath('//*[@id="searchbox"]/div/div/div/div[3]/div[2]/div[2]/div[2]/div/div/div/div/input')
cd_destino.send_keys('Londres, Inglaterra, Reino Unido')
time.sleep(1)

cd_destino.send_keys(Keys.TAB)

# Seleccionar ida
data_picker = driver.find_element_by_xpath('//*[@id="searchbox"]/div/div/div/div[3]/div[2]/div[3]/div/div[1]/div')
data_picker.click()

arrow_right = driver.find_element_by_xpath('/html/body/div[5]/div/div[2]/div[2]')
arrow_right.click()

arrow_right.click()
outward_journey = driver.find_element_by_xpath('/html/body/div[5]/div/div[5]/div[3]/div[4]/span[15]/span[1]')
outward_journey.click()


# Seleccionar vuelta
return_trip = driver.find_element_by_xpath('/html/body/div[5]/div/div[5]/div[4]/div[4]/span[5]/span[1]')
return_trip.click()

apply = driver.find_element_by_xpath('/html/body/div[7]/div/div[6]/div[2]/button[2]/em')
apply.click()

# Añadir personas
room = driver.find_element_by_xpath('//*[@id="searchbox"]/div/div/div/div[3]/div[2]/div[5]/div/div/div[5]/div/div')
room.click()

steppers_sum = driver.find_element_by_xpath('/html/body/div[4]/div/div[1]/div[2]/div[1]/div[2]/div[1]/div[2]/div/a[2]')
steppers_sum.click()
steppers_sum.click()

steppers_minors_sum = driver.find_element_by_xpath('/html/body/div[4]/div/div[1]/div[2]/div[1]/div[2]/div[2]/div[2]/div/a[2]')
steppers_minors_sum.click()
steppers_minors_sum.click()
steppers_minors_sum.click()

age_1 = driver.find_element_by_xpath('/html/body/div[4]/div/div[1]/div[2]/div[1]/div[2]/div[3]/div[1]/div[2]/div/div/select/option[6]')
age_1.click()

age_2 = driver.find_element_by_xpath('/html/body/div[4]/div/div[1]/div[2]/div[1]/div[2]/div[3]/div[2]/div[2]/div/div/select/option[15]') 
age_2.click()

age_3 = driver.find_element_by_xpath('/html/body/div[4]/div/div[1]/div[2]/div[1]/div[2]/div[3]/div[3]/div[2]/div/div/select/option[18]')
age_3.click()

apply_age = driver.find_element_by_xpath('/html/body/div[4]/div/div[2]/a[1]')
apply_age.click()

button_search = driver.find_element_by_xpath('//*[@id="searchbox"]/div/div/div/div[3]/div[2]/div[6]/div/a')
button_search.click()

time.sleep(3)

driver.close()
driver.quit()
