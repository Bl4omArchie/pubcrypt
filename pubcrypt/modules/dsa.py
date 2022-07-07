from hashlib import sha256

"""
p a prime modulus, where 2L–1 < p < 2L, and L is the bit length of p. Values for L are
provided in Section 4.2.
q a prime divisor of (p – 1), where 2N–1 < q < 2 N, and N is the bit length of q. Values for N
are provided in Section 4.2.
g a generator of a subgroup of order q in the multiplicative group of GF(p), such that 1 < g
< p.
x the private key that must remain secret; x is a randomly or pseudorandomly generated
integer, such that 0 < x < q, i.e., x is in the range [1, q–1].
y the public key, where y = gx mod p.
k a secret number that is unique to each message; k is a randomly or pseudorandomly
generated integer, such that 0 < k < q, i.e., k is in the range [1, q–1].


Selection of parameter sizes and hash functions, (L, N):
L = 1024, N = 160
L = 2048, N = 224
L = 2048, N = 256
L = 3072, N = 256

"""