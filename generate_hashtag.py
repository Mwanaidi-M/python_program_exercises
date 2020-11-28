'''
It must start with a hashtag (#).
All words must have their first letter capitalized.
If the final result is longer than 140 chars it must return false.
If the input or the result is an empty string it must return false.
'''

def generate_hashtag(stmt):
    if len(stmt) == 0 or len(stmt)>140:
        return False
    else:
        print('#'+stmt.title().replace(' ', ''))
    
generate_hashtag('hello')
generate_hashtag('Do We have A Hashtag')
generate_hashtag("    Hello     World   " )
