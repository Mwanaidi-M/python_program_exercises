# NOT FINISHED OR SOLVED
size = int(input('How many students are you giving?\t'))


outerlist = []

for st in range(size):
    name = input('Name:\t')
    marks = float(input('Marks:\t'))

    nm = [name, marks]
    outerlist.append(nm)

sd = set(outerlist)
print(outerlist, sd)

