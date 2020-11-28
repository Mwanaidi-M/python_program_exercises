''' Given an array, find the integer that appears an odd number of times.

There will always be only one integer that appears an odd number of times.'''


def find_it(seq):
    #loop thru each item in the sequence
    for i in seq:
        #if the no. of appearances if an element is an odd number assign it to a variable
        if seq.count(i) % 2 != 0:
            num = i
        #else pass that            
        else:
            pass
    #returns the resultant value
    print(num)

find_it([20,1,-1,2,-2,3,3,5,5,1,2,4,20,4,-1,-2,5])
find_it([1,1,2,-2,5,2,4,4,-1,-2,5])
find_it([20,1,1,2,2,3,3,5,5,4,20,4,5])



