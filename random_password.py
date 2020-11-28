import random

def random_password():
    
    l_case = list('abcdefghijklmnopqrstuvwxyz')
    u_case = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    nums = list('1234567890')
    s_char = list('~!@#$%^&*()_+|}{:"<>?`[]\';/.,')
    new = ''
    try:
        print('--------------- RANDOM PASSWORD GENERATOR ---------------\n')
        print('1. Include Uppercase letters.')
        print('2. Include Numbers.')
        print('3. Include Special Characters.')
        pref = int(input('What is your preference:\t'))
        print()
        if pref == 1:
            print('1. 8 - Characters')
            print('2. 16 - Characters')
            print('3. 32 - Characters')
            size = int(input('What length would you prefer?\t'))
            if size == 1:
                for i in range(8):
                    l_case.extend(u_case)
                    n = random.choice(l_case)
                    new += ''.join(n)
                print(f'New Password: {new}')
            elif size == 2:
                for i in range(16):
                    l_case.extend(u_case)
                    n = random.choice(l_case)
                    new += ''.join(n)
                print(f'New Password: {new}')
            elif size == 3:
                for i in range(32):
                    l_case.extend(u_case)
                    n = random.choice(l_case)
                    new += ''.join(n)
                print(f'New Password: {new}\n')
            else:
                print('Wrong Input')

        elif pref == 2:
            print('1. 8 - Characters')
            print('2. 16 - Characters')
            print('3. 32 - Characters')
            size = int(input('What length would you prefer?\t'))
            if size == 1:
                for i in range(8):
                    l_case.extend(nums)
                    n = random.choice(l_case)
                    new += ''.join(n)
                print(f'New Password: {new}')
            elif size == 2:
                for i in range(16):
                    l_case.extend(nums)
                    n = random.choice(l_case)
                    new += ''.join(n)
                print(f'New Password: {new}')
            elif size == 3:
                for i in range(32):
                    l_case.extend(nums)
                    n = random.choice(l_case)
                    new += ''.join(n)
                print(f'New Password: {new}\n')
            else:
                print('Wrong Input')

        elif pref == 3:
            print('1. 8 - Characters')
            print('2. 16 - Characters')
            print('3. 32 - Characters')
            size = int(input('What length would you prefer?\t'))
            if size == 1:
                for i in range(8):
                    l_case.extend(s_char)
                    n = random.choice(l_case)
                    new += ''.join(n)
                print(f'New Password: {new}')
            elif size == 2:
                for i in range(16):
                    l_case.extend(s_char)
                    n = random.choice(l_case)
                    new += ''.join(n)
                print(f'New Password: {new}')
            elif size == 3:
                for i in range(32):
                    l_case.extend(s_char)
                    n = random.choice(l_case)
                    new += ''.join(n)
                print(f'New Password: {new}\n')
            else:
                print('Wrong Input')
        else:
            print('Wrong Entry')

    except:
        print('Invalid Entry')
while True:
    random_password()
    q = input('Press \'q\' or \'Q\' to exit program or any key to continue\t')
    if q == 'q' or q == 'Q':
        print('BYE')
        break
    else:
        continue
