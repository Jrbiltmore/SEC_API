
# /api/business_finance.py
# Author: Jacob Thomas Messer Redmond
# UUID: UUID-00101010107

import json

class BusinessFinance:
    def __init__(self):
        self.revenue = []
        self.expenses = []

    def add_revenue(self, source, amount):
        self.revenue.append({"source": source, "amount": amount})

    def add_expense(self, category, amount):
        self.expenses.append({"category": category, "amount": amount})

    def get_balance(self):
        total_revenue = sum(item['amount'] for item in self.revenue)
        total_expenses = sum(item['amount'] for item in self.expenses)
        return total_revenue - total_expenses

    def get_financial_summary(self):
        balance = self.get_balance()
        summary = {
            "total_revenue": sum(item['amount'] for item in self.revenue),
            "total_expenses": sum(item['amount'] for item in self.expenses),
            "balance": balance
        }
        return json.dumps(summary, indent=4)

# Example usage
if __name__ == "__main__":
    finance = BusinessFinance()
    finance.add_revenue("Product Sales", 10000)
    finance.add_expense("Salaries", 4000)
    finance.add_expense("Office Supplies", 600)
    print(finance.get_financial_summary())
