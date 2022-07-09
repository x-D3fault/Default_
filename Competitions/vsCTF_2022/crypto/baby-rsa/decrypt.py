#!/usr/bin/env python3

from Crypto.PublicKey import RSA
from Crypto.Util.number import *

p = 198387342217803593989680933147752639099
q = 250933075739434836274504719934159653227
n = 49781945970485287497637893439585768739049771806112518367057783076095921722473
e = 101
phi = (p - 1) * (q - 1)
c = 0x459cc234f24a2fb115ff10e272130048d996f5b562964ee6138442a4429af847

f = open('flag.txt', 'r').readline().strip().split(' ')
d_bytes = []

d = 1
while ((d * e) % phi) != 1:
	d += 1
print(d)