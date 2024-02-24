class BankAccount:
    def __init__(self, name, amount):
        self.name = name
        self.amount = amount

    @staticmethod
    def func(a):
        print(a)

    def addIncome(self):
        newIncomeAmount = float(input("Podaj kwotę przychodu: "))  # Konwertuj do float
        name = input("Wybierz nazwę przelewu: ")
        newIncome = Incomes(newIncomeAmount, name, self)
        self.amount += newIncome.income  # Dodaj nowy przychód do salda konta


    def addExpense(self):
        newExpenseAmount = float(input("Podaj kwotę wydatku: "))  # Konwertuj do float
        name = input("Wybierz nazwę przelewu: ")
        if self.amount - newExpenseAmount < 0:  # Poprawione newExpense na newExpenseAmount
            raise ValueError("Nie masz wystarczająco środków na tym koncie")
        newExpense = Expenses(newExpenseAmount, name, self)
        self.amount -= newExpense.expense  # Odejmij nowy wydatek od salda konta

    def showBalance(self):
        print("O to twój obecny stan konta: ", self.amount)

    


class Incomes:
    def __init__(self, income, name, bankAccount):
        if income <= 0:
            raise ValueError("Kwota musi być większa od zera")
        if len(name) == 0:
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

