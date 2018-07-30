#coding=utf-8
# import urllib2
# import cookielib
# #声明一个CookieJar对象实例来保存cookie
# cookie = cookielib.CookieJar()
# #利用urllib2库的HTTPCookieProcessor对象来创建cookie处理器
# handler=urllib2.HTTPCookieProcessor(cookie)
# #通过handler来构建opener
# opener = urllib2.build_opener(handler)
# #此处的open方法同urllib2的urlopen方法，也可以传入request
# response = opener.open('http://www.baidu.com')
# for item in cookie:
#     print 'Name = '+item.name
#     print 'Value = '+item.value

# import cookielib
# import urllib2
# filename = 'cookie.txt'
# cookie = cookielib.MozillaCookieJar(filename)
# handler = urllib2.HTTPCookieProcessor(cookie)
# opener = urllib2.build_opener(handler)
# response = opener.open('http://www.baidu.com')
# cookie.save(ignore_discard=True, ignore_expires=True)

# import cookielib
# import urllib2
# cookie = cookielib.MozillaCookieJar()
# cookie.load('cookie.txt', ignore_discard=True, ignore_expires=True)
# req = urllib2.Request('http://www.baidu.com')
# opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie))
# response = opener.open(req)
# print response.read()

# import urllib
# import urllib2
# import cookielib

# filename = 'cookie.txt'
# cookie = cookielib.MozillaCookieJar(filename)
# opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie))
# postdata = urllib.urlencode({
#     'stuid': '201200131012',
#     'pwd': '23342321'
# })
# loginUrl = 'http://jwxt.sdu.edu.cn:7890/pls/wwwbks/bks_login2.login'
# result = opener.open(loginUrl, postdata)
# cookie.save(ignore_discard=True, ignore_expires=True)
# gradeUrl = 'http:/jwxt.sdu.edu.cn:7890/pls/wwwbks/bkscjcx.curscopre'
# try:
#     result = opener.open(gradeUrl)
# except urllib2.HTTPError, e:
#     print e
# except urllib2.URLError, e:
#     print e

# print result.read()

import re
matchObj = re.match(r'(?P<id>abc){2}', 'abcabc');
print matchObj.string