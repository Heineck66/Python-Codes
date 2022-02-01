from typing import Text
import requests
from bs4 import BeautifulSoup
import smtplib

headers = {
    "Accept-Language": "en-US,en;q=0.9,pt;q=0.8,es;q=0.7",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36 Edg/94.0.992.50",
}

url = "https://www.amazon.com.br/Memoria-Desktop-2666mhz-Hx426c16fb3-16/dp/B07WF9MD3Q/ref=sr_1_5?__mk_pt_BR=%C3%85M%C3%85%C5%BD%C3%95%C3%91&crid=AEZUYD14DVRR&dchild=1&keywords=memoria+16gb+ddr4&qid=1634860637&sprefix=memoria+16%2Caps%2C283&sr=8-5&ufe=app_do%3Aamzn1.fos.25548f35-0de7-44b3-b28e-0f56f3f96147"

response = requests.get(
    url=url,
    headers=headers,
)

soup = BeautifulSoup(response.text, "html.parser")

price = soup.select("#priceblock_ourprice")[0].text
print(price)
print(price.split()[1])
price = float(price.split()[1])
print(price)

MY_EMAIL = "[DEFAUL_EMAIL]"
MY_PASSWORD = "[PASSWD]"

if price < 500:
    # send email
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs="[RECEIVER_email]",
            msg=f"Subject:Price deal!\n\n{price}",
        )
