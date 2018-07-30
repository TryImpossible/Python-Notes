#!/usr/bin/python
# -*- coding: UTF-8 -*-

# HTTP 头部
print "Content-Disposition: attachment; filename=\"/Users/barry/Server/Documents/hello_get _copy.html\"";
print
# 打开文件
fo = open("/Users/barry/Server/Documents/hello_get.html", "rb")

str = fo.read();
print str

file = open("/Users/barry/Server/Documents/hello_get _copy.html", "r+")
file.write(str);
file.close();

# 关闭文件
fo.close()