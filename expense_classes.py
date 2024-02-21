from datetime import datetime
from collections import UserList
import json
from fields import Amount, IncomeCategory, User, ExpenseCategory, Month


class Expense:
    """_summary_
    """
    def __init__(self, amount, category, user, month=None) -> None: 
        self.amount = Amount(amount)
        self.category : ExpenseCategory = ExpenseCategory(category)
        if month is not None:
            self.month = Month(month)
        self.user = User(user)   
    def edit_expense(self, new_data):
        """_summary_

        Args:
            new_data (_type_): _description_
        """
        # need to write a method 
        pass

    @classmethod
    def from_dict(cls, data):
        """_summary_

        Args:
            data (_type_): _description_

        Returns:
            _type_: _description_
        """
        return cls(data['amount'], data['category'], data['date'])

    def __str__(self):
        return f"Amount: {self.amount}, Category: {self.category}, Month: {self.month}"


class Income:
    """_summary_
    """
    def __init__(self, amount, category, user, month=None) -> None:    
        self.amount = Amount(amount)
        self.category  = IncomeCategory(category)
        if month is not None:
            self.month = Month(month)
        self.user = User(user)

    def edit_income(self, new_data):
        """_summary_

        Args:
            new_data (_type_): _description_
        """
        # need to write a method 
        pass

    @classmethod
    def from_dict(cls, data):
        """_summary_

        Args:
            data (_type_): _description_

        Returns:
            _type_: _description_
        """
        return cls(data['amount'], data['category'], data['date']) 
    def __str__(self):
        return f"Amount: {self.amount}, Category: {self.category}, Month: {self.month}"

class Registry(UserList):
    """_summary_

    Args:
        UserList (_type_): _description_
    """
    def __init__(self, data, month : Month):
        super().__init__(data)
        self.month = month
    def to_dict(self):
        """_summary_

        Returns:
            _type_: _description_
        """
        return {
            "month": self.month.value,
            "registry" : self.data
        }
    def save_to_json(self, file_path):
        """_summary_

        Args:
            file_path (_type_): _description_
        """
        data_to_save = self.to_dict()
        with open(file_path, "w") as json_file:
            json.dump(data_to_save, json_file, indent=4)

class AccountPerMonth:
    """_summary_
    """
    def __init__(self, month):
        self.month = Month(month)
        self.registry = Registry([],self.month)
        self.balance = 0 
    def __add__(self,other):
        return self.balance + other.balance
    def __sub__(self,other):
        return self.balance - other.balance
    
    def add_expense(self, expense: Expense):
        """_summary_

        Args:
            expense (Expense): _description_

        Raises:
            ValueError: _description_
        """
        if expense.month is not None:
            expense.month = self.month
        if expense.month.value != self.month.value:
            raise ValueError("Expense from a different month cannot be added to the account")
        self.registry.append({
             "type": "expense",
             "amount": expense.amount.value,
             "category": expense.category.value,
             "month": expense.month.value,
             "user": expense.user.value})
        self.save_registry("./cache/registry"+str(self.month))        
        self.check_balance()        

    def add_income(self, income: Income):
        """_summary_

        Args:
            income (Income): _description_

        Raises:
            ValueError: _description_
        """
        if income.month is None:
                income.month = self.month
        if income.month.value != self.month.value:
            raise ValueError("Income from a different month cannot be added to the account")
        self.registry.append({
             "type": "income",
             "amount": income.amount.value,
             "category": income.category.value,
             "month": income.month.value,
             "user": income.user.value})
        self.save_registry(f"./cache/registry{str(self.month)}.json")
        self.check_balance()


    def save_registry(self, file_path):
        """_summary_

        Args:
            file_path (_type_): _description_
        """
        self.registry.save_to_json(file_path)

    def load_registry(self, file_path):
        """_summary_

        Args:
            file_path (_type_): _description_
        """
        with open(file_path, "r") as json_file:
            data = json.load(json_file)
            self.month = Month(data["month"])
            self.registry = Registry(data["registry"], self.month)
        self.check_balance()
    
    def check_balance(self):
        """_summary_
        """
        res = 0
        for item in self.registry:
            if item["type"] == "income":
                res += item["amount"]
            elif item["type"] == "expense":
                res -= item["amount"]
        self.balance = res
