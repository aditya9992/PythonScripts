import sys, time

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

    return m

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
    s1 = [[0 for x in range(1,n-1)] for x in range(2,len(n))]

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
                    s1[i][j] = k
    return s, s1

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

lm1 = lambda i,j:str(i)+','+str(j)

def mcm(p):
    n = len(p) - 1
    m = {}
    for i in range(1, n + 1):
        for j in range(i, n + 1):
            m[gk(i, j)] = sys.maxsize

    return lookupchain(m,p,1,n)

def lookupchain(m,p,i,j):
    if m[gk(i,j)] < sys.maxsize:
        return m[gk(i,j)]
    if i == j:
        m[gk(i,j)] = 0
    else:
        for k in range(i,j):
            q = lookupchain(m,p,i,k) + lookupchain(m,p,k+1,j) + p[i-1]*p[k]*p[j]
            if q < m[gk(i,j)]:
                m[gk(i,j)] = q
    return m[gk(i,j)]

def main():
    p = [30,35,15,5,10,20,25,5,16,34,28,19,66,34,78,55,23]
    print(mcm(p))

if __name__ == '__main__':
    b = time.time()
    main()
    print('total run time is:', time.time()-b)

def printp(s,i,j):
    if i==j:
        print('A' + str(i))
    else:
        print('(' + str(printp(s,i,s[i][j])) + str(printp(s,s[i][j]+1,j))+ ')')