
# /api/crypto_exchange.py
# Author: Jacob Thomas Messer Redmond
# UUID: UUID-00101010105

import requests
import json

class CryptoExchange:
    BASE_URL = "https://api.coingecko.com/api/v3"

    def get_market_data(self, coin_id="bitcoin"):
        url = f"{self.BASE_URL}/coins/markets"
        params = {"vs_currency": "usd", "ids": coin_id}
        response = requests.get(url, params=params)
        return response.json()

    def get_exchange_rates(self):
        url = f"{self.BASE_URL}/exchange_rates"
        response = requests.get(url)
        return response.json()

    def get_coin_info(self, coin_id="bitcoin"):
        url = f"{self.BASE_URL}/coins/{coin_id}"
        response = requests.get(url)
        return response.json()

# Example usage
if __name__ == "__main__":
    exchange = CryptoExchange()
    print(exchange.get_market_data("ethereum"))
    print(exchange.get_exchange_rates())
    print(exchange.get_coin_info("bitcoin"))
