from abc import ABC, abstractmethod

class Field(ABC):
    __value = None

    def __init__(self, value) -> None:
        self.value = value

    def __str__(self):
        return str(self.value)
    
    @abstractmethod
    def validate(self, value):
        pass


    @property
    def value(self):
        return self.__value
    
    @value.setter
    def value(self, value):
        if self.validate(value):
            self.__value = value
        else:
            raise ValueError("Invaid value")

class ExpenseCategory(Field):
    valid_categories = ["Rent", "Utilities", "", "", "", "", "", ""]

    def validate(self, value):
        return value in self.valid_categories

class IncomeCategory(Field):
     valid_categories = ["Salary", "Bonus", "Freelance"]

     def validate(self, value):
        return value in self.valid_categories

class Amount(Field):
    def validate(self, value):
        return isinstance(value, (int, float))

class User(Field):
    def validate(self, value):
        return isinstance(value, str) and len(value.split()) in [1, 2]


class Month(Field):
    def validate(self, value):
        return 1 <= int(value) <= 12

