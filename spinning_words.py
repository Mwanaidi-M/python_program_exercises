def spin_words(sentence):
    # Your code goes here
    m = []
    lsent = list(sentence.split(' ' ))
    for l in lsent:
        if len(l) >= 5:
            m.append(l[::-1])
        else:
            m.append(l)
        n = ' '.join(m)
    return n

print(spin_words('Welcome'))
print(spin_words("Hey fellow warriors"))
