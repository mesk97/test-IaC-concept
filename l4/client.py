#!/usr/bin/env python

import socket

# socket.socket(family, type,
#  family: socket.AF_UNIX, socket.AF_INET, socket.AF_INET6
#  type:  socket.SOCK_STREAM, socket.SOCK_DGRAM, socket.SOCK_RAW
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.connect(('localhost', 9090))

s.send(b"ping\n")

data = s.recv(1024)
print ("from %s: %s" % (str(s.getpeername()), data))

s.close()
