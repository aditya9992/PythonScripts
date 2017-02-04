
# Program to find the shortest path on basis of weighted graphs
def funct(arr):
    for i in range(1,len(arr)):
        j = len(arr)
        while j > i+1:
            if arr[j] < arr[j-1]:
                temp = arr[j-1]
                arr[j-1] = arr[j]
                arr[j] = temp
            j -= 1
    return arr


def count_sort(arr,k):
    n = k + 1
    c = [0] * n
    b = [0] * len(arr)
    i = 0
    s = 0

    for j in arr:
        c[j] = c[j] + 1

    while i < len(arr):
            if c[s] == 0:
                s += 1
            if c[s] > 0:
                b[i] = s
                i += 1
                c[s] -= 1
    return b



def print_array(arr):

    for i in range(len(arr)):
        if arr[i] != 0:
            x = range(1 * arr[i])
            for j in x:
                print(i)


def printarr(arr,c):
    b = [0]*len(arr)

    for i in range(1,len(c)):
        c[i] = c[i-1] + c[i]
    for j in range(len(arr),1,-1):
        b[c[arr[j]]] = arr[j]
        c[arr[j]] = c[arr[j]] - 1
    return b