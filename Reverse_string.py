import sys

print(sys.argv[1])

print(sys.argv[1])

def rev_string(str):

    str1 = str

    i = 0
    j = len(str1) - 1

    while i < j:
        temp = str1[i]
        str1[i] = str1[j]
        str1[j] = temp
        i = i + 1
        j = j - 1

    print(str1)
