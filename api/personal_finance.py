
# /api/personal_finance.py
# Author: Jacob Thomas Messer Redmond
# UUID: UUID-00101010106

import json

class PersonalFinance:
    def __init__(self):
        self.expenses = []
        self.income = []

    def add_income(self, source, amount):
        self.income.append({"source": source, "amount": amount})

    def add_expense(self, category, amount):
        self.expenses.append({"category": category, "amount": amount})

    def get_balance(self):
        total_income = sum(item['amount'] for item in self.income)
        total_expenses = sum(item['amount'] for item in self.expenses)
        return total_income - total_expenses

    def get_financial_summary(self):
        balance = self.get_balance()
        summary = {
            "total_income": sum(item['amount'] for item in self.income),
            "total_expenses": sum(item['amount'] for item in self.expenses),
            "balance": balance
        }
        return json.dumps(summary, indent=4)

# Example usage
if __name__ == "__main__":
    finance = PersonalFinance()
    finance.add_income("Salary", 5000)
    finance.add_expense("Rent", 1500)
    finance.add_expense("Groceries", 500)
    print(finance.get_financial_summary())
