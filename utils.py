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


print(get_currency_rates())
