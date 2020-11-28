# input the size of your list as an integer
n = int(input())

#user inputs the values
#strip() removes any leading or trailing whitespace
#split(' ') separates the values using space
#the values are then added to the arr list

'''arr = []

num = input().strip()
for nu in num.split(' '):
    arr.append(int(nu))'''
arr = list(int(i) for i in input().strip().split(' '))

#loop through the reversed list and print the output 
for x in reversed(arr):
    print(x, end=' ')
