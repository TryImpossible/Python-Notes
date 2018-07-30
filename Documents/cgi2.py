#!/usr/bin/python
# -*- coding: UTF-8 -*-

import os;
print 'Content-type:text/html';
print 
print '<meta charset="utf-8">';
print '<b>環境變量</b><br>';
print '<ul>';
for key in os.environ.keys():
    print '<li><span style="color:green">%s </span> : %s</li>' % (key, os.environ[key]);
print '</ul>';