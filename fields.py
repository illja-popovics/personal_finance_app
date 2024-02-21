from abc import ABC, abstractmethod

class Field(ABC):
    """_summary_

    Args:
        ABC (_type_): _description_

    Raises:
        ValueError: _description_

    Returns:
        _type_: _description_
    """
    __value = None

    def __init__(self, value) -> None:
        self.value = value

    def __str__(self):
        return str(self.value)
    
    @abstractmethod
    def validate(self, value):
        """_summary_

        Args:
            value (_type_): _description_
        """
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
    """_summary_

    Args:
        Field (_type_): _description_

    Returns:
        _type_: _description_
    """
    valid_categories = ["Rent", "Utilities", "", "", "", "", "", ""]

    def validate(self, value):
        return value in self.valid_categories

class IncomeCategory(Field):
    """_summary_

    Args:
        Field (_type_): _description_

    Returns:
        _type_: _description_
    """
    valid_categories = ["Salary", "Bonus", "Freelance"]

    def validate(self, value):
        return value in self.valid_categories

class Amount(Field):
    """_summary_

    Args:
        Field (_type_): _description_
    """
    def validate(self, value):
        return isinstance(value, (int, float))

class User(Field):
    """_summary_

    Args:
        Field (_type_): _description_
    """
    def validate(self, value):
        return isinstance(value, str) and len(value.split()) in [1, 2]


class Month(Field):
    """_summary_

    Args:
        Field (_type_): _description_
    """
    def validate(self, value):
        return 1 <= int(value) <= 12

