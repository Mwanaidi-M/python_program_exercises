for i in range(5):
    for c in range(i):
        print('x', end=' ')
    print()

print()

for i in range(1,6):
    for c in range(1,i+1):
        print(c, end=' ')
    print()

print()

for i in range(1,6):
    for c in range(i):
        print(i, end=' ')
    print()
    
print()

for i in range(5,0,-1):
    for c in range(1, i+1):
        print(i, end=' ')
    print()

print()

for i in range(5,0,-1):
    for c in range(1, i+1):
        print(c, end=' ')
    print()
    
print()

k = 2*6 -2
for i in range(6):
    for c in range(0,k):
        print(end=' ')
    k-=1
    for c in range(1,i+1):
        print('*', end=' ')
    print()
