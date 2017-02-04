lenA = input()
lenB = input()

if lenA < 1 and lenA > 1000010:
    lenA = input("Enter length of A again: ")
if lenB < 1 and lenB > 1000010:
    lenB = input("Enter length of B again: ")

a = [input()]
b = [input()]
c = []
matC = [[0 for x in range(2)] for y in range(len(b))]

# Function to find the elements which are not in the second list

for j in len(b):
    matC[j][0] = b[j]
    matC[j][1] = 0

for m in len(b):
    for k in len(b):
        if b[m] == b[k]:
            matC[m][1] = 1

for n in len(a):
    for s in len(b):
        if a[n] == b[k]:
            matC[n][1] = 0

for x in len(b):
    if matC[x][1] == 1:
        c.append(matC[x][0])

print(c)
