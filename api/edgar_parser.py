
import requests
from bs4 import BeautifulSoup
import re
import json

class EdgarParser:
    BASE_URL = "https://www.sec.gov/Archives/edgar/data"

    def __init__(self, cik):
        """
        Initializes the EdgarParser with the given Central Index Key (CIK).
        
        :param cik: Central Index Key (CIK) of the company
        """
        self.cik = cik

    def get_filing_urls(self, filing_type="10-K", count=10):
        """
        Retrieves URLs for the specified type of filings.
        
        :param filing_type: Type of filing to retrieve (e.g., "10-K", "10-Q")
        :param count: Number of filings to retrieve
        :return: List of filing URLs
        """
        search_url = f"https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK={self.cik}&type={filing_type}&count={count}&output=atom"
        response = requests.get(search_url)
        soup = BeautifulSoup(response.content, 'html.parser')
        entries = soup.find_all('entry')
        
        urls = []
        for entry in entries:
            link = entry.find('link')
            if link and 'href' in link.attrs:
                urls.append(link['href'])
        
        return urls

    def parse_filing(self, filing_url):
        """
        Parses the filing at the given URL and extracts relevant data.
        
        :param filing_url: URL of the filing to parse
        :return: Parsed data in JSON format
        """
        response = requests.get(filing_url)
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # Extract document content
        document_content = soup.find('document').text
        
        # Example: Extracting the company name and filing date
        company_name = re.search(r'COMPANY CONFORMED NAME:\s+(.*)', document_content)
        filing_date = re.search(r'FILED AS OF DATE:\s+(\d{8})', document_content)
        
        data = {
            "company_name": company_name.group(1).strip() if company_name else None,
            "filing_date": filing_date.group(1).strip() if filing_date else None,
            "document_content": document_content
        }
        
        return json.dumps(data, indent=4)

    def get_recent_filings(self, filing_type="10-K", count=10):
        """
        Retrieves and parses recent filings.
        
        :param filing_type: Type of filing to retrieve and parse
        :param count: Number of filings to retrieve and parse
        :return: List of parsed filings in JSON format
        """
        filing_urls = self.get_filing_urls(filing_type, count)
        filings = [self.parse_filing(url) for url in filing_urls]
        return filings

# Example usage
if __name__ == "__main__":
    parser = EdgarParser(cik="0000320193")  # Example CIK for Apple Inc.
    recent_filings = parser.get_recent_filings(filing_type="10-K", count=5)
    for filing in recent_filings:
        print(filing)
