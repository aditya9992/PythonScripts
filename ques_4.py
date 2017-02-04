from math import floor, ceil

def product(a,n):
    prod = 1

    m = 0
    while n > floor(n/2):
        prod = prod * a
        n -= 1
    while m < floor(n/2):
        prod = prod * a
        m += 1

    return prod

def prod1(a,n):
    prod = 1

    m = 0
    while n > 0:
        if n%2 != 0:
            prod *= a
        n = floor(n/2)
        a = a*a

    return prod