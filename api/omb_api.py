
# /api/omb_api.py
# Author: Jacob Thomas Messer Redmond
# UUID: UUID-00101010112

import requests
import json

class OMBAPI:
    BASE_URL = "https://api.omb.gov"

    def __init__(self, endpoint):
        self.endpoint = endpoint

    def fetch_data(self, params=None):
        url = f"{self.BASE_URL}/{self.endpoint}"
        response = requests.get(url, params=params)
        return response.json()

    def get_data(self, params=None):
        data = self.fetch_data(params)
        return json.dumps(data, indent=4)

# Example usage
if __name__ == "__main__":
    omb_api = OMBAPI(endpoint="budget")
    params = {"fiscal_year": 2024}
    print(omb_api.get_data(params))
