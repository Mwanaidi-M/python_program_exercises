'''
Given an integer,n , and n space-separated integers as input, create a
tuple,t , of those n integers. Then compute and print the result of hash(t).
'''
n = int(input())
integer_list = map(int, input().split())

tup = tuple(integer_list)
print(hash(tup))

'''
Sample Input 0

2
1 2
Sample Output 0

3713081631934410656
'''
