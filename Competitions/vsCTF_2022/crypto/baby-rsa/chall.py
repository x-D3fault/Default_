#!/usr/bin/env python3

from Crypto.PublicKey import RSA
from Crypto.Util.number import *
# e = 101

with open("flag.txt",'r') as f:
    flag = f.read().strip()

#p = getPrime(128)
#q = getPrime(128)

p = 198387342217803593989680933147752639099
q = 250933075739434836274504719934159653227
e = 101

"""
while p % e != 1:
    p = getPrime(128)
while q % e != 1:
    q = getPrime(128)
"""


n = p * q
m = bytes_to_long(flag.encode())
c = pow(m, e, n)

print("p: %d" % p)
print("q: %d" % q)
print("n: %d" % n)
exit()



print(f"Ciphertext: {hex(c)}")


with open("pubkey.pem",'w') as f:
    pk = RSA.construct([n, e])
    f.write(pk.exportKey('PEM').decode('utf-8'))

# Ciphertext: 0x459cc234f24a2fb115ff10e272130048d996f5b562964ee6138442a4429af847