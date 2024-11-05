import os

from dotenv import load_dotenv
import json
import requests

load_dotenv()


def get_currency_rates():
    with open("user_settings.json") as f:
        data = json.load(f)

    list_currency = data["user_currencies"]
    headers = {
        "apikey": os.getenv("API_KEY_EXCHANGE_RATES")
    }

    currency_rates = []
    for cur in list_currency:
        url = f"https://api.apilayer.com/exchangerates_data/latest?symbols=RUB&base={cur}"
        response = requests.get(url, headers=headers).json()
        currency_rates.append({"currency": cur, "rate": response.get("rates").get("RUB")})

    return currency_rates


def get_stock_prices():
    with open("user_settings.json") as f:
        data = json.load(f)

    list_stocks = data["user_stocks"]

    api_alpha_vanvage = os.getenv("API_KEY_ALPHA_VAVANGE")
    interval = "1min"

    list_stocks_prices = []
    for stock in list_stocks:
        url = f'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol={stock}&interval={interval}&apikey={api_alpha_vanvage}'

        data = requests.get(url).json()
        last_refreshed = data["Meta Data"].get("3. Last Refreshed")
        price_stock = data[f"Time Series ({interval})"].get(last_refreshed).get("1. open")
        list_stocks_prices.append({"stock": stock, "price": price_stock})

    return list_stocks_prices


if __name__ == "__main__":
    # print(get_currency_rates)
    print(get_stock_prices())
