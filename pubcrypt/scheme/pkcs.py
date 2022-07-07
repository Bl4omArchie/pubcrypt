from pubcrypt.modules.rsa import encrypt, decrypt
from pubcrypt.number.util import int_to_byte
from random import getrandbits
from os import urandom
from Crypto.Util.number import bytes_to_long


def pkcs_encrypt(m, e, n):
    k = n.bit_length()
    mLen = len(m)

    if mLen > k-11:
        raise ValueError("Message too long")

    em = 0x00 | 0x02 | getrandbits(k-mLen-3) | 0x00 | bytes_to_long(m)
    return int_to_byte(encrypt(em, e, n), k)

def pkcs_decrypt(c, d, n):
    k = n.bit_length()
    cLen = len(c)

    if cLen != k:
        raise ValueError("Ciphertext too long")

    m = pow(bytes_to_long(bytes(c, )), d, n)
    em = 0x00 | 0x02 | int_to_byte(m, k) | 0x00 | m
    return int_to_byte(decrypt(bytes_to_long(em), e, n), k)