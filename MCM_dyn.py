import sys, time, random



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
    return s[1][len(p)-1]


def main():
    if sys.argv[1] == 'rand':
        p = [random.randint(1, 100) for e in range(int(sys.argv[2]))]
        b = time.time()
        print(matrix_chain_dynamic(p, len(p)))
        print('total run time is:', time.time() - b)
    elif sys.argv[1] == 'dynamic':
        p = [int(s) for s in sys.argv[2].split(',')]
        b = time.time()
        print(matrix_chain_dynamic(p,len(p)))
        print('total run time is:', time.time() - b)

if __name__ == '__main__':
    main()
