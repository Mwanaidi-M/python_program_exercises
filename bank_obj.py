from bank_class import Bank

# Instantiating an object
# mary = Bank('Mary', 'Fixed', 9011234)
# james = Bank('James', 'Savings', 9011567)

# # accessing a class attribute
# print(f'Mary just opened an account at {mary.__class__.bankName}')

# # accessing instance attributes
# print(f'James\' account Type: {james.accountName}, account Number: {james.accountNumber}')

# # accessing instance methods
# print(f'{mary.deposit()}')
# print(f'{james.withdraw()}')

mar = Bank(23) # Create instance
print(mar.accountNumber) # Access value

mar.accountNumber = 90000 # Update value

# If we try to assign an invalid value, we see the descriptive message that was specified in the setter
#  mar.accountNumber = 908

#  Delete the instance attribute
#  del mar.accountNumber