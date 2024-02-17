from datetime import datetime


class BankAccount:
    def __init__(self, account_number, balance, date_of_opening: datetime, customer_name):
        if balance < 0:
            raise RuntimeError("Баланс не может быть отрицательным!")
        if account_number < 0:
            raise RuntimeError("Номер не может быть отрицательным!")
        if not isinstance(date_of_opening, datetime):
            raise TypeError("Дата создания должна быть введена в формате ")
        self.account_number = account_number
        self.balance = balance
        self.date_of_opening = date_of_opening.date()
        self.customer_name = customer_name

    def deposit(self, inc):
        self.balance = self.balance + inc

    def print_info(self):
        print("account_number:", self.account_number)
        print("balance:", self.balance)
        print("date_of_opening:", self.date_of_opening)
        print("customer_name:", self.customer_name)
        print("=" * 15)

    def windraw(self, dec):
        if (self.balance - dec < 0) or (self.balance <= 0):
            print("Операция отклонена, недостаточно средств для вывода!")
        else:
            self.balance = self.balance - dec


a1 = BankAccount(1, 2, datetime.strptime("01-01-2001", '%d-%m-%Y'), 'Sasha')
a2 = BankAccount(2, 0, datetime.strptime("02-02-2002", '%d-%m-%Y'), 'Dima')
a3 = BankAccount(3, 100, datetime.strptime("03-03-2003", '%d-%m-%Y'), 'Kolya')
a4 = BankAccount(4, -10, datetime.strptime("04-04-2004", '%d-%m-%Y'), 'Sasha')
a1.print_info()
a1.windraw(1)
a1.print_info()
print("======")
a2.print_info()
a2.windraw(1)
a2.print_info()
print("=======")
a3.print_info()
a3.deposit(100)
a3.print_info()
