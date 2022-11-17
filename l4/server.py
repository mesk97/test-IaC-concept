#!/usr/bin/env python

import socket
import time

socket_for_listen = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# соединить сокет с адресс/порт
socket_for_listen.bind(("0.0.0.0", 9090))

# физически начинаем слушать на порту ждем новые соединения 
socket_for_listen.listen()

# принимаем новое соединение 
client_socket, addr = socket_for_listen.accept()
print("New client ", str(addr))

# принимаем данные 
data = client_socket.recv(1024)

# отправ
client_socket.sendall(bytes("reply: " + str(data), "utf-8"))

client_socket.close()
socket_for_listen.close()

