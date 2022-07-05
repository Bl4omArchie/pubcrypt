from Crypto.Util.number import getPrime, bytes_to_long, long_to_bytes
from pubcrypt import rsa

n, e, d = rsa.generate(2048)

print (f"n = {n}")
print (f"e = {e}")
print (f"d = {d}")


flag = b"cypher{flag_de_test}"
c = rsa.encrypt(bytes_to_long(flag), e, n)
m = rsa.decryp(c, d, n)

print (long_to_bytes(m)) 