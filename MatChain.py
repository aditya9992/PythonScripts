import sys

def MatrixChainDynamic(p, n):
    # 0th row and column are used for the sake of evaluating
    m = [[0 for x in range(n)] for x in range(n)]

    # m[i,j] = Minimum number of scalar multiplications needed
    # to compute the matrix A[i]A[i+1]...A[j] = A[i..j] where
    # dimension of A[i] is p[i-1] x p[i]


    for i in range(1, n):
        m[i][i] = 0

    for j in range(1,n-1,-1):
        for k in range(j+1,n):
            m[j][k] = 1000
            for o in range(j,k):
                c = m[j][o] + m[o+1][k] + p[j-1]*p[o]*p[k]

                if c < m[j][k]:
                    m[j][k] = c

    return m[1][n - 1]

p = [1,2,3,4]

s = [[0 for x in range(len(p))] for x in range(len(p))]

def matrix_chain_recursive(a,i,j):

    if i == j:
        s[i][i] = 0
    else:
        s[i][j] = sys.maxsize
        for k in range(i,j):
            cost = matrix_chain_recursive(a,i,k) + matrix_chain_recursive(a,k+1,j) + p[i-1]*p[k]*p[j]
            if cost < s[i][j]:
                s[i][j] = cost
    return s[1][len(p)-1]

def matrix_chain_dynamic(p,n):
    s = [[0 for x in range(n)] for x in range(n)]


    for i in range(1, n):
        s[i][i] = 0
    for L in range(2,n):
        for i in range(1,n-L+1):
            j = i + L - 1
            s[i][j] = sys.maxsize
            for k in range(i,j):
                cost = s[i][k] + s[k+1][j] + p[i-1]*p[k]*p[j]

                if cost < s[i][j]:
                    s[i][j] = cost
    return s[1][n-1]

def matrix_chain_memoizing(p,i,j):
    if s[i][j] != 0:
        return s[i][j]
    else:
        if i==j:
            s[i][i] = 0
        else:
            s[i][j] = sys.maxsize
            for k in range(i,j-1):
                cost = matrix_chain_memoizing(p,i,k) + matrix_chain_memoizing(p,k+1,j) + p[i-1]*p[k]*p[j]
                if cost < s[i][j]:
                    s[i][j] = cost
    return s[1][len(p)-1]