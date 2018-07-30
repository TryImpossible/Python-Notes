#!/usr/bin/python
# -*- coding: UTF-8 -*-

# filename：test.py

# CGI处理模块
import cgi, cgitb 

# 创建 FieldStorage 的实例化
form = cgi.FieldStorage() 

# 获取数据
name = form.getvalue('name');
location  = form.getvalue('location');
language = form.getvalue('language');


print "Content-type:text/html"
print
print "<html>"
print "<head>"
print "<meta charset=\"utf-8\">"
print "<title>测试实例</title>"
print "</head>"
print "<body>"
print "<h2>%s - %s - %s</h2>" % (name, location, language)
print "</body>"
print "</html>"

