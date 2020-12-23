from bank_class import Bank

# Instantiating an object
mary = Bank('Mary', 'Fixed', 9011234)
james = Bank('James', 'Savings', 9011567)

# accessing a class attribute
print(f'Mary just opened an account at {mary.__class__.bankName}')

# accessing instance attributes
print(f'James\' account Type: {james.accountName}, account Number: {james.accountNumber}')

# accessing instance methods
print(f'{mary.deposit()}')
print(f'{james.withdraw()}')