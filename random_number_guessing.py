#imported the random number
import random
def random_number():
    '''
    This is a guessing game method. Basically it prompts the user to choose the range within which they want to guess and then gives them 3 chances to guess the correct number
    '''
    intro = '-------------------------NUMBER GUESSING GAME---------------------------'
    print(f'{intro}')

    #use a while loop to run infinitely until the user chooses to exit
    while True:
        print('1. Play')
        print('2. Help')
        print('3. Quit')
        user_chances = 3 #assign the number of chances
        try:
            user_input = int(input('Enter your selection: \t')) #user enters menu selection

            if user_input == 1:
                min_numrange = int(input('Choose minumum number: \t')) #user enters minimum range index
                max_numrange = int(input('Choose maximum number: \t')) #user enters maximum range index

                ran_num = random.randint(min_numrange,max_numrange)
                
                while user_chances >= 1:
                    user_chances = user_chances-1

                    user_number = int(input(f'Guess a random number between {min_numrange} and {max_numrange}: \t'))
                    if user_number < ran_num:
                        print('Oh No...That value is too small')
                        print(f'Chances left: {user_chances}\n')
                    
                    elif user_number > ran_num:
                        print('Wow ... That\'s huge')
                        print(f'Chances left: {user_chances}\n')
                    
                    elif user_number == ran_num:
                        print('Perfect you got it.')
                        break
                    if user_chances == 0:
                        print(f'You\'re out of trials.\nThe number was {ran_num}\n')
                        
                                       

            elif user_input == 2:
                print('''
    This is a random number guessing game and the instructions are simple.
    Step 1: Choose option 1(Play) to start the game. You have three chances to guess the correct number.
    Step 2: Enter the values for the range within which you would like to guess; a minimum number and a maximum number.
    Step 3: Enter a random number that you think could be the number we're looking for and if you guess correctly, YOU WIN!!!
                    ''')
                continue
            elif user_input == 3:
                return 'Bye!'
                break
            else:
                print('Ooops, That number is not in the menu')
                continue

        except:
            print('Sorry Wrong Input')
            continue
    
print(random_number())
