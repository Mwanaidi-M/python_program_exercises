def checknum(N):
    if N%2 == 0  and N in range(2,5):
        print('Not Weird')
    elif N%2 == 0  and N in range(6,20):
        print('Weird')
    elif N%2 == 0  and N> 20:
        print('Not Weird')
    else:
        print('Weird')

checknum(3)
checknum(24)
checknum(38)
checknum(14)

