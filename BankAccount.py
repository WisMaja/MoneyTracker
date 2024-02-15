class BankAccount:
    def __init__(self, name, amount):
        self.name = name
        self.amount = amount

    @staticmethod
    def func(a):
        print(a)

    def addIncome(self):
        newIncomeAmount = input("Podaj kwote przychodu: ")
        name = input("Wybierz nazwe przelewu")
        account = self

        newIncome= Incomes(newIncomeAmount,name,account)

        amount+=newIncome.income


    def addExpense(self):
        newExpenseAmount = input("Podaj kwote wydayku: ")
        name = input("Wybierz nazwe przelewu")
        account = self
        if self.amount - newExpens.expense < 0:
            raise ValueError("Nie masz wystarczajaco środków na tym koncie")

        newExpens= Expenses(newExpenseAmount,name,account)

        amount-=newExpens.expense
 


class Incomes:
    def __init__(self, income, name, bankAccount):
        if income<=0:
            raise ValueError("Kwota musi być wieksza od zera")
        if len(name)==0:
            raise ValueError("Brak nazwy")
        
        self.income = income
        self.name = name
        self.bankAccount = bankAccount



class Expenses:
    def __init__(self, expense, name, bankAccount):
        if expense<=0:
            raise ValueError("Kwota musi być wieksza od zera")
        if len(name)==0:
            raise ValueError("Brak nazwy")
        self.expense = expense
        self.name = name
        self.bankAccount = BankAccount


      


        
