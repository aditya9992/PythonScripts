# Code for finding all the palindromes in a string

def distpalindromeString(s): 
    m = dict()
    n = len(s)
 
    # table for storing results (2 rows for odd-
    # and even-length palindromes
    R = [[0 for x in range(n+1)] for x in range(2)]
 
    # Find all sub-string palindromes from the given input
    # string insert 'guards' to iterate easily over s
    s = "@" + s + "#"
 
    for j in range(2):
        rp = 0    # length of 'palindrome radius'
        R[j][0] = 0
 
        i = 1
        while i <= n:
 
            # Attempt to expand palindrome centered at i
            while s[i - rp - 1] == s[i + j + rp]:
                rp += 1 # Incrementing the length of palindromic
                        # radius as and when we find valid palindrome
 
            # Assigning the found palindromic length to odd/even
            # length array
            R[j][i] = rp
            k = 1
            while (R[j][i - k] != rp - k) and (k < rp):
                R[j][i+k] = min(R[j][i-k], rp - k)
                k += 1
            rp = max(rp - k, 0)
            i += k
 
    # remove guards
    s = s[1:len(s)-1]
 
    # Put all obtained palindromes in a hash map to
    # find only distinct palindrome
    m[s[0]] = 1
    for i in range(1,n):
        for j in range(2):
            for rp in range(R[j][i],0,-1):
                m[s[i - rp - 1 : i - rp - 1 + 2 * rp + j]] = 1
        m[s[i]] = 1
 
    # printing all distinct palindromes from hash map
    print("Below are %d pali sub-strings"%len(m))
    for i in m:
        print(i)
    

def palindromeString(string1):

    val = list(string1)
    j = 0
    k = 1
    m = []
    temp = []
    for i in range(len(val)):
        j = i - 1
        k = i + 1
        if (j < 0 or k > len(val) + 1):
            m.append((val[i]))
        if val[j] == val[k]:
            temp.append(val[j])
            temp.append(val[i])
            temp.append(val[k])
            j += 1
            k += 1

    return True