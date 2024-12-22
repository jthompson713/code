class BankAccount:
    def __init__(self, firstname, lastname, accountid, accounttype, pin, balance):
        self.firstname = firstname
        self.lastname = lastname
        self.accountid = accountid
        self.accounttype = accounttype
        self.pin = pin
        self.balance = balance
    def deposit(self):
        user_deposit = int((input('Enter an amount to deposit: ')))
        answer = int(self.balance) + int(user_deposit)
        self.balance = answer
    def withdraw(self):
        user_withdraw = (input('Enter an amount to withdraw: '))
        answer = int(self.balance) - int(user_withdraw)
        self.balance = answer

    def display_balance(self):
        print('Your balance is: $',self.balance)

wells_checking = BankAccount('Jared', 'Thompson', '12232453', 'Checking', '8745', '1098')

wells_checking.display_balance()
wells_checking.deposit()
wells_checking.withdraw()

wells_checking.display_balance()

