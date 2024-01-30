#!/usr/bin/env python
# coding: utf-8

# In[1]:


import json
from datetime import datetime

class BudgetTracker:
    def __init__(self):
        self.transactions = []

    def display_menu(self):
        print("\nBudget Tracker Menu:")
        print("1. Add Income")
        print("2. Add Expense")
        print("3. Calculate Budget")
        print("4. Expense Analysis")
        print("5. Exit")

    def add_income(self):
        amount = float(input("Enter income amount: "))
        description = input("Enter income description: ")
        self.transactions.append({"type": "Income", "amount": amount, "description": description, "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S")})
        print("Income added successfully!")

    def add_expense(self):
        amount = float(input("Enter expense amount: "))
        description = input("Enter expense description: ")
        self.transactions.append({"type": "Expense", "amount": amount, "description": description, "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S")})
        print("Expense added successfully!")

    def calculate_budget(self):
        total_income = sum(transaction["amount"] for transaction in self.transactions if transaction["type"] == "Income")
        total_expense = sum(transaction["amount"] for transaction in self.transactions if transaction["type"] == "Expense")
        budget = total_income - total_expense
        print(f"Total Income: ${total_income}")
        print(f"Total Expense: ${total_expense}")
        print(f"Budget: ${budget}")

    def expense_analysis(self):
        expense_data = [transaction for transaction in self.transactions if transaction["type"] == "Expense"]
        print("\nExpense Analysis:")
        for expense in expense_data:
            print(f"{expense['description']}: ${expense['amount']} on {expense['date']}")

    def save_data(self):
        with open("budget_data.json", "w") as file:
            json.dump(self.transactions, file)
        print("Data saved successfully!")

    def load_data(self):
        try:
            with open("budget_data.json", "r") as file:
                self.transactions = json.load(file)
            print("Data loaded successfully!")
        except FileNotFoundError:
            print("No previous data found.")

    def run_budget_tracker(self):
        self.load_data()

        while True:
            self.display_menu()
            choice = input("Enter your choice (1-5): ")

            if choice == "1":
                self.add_income()
            elif choice == "2":
                self.add_expense()
            elif choice == "3":
                self.calculate_budget()
            elif choice == "4":
                self.expense_analysis()
            elif choice == "5":
                self.save_data()
                print("Exiting Budget Tracker. Goodbye!")
                break
            else:
                print("Invalid choice. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    budget_tracker = BudgetTracker()
    budget_tracker.run_budget_tracker()

