def palindrome(s):
    ''' Function to check if a string is a palindrome. A palindrome is a word
    that spells the same forward and backward'''

    #use casefold to make the string suitable for caseless comparison
    s = s.casefold()

    #convert the str to a list and hold it in a variable
    frwd_str = list(s)

    #use reversed() to make a reverse iterator str characters.
    #wrap it in a list and hold it in a variable
    reverse_str = list(reversed(s))

    #compare both variables for equality
    if frwd_str == reverse_str:
        return f'{s} is indeed a palindrome'
    else:
        return f'{s} is not a palindrome'

print(palindrome('madam'))
print(palindrome('mum'))
print(palindrome('papa'))
