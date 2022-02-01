from bs4 import BeautifulSoup
import requests
import re
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

page_url = "https://www.zillow.com/homes/for_rent/1-_beds/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22mapBounds%22%3A%7B%22west%22%3A-123.14950026464844%2C%22east%22%3A-121.71715773535156%2C%22south%22%3A37.3441951223128%2C%22north%22%3A38.203888622220404%7D%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22price%22%3A%7B%22max%22%3A872627%7D%2C%22beds%22%3A%7B%22min%22%3A1%7D%2C%22fore%22%3A%7B%22value%22%3Afalse%7D%2C%22mp%22%3A%7B%22max%22%3A3000%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22fr%22%3A%7B%22value%22%3Atrue%7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22fsba%22%3A%7B%22value%22%3Afalse%7D%7D%2C%22isListVisible%22%3Atrue%7D"

headers = {
    "Accept-Language": "en-US,en;q=0.9,pt;q=0.8,es;q=0.7",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36 Edg/95.0.1020.30",
}

response = requests.get(url=page_url, headers=headers)

soup = BeautifulSoup(response.text, "html.parser")

all_price_elements = soup.select(
    'ul[class="photo-cards photo-cards_wow photo-cards_short"] div[class="list-card-price"]'
)
all_prices = [re.split("[/+]", price.text)[0] for price in all_price_elements if "$" in price.text]

print(all_prices)

driver_path = "../../selenium-drivers/chromedriver.exe"

driver = webdriver.Chrome(executable_path=driver_path)

driver.get("https://docs.google.com/forms/d/e/1FAIpQLSdNBlcDtw21i4EuFms5nbXAKHlCxaMWoi_D5ak4_ZZ7iZGVEA/viewform")

for price in all_prices:
    print(price)
    try:
        element = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located(
                (By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span/span')
            ),
        )
    finally:
        address_field = driver.find_element_by_xpath(
            '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input'
        )
        price_field = driver.find_element_by_xpath(
            '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input'
        )
        link_field = driver.find_element_by_xpath(
            '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input'
        )

        address_field.send_keys("address layer")
        price_field.send_keys(price)
        link_field.send_keys(
            "https://www.zillow.com/homedetails/1830-6th-Ave-APT-18-Oakland-CA-94606/2092007940_zpid/"
        )

        bnt = driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span/span')
        bnt.click()
        time.sleep(0.5)
        back_bnt = driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[1]/div/div[4]/a").click()


driver.quit()
