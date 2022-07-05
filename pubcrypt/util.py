from random import randrange

def invmod(z, a):
    if not z < a:
        z, a = a, z

    i, j = a, z
    y1, y2 = 1, 0

    while True:
        q = i//j
        r = i - (j*q)
        y = y2 - (y1*q)
        i, j = j, r
        y2, y1 = y1,y

        if j>0:
            continue

        else:
            break

    return y2%a

def gcd(x,y):
    """ Greatest Common Divisor of x and y """
    x = abs(x) ; y = abs(y)
    while x > 0:
        x, y = y % x, x
    return y

def lcm(x, y):
    return (x*y) // gcd(x, y)

def pair_wise_consistency_test(n, e, d):
    m = randrange(1, n-1)
    return m == pow(m, e*d, n)