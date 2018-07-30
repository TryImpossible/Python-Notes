#!/usr/bin/python
#coding=utf-8
import socket;
s = socket.socket();
# host = socket.gethostname();
host = '127.0.0.1';
port = 12345;
s.bind((host, port));

s.listen(5);

while True:
    c, addr = s.accept();
    print '連接地址：', addr;
    c.send('歡迎訪問菜鳥教程');
    c.close();
    