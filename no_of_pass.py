l_case = list('abcdefghijklmnopqrstuvwxyz')
u_case = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
nums = list('1234567890')
s_char = list('~!@#$%^&*()_+|}{:"<>?`[]\';/.,')


def ranpass():
    new = ''
    for i in range(5):
        l_case.extend(u_case)
        n = random.choice(l_case)
        new += ''.join(n)
    print(new)
    
import random

sz = 1
while sz <=3:
    ranpass()
    sz +=1

    
