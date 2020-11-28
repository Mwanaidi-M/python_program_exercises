# accept input to determine number of contacts to be added
n = int(input())

#create a dictionary variable
d = dict()

#accept input from the user and add the input into the dictionary variable
for i in range(0, n):
    name, number = input().split()
    d[name] = int(number)

#accept input by looping through the input size for names to search for in the dictionary.
for i in range(0, n):
    try:
        name = input()
        if name in d:
            print(f"{name}={d[name]}")
        else:
            print("Not found")
    except:
        break
    

'''
Sample Input:

3
sam 99912222
tom 11122222
harry 12299933
sam
edward
harry

Sample Output:

sam=99912222
Not found
harry=12299933

'''
