import sys


arr = [int(s) for s in sys.argv[1].split(',')]

def count_sort(arr,k):
    n = k + 1
    c = [0] * n

    for j in arr:
        c[j] = c[j] + 1

    return c

def print_array(arr):

    for i in range(len(arr)):
        if arr[i] != 0:
            x = range(1 * arr[i])
            for j in x:
                print(i)


# Hackerrank Problem

p = int((input()))
ar1 = input()
str1 = ''

arr = [int(s) for s in ar1.split(' ')]

k = p + 1
if k >= 100 and k <= 1000000:
    c = [0] * (k - 1)

for j in arr:
    if arr[j] >= 0 and arr[j] < 100:
        c[j] = c[j] + 1

for i in range(0, len(c)):
    str1 += str(c[i])
    if i != len(c) - 1:
        str1 += " "
print(str1)
