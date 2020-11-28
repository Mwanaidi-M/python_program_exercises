'''
Bank Applicationt that incorporates files. How it works:
- Application starts and displays the menu.
- If the user has no account, they fill in their name, enter a PIN, deposit some
money(1500 min) and the details are saved to a file.
- if the user has an account, they enter their PIN and access their file.
-User can deposit any amount they wish (100 min)
-Withdrawals can only be done if the user has sufficient funds
- User can view the balance if they wish

'''

def bank_application():
    menu_heading = 'ASD BANK'
    
    print(menu_heading.center(40, '-'))
    print('1. Create Account')
    print('2. Deposit Money')
    print('3. Withdraw Money')
    print('4. Check Balance')
    print('5. Exit')

    try:
        menu_option = int(input('Input your selection:\t'))

    except:
        print('Wrong Input')



bank_application()
