def prime_number():
    num_size = int(input())
    num_arr = []
    for i in range(num_size):
        y = input()
        num_arr.append(int(y))
        
    for num in num_arr:
        if(num % 2) == 0:
            print(f'{num} is not a prime number.')
            
        else:
            print(f'{num} is a prime number.')

prime_number()

'''
Sample Input

3
12
5
7
Sample Output

Not prime
Prime
Prime

'''
