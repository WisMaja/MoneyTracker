import tkinter as tk
from BankAccount import BankAccount, Expenses, Incomes

class Interface:
    def __init__(self, master):
        self.master = master
        master.title("Bank Account Interface")
        master.geometry("400x300")  # Ustawienie rozmiaru okna

        self.bank = BankAccount("Konto1", 0)

        # Kontener przycisków
        self.button_frame = tk.Frame(master)
        self.button_frame.pack(side="left", padx=10, pady=10)  # Wyjustowanie do lewej strony, dodanie marginesów

        self.label = tk.Label(self.button_frame, text="Wybierz opcję:")
        self.label.pack(anchor="w", padx=10, pady=5)  # Wyjustowanie do lewej strony, dodanie marginesów

        self.add_income_button = tk.Button(self.button_frame, text="Dodaj przychód", command=self.show_income_entry)
        self.add_income_button.pack(anchor="w", padx=10, pady=5)  # Wyjustowanie do lewej strony, dodanie marginesów

        self.add_expense_button = tk.Button(self.button_frame, text="Dodaj wydatek", command=self.show_expense_entry)
        self.add_expense_button.pack(anchor="w", padx=10, pady=5)  # Wyjustowanie do lewej strony, dodanie marginesów

        self.show_balance_button = tk.Button(self.button_frame, text="Wyświetl stan konta", command=self.show_balance)
        self.show_balance_button.pack(anchor="w", padx=10, pady=5)  # Wyjustowanie do lewej strony, dodanie marginesów

        self.add_account_button = tk.Button(self.button_frame, text="Dodaj konto", command=self.add_account)
        self.add_account_button.pack(anchor="w", padx=10, pady=5)  # Wyjustowanie do lewej strony, dodanie marginesów

        self.quit_button = tk.Button(self.button_frame, text="Zakończ", command=self.quit)
        self.quit_button.pack(anchor="w", padx=10, pady=5)  # Wyjustowanie do lewej strony, dodanie marginesów

        # Kontener dla obecnego stanu konta
        self.balance_frame = tk.Frame(master)
        self.balance_frame.pack(side="left", padx=10, pady=10)

        self.balance_label = tk.Label(self.balance_frame, text="Obecny stan konta:")
        self.balance_label.pack(anchor="w", padx=10, pady=5)

        self.balance_value_label = tk.Label(self.balance_frame, text=f"{self.bank.amount}")
        self.balance_value_label.pack(anchor="w", padx=10, pady=5)


    def show_income_entry(self):
        self.clear_content()

        amount_label = tk.Label(self.master, text="Kwota:")
        amount_label.pack(anchor="w", padx=10, pady=5)

        self.amount_entry = tk.Entry(self.master)
        self.amount_entry.pack(anchor="w", padx=10, pady=5)

        name_label = tk.Label(self.master, text="Nazwa:")
        name_label.pack(anchor="w", padx=10, pady=5)

        self.name_entry = tk.Entry(self.master)
        self.name_entry.pack(anchor="w", padx=10, pady=5)

        confirm_button = tk.Button(self.master, text="Potwierdź", command=self.add_income_and_show_main_interface)
        confirm_button.pack(anchor="w", padx=10, pady=5)

    def show_expense_entry(self):
        self.clear_content()

        amount_label = tk.Label(self.master, text="Kwota:")
        amount_label.pack(anchor="w", padx=10, pady=5)

        self.amount_entry = tk.Entry(self.master)
        self.amount_entry.pack(anchor="w", padx=10, pady=5)

        name_label = tk.Label(self.master, text="Nazwa:")
        name_label.pack(anchor="w", padx=10, pady=5)

        self.name_entry = tk.Entry(self.master)
        self.name_entry.pack(anchor="w", padx=10, pady=5)

        confirm_button = tk.Button(self.master, text="Potwierdź", command=self.add_expense_and_show_main_interface)
        confirm_button.pack(anchor="w", padx=10, pady=5)

    def clear_content(self):
        for widget in self.master.winfo_children():
            widget.destroy()

    def add_income_and_show_main_interface(self):
        self.add_income()
        self.show_main_interface()

    def add_expense_and_show_main_interface(self):
        self.add_expense()
        self.show_main_interface()

    def add_income(self):
        new_income_amount = float(self.amount_entry.get())
        name = self.name_entry.get()
        new_income = Incomes(new_income_amount, name, self.bank)
        self.bank.amount += new_income.income
        self.show_balance()

    def add_expense(self):
        new_expense_amount = float(self.amount_entry.get())
        name = self.name_entry.get()
        if self.bank.amount - new_expense_amount < 0:
            print("Nie masz wystarczająco środków na tym koncie")
        else:
            new_expense = Expenses(new_expense_amount, name, self.bank)
            self.bank.amount -= new_expense.expense
            self.show_balance()

    def show_balance(self):
        self.clear_content()

        balance_label = tk.Label(self.master, text="Obecny stan konta:")
        balance_label.pack(anchor="w", padx=10, pady=5)

        balance_value_label = tk.Label(self.master, text=f"{self.bank.amount}")
        balance_value_label.pack(anchor="w", padx=10, pady=5)

    def add_account(self):
        print("Stworzysz teraz nowe konto bankowe")
        name = input("Podaj nazwę nowego konta bankowego: ")
        amount = float(input("Podaj kwotę, jaka ma znajdować się na tym koncie: "))
        self.bank = BankAccount(name, amount)
        self.show_balance()

    def quit(self):
        self.master.quit()

    def show_main_interface(self):
        self.clear_content()
        self.__init__(self.master)  # Re-creating the main interface

root = tk.Tk()
interface = Interface(root)
root.mainloop()
