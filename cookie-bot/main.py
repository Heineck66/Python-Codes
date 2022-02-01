import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# driver = webdriver.Chrome()
profile = webdriver.FirefoxProfile("./")
driver = webdriver.Firefox(firefox_profile=profile, executable_path="../../selenium-drivers/geckodriver")

driver.get("https://orteil.dashnet.org/cookieclicker/")

try:
    element = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.ID, "bigCookie")),
    )
finally:
    print("finally")
    big_cookie = driver.find_element_by_css_selector("#bigCookie")

check_store = time.time() + 0.5
five_min = time.time() + 60 * 5

while True:

    big_cookie.click()
    big_cookie.click()

    if time.time() > check_store:
        products = driver.find_elements_by_css_selector("#products div[class='product unlocked enabled']")
        for product in products[::-1]:
            product.click()
        check_store = time.time() + 0.5

    if time.time() > five_min:
        cookies = driver.find_element_by_id("cookies").text
        print(cookies)
        break
