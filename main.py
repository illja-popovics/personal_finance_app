from expense_classes import Expense, Income, Account_per_month

oct = Account_per_month(10)

exp1 = Expense(100.50, "Rent", "Illja", 10)

inc1 = Income(1000, "Salary", "Illja", 10)

oct.add_income(inc1)
oct.add_expense(exp1)
print(oct.registry)
print(oct.balance())
