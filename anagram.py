# Program to find whether a string is anagram of other one
import sys

def anagramfind(s1, s2):    
    k1 = list(s1)
    k2 = list(s2)
    k1.sort()
    k2.sort()
    if k1 == k2:
        return True
    else:
        return False


s1, s2 = sys.argv[1], sys.argv[2]
anagramfind(s1, s2)


# Function without sorting functionality
def stringreplace(s1):
    s1 = list(s1)
    for i in range(len(s1)):
        if s1[i] == ' ':
            s1[i] = '%20'
    s1 = ''.join(s1)
    return s1

def compressstring(s1):
    s2 = list(s1)
    s2.sort()
    print(s2)
    j = 1
    s3 = []
    i = 0
    while i < len(s2):
        if s2[i] == s2[i+1]:
            j += 1
        else:
            s3.append(s2[i-1])
            s3.append(str(j+1))
            j = 1
        i = j + 1
    print(s3)
    s2 = ''.join(s3)
    print(s2)
    if len(s2) < len(s1):
        print(s2)
    else:
        print(s1)

def matcolrow(mat1):
    i = 0
    j = 0
    for row in mat1:
        j += 1
        for col in row:
            i += 1
            if col == 0:
            