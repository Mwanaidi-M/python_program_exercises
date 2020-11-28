import os

name = input().strip()
def create_acc():
    '''create a user txt file'''
    with open(f'{name}.txt','w') as newone:
        newone.write(f'Name:{name}')

def add_acc_info():
    ''' add information to the user account file if it exists ''' 
    try:
        if os.path.exists(f'{name}.txt'):
            with open(f'{name}.txt','a') as no:
                no.write('\nIt works so far') 
            print(True)
        else:
            print('file does not exists')
    except:
        print('nothin')


