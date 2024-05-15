
# /api/edgar_tool.py
# Author: Jacob Thomas Messer Redmond
# UUID: UUID-00101010101

import requests
from bs4 import BeautifulSoup
import json

class EdgarTool:
    BASE_URL = "https://www.sec.gov/Archives/edgar/data"

    def __init__(self, cik):
        self.cik = cik

    def fetch_filing_index(self, filing_type="10-K"):
        url = f"https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK={self.cik}&type={filing_type}&output=atom"
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')
        return soup

    def extract_filing_info(self, soup):
        entries = soup.find_all('entry')
        filings = []
        for entry in entries:
            filing = {
                "title": entry.title.text,
                "link": entry.link['href'],
                "summary": entry.summary.text if entry.summary else None
            }
            filings.append(filing)
        return filings

    def get_filing_data(self, filing_type="10-K"):
        index_soup = self.fetch_filing_index(filing_type)
        filings = self.extract_filing_info(index_soup)
        return json.dumps(filings, indent=4)

# Example usage
if __name__ == "__main__":
    tool = EdgarTool(cik="0000320193")  # Example CIK for Apple Inc.
    print(tool.get_filing_data(filing_type="10-Q"))
