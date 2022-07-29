from pubcrypt.number.util import gcd, isqrt, perfect_square
from random import getrandbits, randrange
from math import log2


def get_prime_factors(pBits, e):
    candidate = 0
    while candidate == 0:
        p = getrandbits(pBits)
        if p%2 == 0:
            p += 1

        if p >= isqrt(2)*(pow(2, pBits-1)):
            if gcd(p-1, e) == 1:
                candidate = miller_rabin(p, pBits, 5)

    candidate = 0
    while candidate == 0:
        q = getrandbits(pBits)
        if q%2 == 0:
            q += 1

        if p-q > pow(2, (pBits)-100) or q >= isqrt(2)*(pow(2, pBits-1)):
            if gcd(q-1, e) == 1:
                candidate = miller_rabin(q, pBits, 5)
    
    return p, q


def miller_rabin(w, wLen, r):
    """Credit: https://rosettacode.org/wiki/Miller%E2%80%93Rabin_primality_test#Python"""
    s = 0
    d = w-1
    while d%2==0:
        d>>=1
        s+=1
    assert(2**s * d == w-1)
 
    def trial_composite(a):
        if pow(a, d, w) == 1:
            return 0

        for i in range(s):
            if pow(a, 2**i * d, w) == w-1:
                return 0
        return 1  
 
    for i in range(r): #number of trials 
        a = randrange(2, w)
        if trial_composite(a):
            return 0
 
    return 1

def phi(n):
    amount = 0
    for k in range(1, n + 1):
        if gcd(k, n) == 1:
            amount += 1
    return amount


def aks_primality_test(n):
    if perfect_square(n):
        return 0

    maxK = pow(log2(n), 2)    
    nexR = True           
    r = 1

    while nexR == True:
        r +=1
        nexR = False
        k = 0
        while k <= maxK and nexR == False:
            k += 1
            if pow(n, k, r) == 0 or pow(n, k, r) == 1:
                nexR = True

    for a in range(2, min(r, n)+1):                    
        if gcd(a,n) > 1:                       
            return 0

    if n <= r:
        return 1

    for a in range(1, floor(isqrt(phi(r))*log2(n))):
        c=1
        for i in range(n//2+1):
            c = c*(p-i)//(i+1)
            if c%n:
                return 0
        return 1
