
# /api/budget_api.py
# Author: Jacob Thomas Messer Redmond
# UUID: UUID-00101010111

import json

class BudgetAPI:
    def __init__(self):
        self.budgets = {}

    def create_budget(self, name, total_amount):
        self.budgets[name] = {"total_amount": total_amount, "expenses": []}

    def add_expense(self, budget_name, category, amount):
        if budget_name in self.budgets:
            self.budgets[budget_name]["expenses"].append({"category": category, "amount": amount})

    def get_budget_summary(self, budget_name):
        if budget_name in self.budgets:
            budget = self.budgets[budget_name]
            total_expenses = sum(expense["amount"] for expense in budget["expenses"])
            remaining_amount = budget["total_amount"] - total_expenses
            summary = {
                "total_amount": budget["total_amount"],
                "total_expenses": total_expenses,
                "remaining_amount": remaining_amount
            }
            return json.dumps(summary, indent=4)
        return None

# Example usage
if __name__ == "__main__":
    budget_api = BudgetAPI()
    budget_api.create_budget("Personal Budget", 5000)
    budget_api.add_expense("Personal Budget", "Rent", 1500)
    budget_api.add_expense("Personal Budget", "Groceries", 500)
    print(budget_api.get_budget_summary("Personal Budget"))
