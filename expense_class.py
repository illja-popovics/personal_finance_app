from datetime import datetime
import json

class Expense:
    def __init__(self, amount, category, user, month=None) -> None:
        if int(amount) >= 0:
            raise ValueError("Amount must be a positive number")
        if category not in ["Rent", "Utilities", "", "", "", "", "", ""]:
            raise ValueError("Category must be one of these:")
        if not 1 <= month <=12:  
            raise ValueError("Month must be a datetime.month object or None")
        
        self.amount = amount
        self.category = category
        self.month = month
        self.user = user
    
    def edit_expense(self, new_data):
        pass

    @classmethod
    def from_dict(cls, data):
        return cls(data['amount'], data['category'], data['date'])

    def __str__(self):
        return f"Amount: {self.amount}, Category: {self.category}, Month: {self.month}"


class Income:
    def __init__(self, amount, category, user, month=None) -> None:
        if int(amount) <= 0:
            raise ValueError("Amount must be a positive number")
        if category not in ["Salary", "", ]:
            raise ValueError("Category must be one of these:")
        if month is not None and not isinstance(month, datetime.month):
            raise ValueError("Month must be a datetime.month object or None")
        
        self.amount = amount
        self.category = category
        self.month = month
        self.user = user

    def edit_income(self, new_data):
        pass

    @classmethod
    def from_dict(cls, data):
        return cls(data['amount'], data['category'], data['date'])


class Account_per_month:
    def __init__(self, month : datetime.month):
        self.month = month
        self.total_amount = 0
        self.registry = []
    
    def add_expense(self, expense: Expense):
        self.total_amount += expense.amount
        self.registry.append({'amount':expense.amount, "category": expense.category, "month": expense.month, "user": expense.user})

    def add_income(self, income: Income):
        self.total_amount += int(income.amount)
        self.registry.append({'amount':income.amount, "category": income.category, "month": income.month, "user": income.user})


    def save_registry(self, file_path):
        pass 



        