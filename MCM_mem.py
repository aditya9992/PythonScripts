import sys, time, random


lm1 = lambda i,j:str(i)+','+str(j)
def matrix_chain_memoize(p):
    n = len(p) - 1
    m = {}
    for i in range(1, n + 1):
        for j in range(i, n + 1):
            m[lm1(i, j)] = sys.maxsize

    return lookupchain(m,p,1,n)

def lookupchain(m,p,i,j):
    if m[lm1(i,j)] < sys.maxsize:
        return m[lm1(i,j)]
    if i == j:
        m[lm1(i,j)] = 0
    else:
        for k in range(i,j):
            q = lookupchain(m,p,i,k) + lookupchain(m,p,k+1,j) + p[i-1]*p[k]*p[j]
            if q < m[lm1(i,j)]:
                m[lm1(i,j)] = q
    return m[lm1(i,j)]

def main():
        if sys.argv[1] == 'rand':
            p = [random.randint(1, 100) for e in range(int(sys.argv[2]))]
            b = time.time()
            print(matrix_chain_memoize(p))
            print('total run time is:', time.time() - b)
        elif sys.argv[1] == 'memoized':
            p = [int(s) for s in sys.argv[2].split(',')]
            b = time.time()
            print(matrix_chain_memoize(p))
            print('total run time is:', time.time() - b)

if __name__ == '__main__':
    main()
