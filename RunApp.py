from BankAccount import BankAccount, Expenses, Incomes 

run = True
bank = BankAccount("Konto1",0)

def add():
    print("Stworzysz teraz nowe konto bankowe")
    name = input("Podaj nazwe nowego konta bankowego: ")
    amount = input("Podaj kwote jaka ma znajodować sie na tym koncie: ")
    bank = BankAccount(name, amount)

def stop():

    global run
    run = False


def choice(x):
    action = {
        '1': bank.addIncome,
        '2': bank.addExpense,
        '3': bank.showBalance,
        '4': add,
        '5': stop
    }

    if x in action:
        action[x]()
    else:
        print("Invalid value err", x)


while run:
    print("/////////////////////////////////")
    userInput = input("Dodaj przychod - 1\n"
                      "Dodaj wydatek - 2\n"
                      "Wyswietl stan konta - 3\n"
                      "Dodaj konto - 4\n"
                      "Zakoncz - 5\n")

    choice(userInput)
