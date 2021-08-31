from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()

driver.get("https://tv.kyivstar.ua/en")
driver.maximize_window()
time.sleep(3)
search_button = driver.find_element_by_css_selector("body > vd-root > vd-navbar > div.nav > div.nav__btn.nav__search > button")
search_button.click()

search_field = driver.find_element_by_css_selector("#cdk-overlay-0 > vd-sidenav-search > div > div.header > form > div > input")
search_field.send_keys("harry potter")
time.sleep(3)

asset = driver.find_elements_by_class_name("search-tile")
first_asset = asset[0]
first_asset.click()
time.sleep(3)
#cast = driver.find_element_by_link_text("Daniel")
driver.close() #close browser