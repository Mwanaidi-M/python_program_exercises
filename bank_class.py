"""Introduction to OOP in Python by creating a sample class Bank, that has attributes; accountHolder, accountName, accountNumber.
    -- Making a few modifications by adding the @property decorator.
    -- Properties are a pythonic way of working with class attributes.
    -- @property is the decorator used to provide special functionality to methods making them getters, setters, deleters when defining
    class properties.
    -- Its particularly important when making attributes private/protected and validating them before assigning them
    -- The getter is used to : [access the value of the attribute]
    -- The setter is used to :[set the value of the attribute]
    -- The deleter is used to :[delete the instance attribute]
    -- NB: the name of the property is "reused" for all three methods.
"""

class Bank:
            
    def __init__(self, accountNumber):
        self._accountNumber = accountNumber

    # GETTER
    @property #indicates that we're defining a property
    def accountNumber(self):
        return self._accountNumber #returns the value of the attr

    # SETTER ;The name of the property is included before .setter
    @accountNumber.setter #indicates that this is the setter method for the accountNumber property
    def accountNumber(self, accNum): #the name of the property is used as the name of the setter.
        if len(str(accNum)) == 5 :
            self._accountNumber = accNum
        else:
            print('Please give a valid account Number')

    # DELETER
    @accountNumber.deleter #indicateS that this is the deleter method for the accountNumber property
    def accountNumber(self): #This method only has one formal parameter defined, self.
        del self._accountNumber #The body, where we delete the instance attribute

'''
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

'''