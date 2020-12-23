import string, random

while True:
    welcome_msg = '------------------------- M\'S RANDOM PASSWORD GENERATOR -----------------------------------'
    print(welcome_msg, '\n')
    print('1. 8 Character Password')
    print('2. 16 Character Password')
    print('3. 32 Character Password')
    print('4. Exit \n')
    
    try:
        user_input = int(input('Please Enter your preference: \t'))
        all_chars = string.ascii_letters + string.digits + string.punctuation
        
        if user_input == 1:
            new_password = ''.join(random.sample(all_chars, 8))
            print('Your Password: {}'.format(new_password), '\n')

        elif user_input == 2:
            new_password = ''.join(random.sample(all_chars, 16))
            print('Your Password: {}'.format(new_password), '\n')

        elif user_input == 3:
            new_password = ''.join(random.sample(all_chars, 32))
            print('Your Password: {}'.format(new_password), '\n')

        elif user_input == 4:
            print('Bye! ')
            break

        else:
            print('Please enter a number on the menu')
    except:
        print('Please enter a number')
        continue
    

    
    
