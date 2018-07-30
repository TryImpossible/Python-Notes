#!/usr/bin/python
# -*- coding: UTF-8 -*-

# print "Content-type:text/html"
# print                               # 空行，告诉服务器结束头部
# print '<html>'
# print '<head>'
# print '<meta charset="utf-8">'
# print '<title>Hello Word - 我的第一个 CGI 程序！</title>'
# print '</head>'
# print '<body>'
# print '<h2>Hello Word! 我是来自菜鸟教程的第一CGI程序</h2>'
# print '</body>'
# print '</html>'

# import os;
# print 'Content-type:text/html';
# print 
# print '<meta charset="utf-8">';
# print '<b>環境變量</b><br>';
# print '<ul>';
# for key in os.environ.keys():
#     print '<li><span style="color:green">%30s </span> : %s</li>' % (key, os.environ[key]);
# print '</ul>';

import cgi, cgitb;
form = cgi.FieldStorage();
site_name = form.getValue('name');
site_url = form.getValue('url');

print "Content-type:text/html";
print;                              
print '<html>';
print '<head>';
print '<meta charset="utf-8">';
print '<title>菜鳥教程CGI測試實例！</title>';
print '</head>';
print '<body>';
print '<h2>%s官網：%s</h2>' % (site_name, site_url);
print '</body>';
print '</html>';