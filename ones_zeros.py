'''
    to convert an array of int from their binary values to integers;
    use int(x, y) where y = (base=2)
'''
def binary_array_to_number(arr):
    '''print (int("".join(map(str, arr)), 2))'''
    print(int(''.join(str(a) for a in arr),2))
    

binary_array_to_number([0,0,0,1])
binary_array_to_number([0,0,1,0])
binary_array_to_number([1,1,1,1])
