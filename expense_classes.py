from datetime import datetime
from collections import UserList
import json
from fields import Amount, IncomeCategory, User, ExpenseCategory, Month


class Expense:
    def __init__(self, amount, category, user, month=None) -> None: 
        self.amount = Amount(amount)
        self.category : ExpenseCategory = ExpenseCategory(category)
        if month != None:
            self.month = Month(month)
        self.user = User(user)   
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
        self.amount = Amount(amount)
        self.category  = IncomeCategory(category)
        self.month = Month(month)
        self.user = User(user)

    def edit_income(self, new_data):
        # need to write a method 
        pass

    @classmethod
    def from_dict(cls, data):
        return cls(data['amount'], data['category'], data['date']) 
    def __str__(self):
        return f"Amount: {self.amount}, Category: {self.category}, Month: {self.month}"

class Registry(UserList):
    def __init__(self, data, month : Month):
        super().__init__(data)
        self.month = month
    def to_dict(self):
        return {
            "month": self.month.value,
            "registry" : self.data
        }
    def save_to_json(self, file_path):
        data_to_save = self.to_dict()
        with open(file_path, "w") as json_file:
            json.dump(data_to_save, json_file, indent=4)

class Account_per_month:
    def __init__(self, month):
        self.month = Month(month)
        self.registry = Registry([],month) 
    def add_expense(self, expense: Expense):
        if expense.month == None:
            expense.month = self.month
        if expense.month.value != self.month.value:
            raise ValueError("Expense from a different month cannot be added to the account")
        self.registry.append({
             "type": "expense",
             "amount": expense.amount.value,
             "category": expense.category.value,
             "month": expense.month.value,
             "user": expense.user.value})        

    def add_income(self, income: Income):
        if income.month == None:
                income.month = self.month
        if income.month.value != self.month.value:
            raise ValueError("Income from a different month cannot be added to the account")
        self.registry.append({
             "type": "income",
             "amount": income.amount.value,
             "category": income.category.value,
             "month": income.month.value,
             "user": income.user.value})


    def save_registry(self, file_path):
        return self.registry.save_to_json(file_path)
    
    def balance(self):
        res = 0
        for item in self.registry:
            if item["type"] == "income":
                res += item["amount"]
            elif item["type"] == "expense":
                res -= item["amount"]
        return res



        