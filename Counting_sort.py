import sys


arr = [int(s) for s in sys.argv[1].split(',')]

c = []

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