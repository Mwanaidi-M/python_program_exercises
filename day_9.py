# defining my function that accepts an integer.
def factorial(num):
    # if the integer is 1 then the function returns the value 1
    if num ==1:
        return num
    #if the intege ris not 1 then it calculates the factorial by calling the same function we created subtracting 1 from the integer.
    else:
        return num * factorial(num -1)
         
'''
Sample Input

3

Sample Output

6
'''

print(factorial(6))
