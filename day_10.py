''' Given a base-10 integer,n , convert it to binary (base-2). Then find and
print the base-10 integer denoting the maximum number of consecutive 1's in n's
binary representation.'''

#accept integer to convert
n = int(input())

#convert the integer to binary
m = '{:b}'.format(n)

# split the binary number where '0' is found, get the max number of '1'
# from the length of the value
num = max(map(len, m.split('0')))
    
print(num)
