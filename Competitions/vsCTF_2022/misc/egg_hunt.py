#!/usr/bin/env python3

import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = '104.197.118.147'
port = 10100
s.connect((host, port))

intro_msg = s.recv(1024)
x = 0
y = 0 

s.send(b'D')
s.send(b'0 0')
n = s.recv(1024)
print(n)
print("=========================")
s.send(b'D')
s.send(b'0 1')
x = s.recv(1024)
print(x)