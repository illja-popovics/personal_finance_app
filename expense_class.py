from datetime import datetime

class Expense:
    def __init__(self, amount, category, date=None) -> None:
        self.amount = amount
        self.category = category
        self.date = date
    
    def edit_expense(self, new_data):
        pass

    @classmethod
    def from_dict(cls, data):
        return cls(data['amount'], data['category'], data['date'])

class Income:
    pass

class Account:
    def __init__(self, month : datetime.month, total_amount=0 ):
        self.month = month
        self.month = month
        self.total_amount = total_amount
        self.registry = []
    
    def add_expense(self, expense:Expense):
        self.total_amount += expense.amount
        self.registry.append({'amount':expense.amount, "category": expense.category, "date": expense.date})




        