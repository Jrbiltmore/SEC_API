
# /api/financial_data_aggregator.py
# Author: Jacob Thomas Messer Redmond
# UUID: UUID-00101010102

import requests
import json

class FinancialDataAggregator:
    def __init__(self, sources):
        self.sources = sources

    def fetch_data(self, source):
        response = requests.get(source)
        return response.json()

    def aggregate_data(self):
        aggregated_data = {}
        for source in self.sources:
            data = self.fetch_data(source)
            aggregated_data[source] = data
        return aggregated_data

    def get_aggregated_data(self):
        data = self.aggregate_data()
        return json.dumps(data, indent=4)

# Example usage
if __name__ == "__main__":
    sources = [
        "https://api.example.com/financials/source1",
        "https://api.example.com/financials/source2"
    ]
    aggregator = FinancialDataAggregator(sources)
    print(aggregator.get_aggregated_data())
