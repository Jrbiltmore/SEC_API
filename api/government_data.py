
# /api/government_data.py
# Author: Jacob Thomas Messer Redmond
# UUID: UUID-00101010103

import requests
import json

class GovernmentData:
    BASE_URL = "https://api.usa.gov"

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
    gov_data = GovernmentData(endpoint="finance/treasury")
    params = {"limit": 10}
    print(gov_data.get_data(params))
