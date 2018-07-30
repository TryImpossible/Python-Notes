#coding=utf-8

# import urllib2
# req = urllib2.Request('http://www.baibai.com')
# try:
#     urllib2.urlopen(req)
# except urllib2.URLError as e:
#     print e.reason

# from urllib2 import Request, urlopen, URLError, HTTPError
# req  = Request('http://bbs.csdn.net/callmewhy')

# try:
#     response = urlopen(req)
# except HTTPError as e:
#     print 'The server couldn\'t fulfill the request'
#     print 'Error code:', e.code
# except URLError as e:
#     print 'We failed to read a server'
#     print 'Reason:', e.reason
# else:
#     print 'No exception was raised'

# from urllib2 import Request, urlopen, URLError, HTTPError
# req  = Request('http://bbs.csdn.net/callmewhy')

# try:
#     response = urlopen(req)
# except URLError as e:
#     if hasattr(e, 'code'):
#         print 'The server couldn\'t fulfill the request'
#         print 'Error code:', e.code
#     elif hasattr(e, 'reason'):
#         print 'We failed to read a server'
#         print 'Reason:', e.reason
# else:
#     print 'No exception was raised'

