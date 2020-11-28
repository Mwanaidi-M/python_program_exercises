''' Question was to replace the alphabets with their numerical position'''

def alphabet_position(text):
    '''made two lists, one for the alphabets, the other for the numbers'''
    lett = list('abcdefghijklmnopqrstuvwxyz')
    val = [x for x in range(1,27)]

    '''made a dictionary of both lists the letters are the keys and numbers are values'''
    alph = dict(zip(lett,val))

    '''print(lett)
    print(val)
    print(alph)'''

    ''' made the sentence into lowercase and removed any spaces in between
    and put it in a list'''
    txt =text.lower().replace(' ', '')
    #print(txt)

    numtxt = []
    '''empty list to hold the sentence characters
     loop thru the list and check if any character is a key in the dict.
    If it is the the value of that key is added to the empty list.
    Finally join the list to form a sentence of the numeric values.'''
    for t in txt:
        if t in alph.keys():
            numtxt.append(str(alph.get(t)))
    print(' '.join(numtxt))

alphabet_position('hello')
alphabet_position("The sunset sets at twelve o' clock.")
alphabet_position("The narwhal bacons at midnight.")
