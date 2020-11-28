#value whose multiplication table you would like
n = int(input())

#value from which multiplication begins
i = 1

#looping through i while it is in the range of 1 to 11
#11 is the stop value and will not be included in the multiplication
while i in range(1,11):

    #res variable hold the result of multiplication
    res = n * i
    print(f'{n} x {i} = {res}')

    #keep on increasing the value of i as you continue.
    i += 1
