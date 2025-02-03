class FinanceTracker:
    def __init__(self):
        self.income = 0
        self.expenses = 0

    def add_income(self, amount):
        self.income += amount

    def add_expense(self, amount):
        self.expenses += amount

    def show_balance(self):
        balance = self.income - self.expenses
        print(f"Income: ${self.income}")
        print(f"Expenses: ${self.expenses}")
        print(f"Balance: ${balance}")

# Example usage
tracker = FinanceTracker()
tracker.add_income(1000)
tracker.add_expense(300)
tracker.show_balance()
