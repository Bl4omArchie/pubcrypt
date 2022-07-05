from pubcrypt.primality import get_prime_factors
from pubcrypt.util import *


def generate(nBits, e=65537):
    if nBits < 2048:
        raise ValueError(("Incorrect key length. nBits must be equal or greater than 2048"))
    
    elif e%2 == 0 or not pow(2, 16) <= e <= pow(2, 256):
        raise ValueError("Incorrect puclic exponent. e must be odd and in the range [2^16, 2^256]")

    pBits = nBits//2
    key = 0 
    while key == 0:
        p, q = get_prime_factors(pBits, e) 
        d = invmod(e, lcm(p-1, q-1))
        n = p*q

        key = d > pow(2, pBits)
        key = pair_wise_consistency_test(n, e, d)

    return n, e, d

def encrypt(m, e, n):
    return pow(m, e, n)

def decryp(c, d, n):
    return pow(c, d, n)