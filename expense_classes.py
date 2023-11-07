from datetime import datetime
from collections import UserList
import json
from fields import *


class Expense:
    def __init__(self, amount, category, user, month=None) -> None:
    
        self.amount : Amount = amount
        self.category : ExpenseCategory = category
        self.month: Month = month
        self.user: User = user
    
    def edit_expense(self, new_data):
        # need to write a method 
        pass

    @classmethod
    def from_dict(cls, data):
        return cls(data['amount'], data['category'], data['date'])

    def __str__(self):
        return f"Amount: {self.amount}, Category: {self.category}, Month: {self.month}"


class Income:
    def __init__(self, amount, category, user, month=None) -> None:
        
        self.amount: Amount  = amount
        self.category: IncomeCategory = category
        self.month: Month = month
        self.user: User = user

    def edit_income(self, new_data):
        # need to write a method 
        pass

    @classmethod
    def from_dict(cls, data):
        return cls(data['amount'], data['category'], data['date'])
    
    def __str__(self):
        return f"Amount: {self.amount}, Category: {self.category}, Month: {self.month}"

class Registry(UserList):
    def __init__(self, data, month):
        super().__init__(data)
        self.month: Month = month
    def to_dict(self):
        return {
            "month": self.month,
            "registry" : self.data
        }
    def save_to_json(self, file_path):
        data_to_save = self.to_dict()
        with open(file_path, "w") as json_file:
            json.dump(data_to_save, json_file, indent=4)

class Account_per_month:
    def __init__(self, month):
        self.month : Month = month
        self.total_amount = 0
        self.registry = Registry([],month)
    
    def add_expense(self, expense: Expense):
        self.total_amount -= expense.amount
        self.registry.append({'amount':expense.amount, "category": expense.category, "month": expense.month, "user": expense.user})

    def add_income(self, income: Income):
        self.total_amount += int(income.amount)
        self.registry.append({'amount':income.amount, "category": income.category, "month": income.month, "user": income.user})


    def save_registry(self, file_path):
        return self.registry.save_to_json(file_path)



        