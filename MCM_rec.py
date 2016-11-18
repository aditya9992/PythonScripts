import sys, time, random


def matrix_chain_recursive(a,i,j):

    if i == j:
        return 0
    else:
        x = sys.maxsize
        for k in range(i,j):
            cost = matrix_chain_recursive(a,i,k) + matrix_chain_recursive(a,k+1,j) + a[i-1]*a[k]*a[j]
            if cost < x:
                x = cost
    return x



def main():
    if sys.argv[1] == 'rand':
        p = [random.randint(1, 100) for e in range(int(sys.argv[2]))]
        b = time.time()
        print(matrix_chain_recursive(p, 1, len(p)-1))
        print('total run time is:', time.time() - b)
    elif sys.argv[1] == 'recursive':
        p = [int(s) for s in sys.argv[2].split(',')]
        b = time.time()
        print(matrix_chain_recursive(p, 1, len(p)-1))
        print('total run time is:', time.time() - b)


if __name__ == '__main__':
    main()

