from math import floor, log2, ceil
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

def isqrt (x):
    """ Credit: https://rosettacode.org/wiki/Isqrt_(integer_square_root)_of_X#Python """
    q = 1
    while q <= x : 
        q *= 4

    z, r = x, 0
    while q > 1 :
        q //= 4
        t, r = z-r-q, r//2
        if t >= 0 :
            z, r = t, r+q
    return r 

def perfect_square(c):
    n = floor(log2(c)) + 1
    m = ceil(n/2)
    x = pow(2, m) - pow(2, m-1)

    while True:
        x = (pow(x, 2)+c)/(2*x)

        if pow(x, 2) < pow(2, m)+c:
            break

    return c == pow(floor(x), 2)


def int_to_bytes(x: int) :
    return x.to_bytes((x.bit_length() + 7) // 8, 'big')
    
def bytes_to_int(xbytes: bytes) :
    return int.from_bytes(xbytes, 'big') 