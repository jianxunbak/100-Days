import requests
from twilio.rest import Client
import os

account_sid = os.environ.get("account_sid")
auth_token = os.environ.get("auth_token")

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
STOCK_API = "https://www.alphavantage.co/query"
API_STOCK_KEY_1 = os.environ.get("API_STOCK_KEY_1")
API_STOCK_KEY_2 = os.environ.get("API_STOCK_KEY_2")
PARAMETERS_STOCK = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "apikey": API_STOCK_KEY_2
}

NEWS_API = "https://newsapi.org/v2/everything"
API_NEWS_KEY = os.environ.get("API_NEWS_KEY")

stock_details = requests.get(STOCK_API, params=PARAMETERS_STOCK)
stock_details.raise_for_status()
tsla_stock = list(stock_details.json()["Time Series (Daily)"].items())
tsla_stock_yesterday = tsla_stock[0][1]["4. close"]
tsla_stock_before_yesterday = tsla_stock[1][1]["4. close"]
differences = float(tsla_stock_yesterday) - float(tsla_stock_before_yesterday)

up_down: None
if differences > 0:
    up_down = "🔺"
else:
    up_down = "🔻"

diff_percent = round((float(tsla_stock_yesterday) / float(tsla_stock_before_yesterday)) * 100)
if abs(diff_percent) > 5:
    PARAMETERS_NEWS = {
        "qInTitle": COMPANY_NAME,
        "apiKey": API_NEWS_KEY
    }

    news_details = requests.get(NEWS_API, params=PARAMETERS_NEWS)
    news_details.raise_for_status()
    three_articles = news_details[:3]
    formatted_articles = [(f"{STOCK}: {up_down}{diff_percent}%\nHeadline: {items['title']}\n"
                           f"Brief: {items['description']}") for items in three_articles]

    client = Client(account_sid, auth_token)
    for article in formatted_articles:
        message_1 = client.messages.create(
            body=article,
            from_="+19033547972",
            to="+6593622594")
        print(message_1.status)
