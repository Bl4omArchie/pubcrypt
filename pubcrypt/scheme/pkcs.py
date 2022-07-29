from pubcrypt.number.util import int_to_bytes, bytes_to_int
from pubcrypt.modules.rsa import primitive_exp
from os import urandom

def pkcs_encrypt2(m, e, n):
    k = n.bit_length()
    mLen = len(m)

    if mLen > k - 11:
        raise ValueError("Plaintext is too long.")

    ps = urandom(k-mLen-3)
    em = b"\0x00\0x02" + ps + b"0x00" + m
    m = bytes_to_int(em)
    c = primitive_exp(m, e, n)
    return int_to_bytes(c)

def pkcs_encrypt(m, e, n):
    k = n.bit_length()
    mLen = len(m)

    if mLen > k - 11:
        raise ValueError("Plaintext is too long.")

    ps = []
    while len(ps) != k - mLen - 3:
        new_byte = urandom(1)
        if new_byte[0] == 0x00:
            continue
        ps.append(new_byte)
    ps = b"".join(ps)
    assert(len(ps) == k - mLen - 3)

    em = b'\x00\x02' + ps + b'\x00' + m
    em_int = bytes_to_int(em)
    m_int = pow(em_int, e, n)
    return int_to_bytes(m_int)

def pkcs_decrypt(c, d, n):
    k = n.bit_length()

    if len(c) != k or k < 11:
        raise ValueError("Decryption error")

    m = primitive_exp(bytes_to_int(c), d, n)
    em = "\0x00\0x02" + ps + "0x00" + m

    return int_to_byte(primitive_exp(bytes_to_int(em), e, n), k)