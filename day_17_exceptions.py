class Calculator:
    def power(self,n,p):
        #check if either n or p is negative
        if n < 0 or p < 0:
            #raising the exception if either of the values is negative
            raise Exception('n and p should be non-negative')
        else:
            # returning the value of n to the power of p
            return n ** p


cl1 = Calculator()
T = int(input()) #number of test cases to be input
#looping though every test case
for i in range(T):
    #create two variables as the input is space-separated
    n, p = map(int, input().split())
    try:
        ans = cl1.power(n,p)
        print(ans)
    except Exception as e:
        print(e)


'''
Sample Input

4
3 5
2 4
-1 -2
-1 3
Sample Output

243
16
n and p should be non-negative
n and p should be non-negative
'''
