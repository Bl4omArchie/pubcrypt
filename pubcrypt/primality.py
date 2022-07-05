from random import getrandbits, randrange
from pubcrypt.util import gcd
from math import sqrt


def get_prime_factors(pBits, e):
    candidate = 0
    while candidate == 0:
        p = getrandbits(pBits)
        if p%2 == 0:
            p += 1

        if p >= sqrt(2)*(pow(2, pBits-1)):
            if gcd(p-1, e) == 1:
                candidate = miller_rabin(p, pBits, 5)

    candidate = 0
    while candidate == 0:
        q = getrandbits(pBits)
        if q%2 == 0:
            q += 1

        if p-q > pow(2, (pBits)-100) or q >= sqrt(2)*(pow(2, pBits-1)):
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