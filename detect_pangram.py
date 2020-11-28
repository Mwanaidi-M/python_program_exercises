import string
def is_pangram(s):
    lett = set(string.ascii_letters)

    if s.__contains__(''.join(lett)):
        return True
    else:
        return False
    

print(is_pangram("The quick, brown fox jumps over the lazy dog!"))
print(is_pangram("ABCDE, FGRHIJK, MNOPQRSTUVWXYZ!"))
print(is_pangram("The quick, brown!"))
