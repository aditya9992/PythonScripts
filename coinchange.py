def count(arr,c,num):
    tab = [[0 for x in range(c)] for x in range(num+1)]

    for i in range(c):
        tab[0][i] = 1

    for i in range(1, num + 1):
        for j in range(c):
            # Count of solutions including S[j]
            x = tab[i - arr[j]][j] if i - arr[j] >= 0 else 0

            # Count of solutions excluding S[j]
            y = tab[i][j - 1] if j >= 1 else 0

            # total count
            tab[i][j] = x + y

    return tab[c][num - 1]

def min1(x1,x2):
    if x2 > x1:
        return x1
    else:
        return x2

def ct(C, num):
    tab = [0] * (num+1)
    x = 1

    while x< len(tab):
        tab[x] = 100
        x +=1

    m = len(C)
    j = 1
    while j < (num+1):
        i = 0
        while i < m:
            if j-C[i] >= 0:
                z = tab[j-C[i]] + 1
                tab[j] = min1(z,tab[j])
            i += 1
        j += 1

    return tab


def count1(S, m, n):
    # We need n+1 rows as the table is consturcted in bottom up
    # manner using the base case 0 value case (n = 0)
    table = [[0 for x in range(m)] for x in range(n + 1)]

    # Fill the enteries for 0 value case (n = 0)
    for i in range(m):
        table[0][i] = 1

    # Fill rest of the table enteries in bottom up manner
    for i in range(1, n + 1):
        for j in range(m):
            # Count of solutions including S[j]
            x = table[i - S[j]][j] if i - S[j] >= 0 else 0

            # Count of solutions excluding S[j]
            y = table[i][j - 1] if j >= 1 else 0

            # total count
            table[i][j] = x + y

    return table[n][m - 1]