def num_func(n):
    ''' This function is supposed to print consecutive numbers within the range
    of the given number. eg fun(5) >>> 12345'''
    for i in range(1,n+1):
        print(i, end='')

#num_func(3)

def list_comprehension():
    '''
    Let's learn about list comprehensions! You are given three integers x,y and
    z representing the dimensions of a cuboid along with an integer n. Print a
    list of all possible coordinates given by (i,j,k) on a 3D grid where the
    sum of (i+j+k) is not equal to n.
    '''
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())

    cuboid = [[a,b,c] for a in range(x+1) for b in range(y+1) for c in range(z+1) if (a+b+c)!= n]

    print(cuboid)

list_comprehension()
    
'''
Sample Input 0

1
1
1
2
Sample Output 0

[[0, 0, 0], [0, 0, 1], [0, 1, 0], [1, 0, 0], [1, 1, 1]]
'''
