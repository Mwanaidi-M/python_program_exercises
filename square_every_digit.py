def square_digit(num):
    nl = []
    s_num = num.__str__()
    for n in s_num:
        m = int(n) * int(n)
        nl.append(m.__str__())
    return(int(''.join(nl)))

print(square_digit(9119))
