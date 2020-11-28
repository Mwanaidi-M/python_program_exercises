#integer input for the number of test cases
N = int(input())

#variables to hold the even and odd indexed characters; I used lists.
index_even = []
index_odd = []

#looping through each test case
for i in range(0,N):
    #input for the string
    string = input() 

    #empty the lists if they hold any strings 
    index_even.clear()
    index_odd.clear()

    #loop through the string; item(index value) and char(character value)
    #enumerate() method eases looping through the string
    for item , char in enumerate(string):

        #conditional to check if the index is odd or even.
        #if even, the character is added to the index_even list respectively
        if item % 2 == 0:
            index_even.append(char)
        else:
            index_odd.append(char)

    #transform the characters in the list to form a single word.
    print(''.join(index_even), ''.join(index_odd))
        


