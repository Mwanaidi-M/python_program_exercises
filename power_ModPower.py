# Powers or exponents in Python can be calculated using the built-in power function 'pow()'
#  pow(a,b) ,  pow(a,b,m) 

num = int(input('Numerator:\t'))
den = int(input('Denominator:\t'))
mod = int(input('Mode:\t'))

print(pow(num, den),'\n',pow(num, den, mod))