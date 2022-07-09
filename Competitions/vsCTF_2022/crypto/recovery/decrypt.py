#!/usr/bin/env python3
from random import randint
from base64 import b64encode

block = b'c3MxLnRkMy57XzUuaE83LjVfOS5faDExLkxfMTMuR0gxNS5fTDE3LjNfMTkuMzEyMS5pMzIz'
clear_text_block = "ss1.td3.{_5.hO7.5_9._h11.L_13.GH15._L17.3_19.3121.i323"
dot_split_clear_text_block = clear_text_block.split(".")
password = []

hammer = {}
for b in dot_split_clear_text_block:
	if len(b) == 3:
		num = b[-1]
		part = b[:2]
		hammer[num] = part 
	elif len(b) == 4:
		num = b[-2:]
		part = b[:3]
		hammer[num] = part 

print(hammer)
for i in range(49):
	password.append('')

for key,val in hammer.items():
	password[key] = val[key]

print(password)


"""
1
3
5
7
9
11
13
15
17
19
21
23
"""



