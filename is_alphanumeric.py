def alphanumeric(password):
    if password.isalnum() == True:
        return True
    else:
        return False

print(alphanumeric('hello_jum'))
