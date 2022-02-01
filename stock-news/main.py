# STOCK = "TSLA"
# COMPANY_NAME = "Tesla Inc"
STOCK = "AAPL"
COMPANY_NAME = "Apple"

alpha_key = "[API_KEY]"

from typing import List
import requests

# --- Get current Day and yesterday

import datetime as dt

today = str(dt.date.today() - dt.timedelta(days=1))
yesterday = str(dt.date.today() - dt.timedelta(days=2))
print(today)
print(yesterday)

# --- Get stock info

alpha_params = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "apikey": alpha_key,
}

url = "https://www.alphavantage.co/query"
r = requests.get(url, params=alpha_params)
data = r.json()["Time Series (Daily)"]
data_list = [value for (key, value) in data.items()]

print(data_list[0])

print("\n\nfail")

# print(data["Time Series (Daily)"])

today_price = float(data_list[0]["4. close"])
yesterday_price = float(data_list[1]["4. close"])
five_percent = today_price * 0.05
percentage_dif = abs(today_price - yesterday_price) / yesterday_price * 100

print(today_price)
print(yesterday_price)
print(five_percent)


# ---- get the first 3 news pieces for the COMPANY_NAME.

news_apiKey = "[API_KEY]"


def get_news():
    news_params = {
        "q": COMPANY_NAME,
        "apiKey": news_apiKey,
    }

    url = "https://newsapi.org/v2/top-headlines?"
    response = requests.get(url, params=news_params)
    data = response.json()
    articles = data["articles"]
    total_articles = data["totalResults"]

    print(total_articles)

    return articles[:3]


# Send a seperate message with the percentage change and each article's title and description to your phone number.

from twilio.rest import Client


def send_sms(percentage: int, articles: List):

    account_sid = "[ACC_ID]"
    auth_token = "[API_KEY]"
    client = Client(account_sid, auth_token)

    formated_percent = f"🔺{abs(percentage):0.2f}%" if percentage > 0 else f"🔻{abs(percentage):0.2f}%\n"

    body = f"{STOCK}: {formated_percent}"

    for article in articles:
        headline = "Headline: " + article["title"]
        url = "link: " + article["url"]
        body += f"{headline}\n{url}"

    formated_articles = [f"{' Headline: ' + article['title']}\nlink: {article['url']}\n" for article in articles]

    message = client.messages.create(body=body, from_="FROM_NUMBER", to="[TO_NUMBER]")

    print("\n\n", message.status)
    print(message.price)
    print(message.body)


send_sms(percentage_dif, get_news())
