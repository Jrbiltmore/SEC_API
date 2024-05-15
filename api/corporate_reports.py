
# /api/corporate_reports.py
# Author: Jacob Thomas Messer Redmond
# UUID: UUID-00101010110

import json

class CorporateReports:
    def __init__(self):
        self.reports = []

    def add_report(self, title, content):
        self.reports.append({"title": title, "content": content})

    def get_report(self, title):
        for report in self.reports:
            if report["title"] == title:
                return report
        return None

    def get_all_reports(self):
        return json.dumps(self.reports, indent=4)

# Example usage
if __name__ == "__main__":
    reports = CorporateReports()
    reports.add_report("Q1 2024 Financials", "Content of Q1 2024 financial report")
    reports.add_report("Q2 2024 Financials", "Content of Q2 2024 financial report")
    print(reports.get_report("Q1 2024 Financials"))
    print(reports.get_all_reports())
