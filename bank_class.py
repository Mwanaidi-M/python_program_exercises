"""Introduction to OOP in Python by creating a sample class Bank, that has attributes; accountHolder, accountName, accountNumber
"""

class Bank:
    # class attribute
    bankName = 'KCB'

    # instance attribute
    def __init__(self, accountHolder, accountName, accountNumber):
        self.accountHolder = accountHolder
        self.accountName = accountName
        self.accountNumber = accountNumber

    # instance methods
    def deposit(self):
        return f'{self.accountHolder} would like to make a deposit.'

    def withdraw(self):
        return f'{self.accountHolder} would like to make a withdrawal.'