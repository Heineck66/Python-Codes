from selenium import webdriver
import time
from pprint import pprint

start_time = time.time()
# firefox_driver_path = "../../selenium-drivers/geckodriver.exe"
# driver = webdriver.Firefox(executable_path=firefox_driver_path)

chrome_driver_path = "./chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get("https://www.python.org/")

events = {}

elements = driver.find_elements_by_css_selector(".event-widget ul li")
for index, element in enumerate(elements):
    elem_date = element.find_element_by_css_selector("time").text
    elem_event = element.find_element_by_css_selector("a").text

    events[index] = {elem_date: elem_event}

pprint(events)
driver.quit()

print("--- %s seconds ---" % (time.time() - start_time))
