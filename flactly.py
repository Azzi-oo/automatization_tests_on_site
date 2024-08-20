from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_condition as ec
from time import sleep


browser = webdriver.Chrome()
browser.implicitly_wait(10)
browser.get('https://magento.softwaretestingboard.com/women/tops-women/tees-women.html')
WebDriverWait(browser, 10).until(ec.text_to_be_present_in_element((By.TAG_NAME, 'body'), 'Default welcome msg!'))
# sleep(2)

girls = browser.find_elements(By.CLASS_NAME, 'product-item-link')
first_girl = girls[0]
# print(first_girl.id)

# print(first_girl.text)
# print(first_girl.get_attribute('href'))
sorter = browser.find_elements(By.ID, 'sorter')
select = Select(sorter)
select.select_by_value('price')

WebDriverWait(browser, 10).until(ec.staleness_of(first_girl))
sleep(5)
print(first_girl.text)
print(first_girl.get_attribute('href'))

first_girl = browser.find_element(By.XPATH, '/html/body/div[1]/main/div[3]/div[1]/div[3]/ol/li[1]/div/div/strong/a')
print(first_girl.text)
print(first_girl.get_attribute('href'))
