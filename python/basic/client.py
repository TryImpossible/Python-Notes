#!/usr/bin/python
#coding=utf-8
import socket;
s = socket.socket();
# host = socket.gethostname();
host = '127.0.0.1';
port = 12345;

s.connect((host, port));

print s.recv(1024);
s.close();