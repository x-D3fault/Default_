#!/usr/bin/env python3
from random import randint
from base64 import b64encode

def phase_one(password):
	gate = [118, 140, 231, 176, 205, 480, 308, 872, 702, 820, 1034, 1176, 1339, 1232, 1605, 1792, 782, 810, 1197, 880, 924, 1694, 2185, 2208, 2775]

	flag = ""
	for i,g in enumerate(gate, 1):
		x = 3 * (g + 7 * i) // i
		x = int(x / 3)
		ch = chr(x)
		flag += ch

	for i,j in enumerate(range(48, 0, -2)):
		password[j] = flag[i]

	return password


def phase_two(password):
	block = b'c3MxLnRkMy57XzUuaE83LjVfOS5faDExLkxfMTMuR0gxNS5fTDE3LjNfMTkuMzEyMS5pMzIz'
	clear_text_block = "ss1.td3.{_5.hO7.5_9._h11.L_13.GH15._L17.3_19.3121.i323"
	dot_split_clear_text_block = clear_text_block.split(".")

	# Create hammer dictionary
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

	# {'1': 'ss', '3': 'td', '5': '{_', '7': 'hO', '9': '5_', '11': '_h1', '13': 'L_1', '15': 'GH1', '17': '_L1', '19': '3_1', '21': '312', '23': 'i32'}
	for a in range(1, 24, 2):
		n = str(a)
		password[a] = hammer[n][0]
		password[a + 24] = hammer[n][1]
	
	password[0] = 'v'
	return password


password = []
for i in range(0,49):
	password.append('')

password = phase_one(password)
password = phase_two(password)

password = "".join(password)
print(password)