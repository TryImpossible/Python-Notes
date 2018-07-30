import urllib
import urllib2

url = 'http://localhost/register.py'
values = {'name': 'WHY', 'location': 'SDU', 'language': 'Python'}
data  = urllib.urlencode(values)
req = urllib2.Request(url, data)
response = urllib2.urlopen(req)
the_page = response.read()
print the_page

import urllib2
import urllib

data = {}
data['name'] = 'WHY'
data['location'] = 'SDU'
data['language'] = 'Python'

url_values = urllib.urlencode(data)
print url_values

url = 'http://localhost/register.py'
full_url = url + '?' + url_values
data = urllib2.urlopen(full_url)  
print data.read()

import urllib
import urllib2

url = 'http://localhost/register.py'
user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
values = {'name': 'WHY', 'location': 'SDU', 'language': 'Python'}
headers = {'User-Agent': user_agent}
data = urllib.urlencode(values)
req = urllib2.Request(url, data, headers)
response = urllib2.urlopen(req)
the_page = response.read()
print the_page