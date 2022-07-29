from pubcrypt.number.primality import get_prime_factors
from pubcrypt.number.util import *


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


def primitive_exp(m, exp, n):
    """ This function represent the encryption/decryption/signature operation """
    if 0 < m < n-1:
        return pow(m, exp, n)

    else:
        raise ValueError("Data representative out of range")


def prime_recovery(n, e, d):
    a = (d*e-1) * gcd(n-1, d*e-1)
    m = a//n
    r = a - m*n
    b = (n-r) // (m+1) +1

    if pow(b, 2) <= 4*n:
        raise ValueError("Error")

    y = isqrt(pow(b, 2)-4*n)
    return (b+y) // 2, (b-y) // 2