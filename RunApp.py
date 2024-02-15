import BankAccount

run = True


def stop():

    global run
    run = False


def choice(x):
    action = {
        '1': BankAccount.BankAccount.addIncome,
        '2': BankAccount.BankAccount.addExpense,
        '3': BankAccount.BankAccount.showBalance,
        '4': BankAccount.BankAccount.add,
        '5': stop
    }

    if x in action:
        action[x]()
    else:
        print("Invalid value err")


while run:
    print("/////////////////////////////////")
    userInput = input("Dodaj przychod - 1\n"
                      "Dodaj wydatek - 2\n"
                      "Wyswietl stan konta - 3\n"
                      "Dodaj konto - 4\n"
                      "Zakoncz - 5\n")

    choice(userInput)
