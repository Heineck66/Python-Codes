from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()

driver.get("https://secure-retreat-92358.herokuapp.com/")

f_name = driver.find_element_by_name("fName")
f_name.send_keys("test")

l_name = driver.find_element_by_name("lName")
l_name.send_keys("test")

email = driver.find_element_by_name("email")
email.send_keys("test@gmail.com")

bnt = driver.find_element_by_css_selector("button")
bnt.click()
