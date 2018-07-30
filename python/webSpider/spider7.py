#coding=utf-8
import re
# matchObj = re.match(r'abc', 'abc')
# matchObj = re.match(r'a.c', 'abc')
# matchObj = re.match(r'a[bcd]e', 'ace')
# matchObj = re.match(r'hello', 'hello world')
# if matchObj:
#     print matchObj.group()

# import re
# pattern = re.compile(r'hello')
# match = pattern.match('hello world')
# if match:
#     print match.group()


# import re
# m = re.match(r'(\w+) (\w+)(?P<sign>.*)', 'hello world!')
# print "m.string:", m.string
# print "m.re:", m.re
# print "m.pos:", m.pos
# print "m.endpos:", m.endpos
# print "m.lastindex:", m.lastindex
# print "m.lastgroup:", m.lastgroup
 
# print "m.group(1,2):", m.group(1, 2)
# print "m.groups():", m.groups()
# print "m.groupdict():", m.groupdict()
# print "m.start(2):", m.start(2)
# print "m.end(2):", m.end(2)
# print "m.span(2):", m.span(2)
# print r"m.expand(r'\2 \1\3'):", m.expand(r'\2 \1\3')

# import re
# p = re.compile(r'(\w+) (\w+)(?P<sign>.*)', re.DOTALL)
# print "p.pattern:", p.pattern
# print "p.flags:", p.flags
# print "p.groups:", p.groups
# print "p.groupindex:", p.groupindex

# import re
# pattern = re.compile(r'world')
# match = pattern.search('hello world')
# if match:
#     print match.group()
    
# import re
# p = re.compile(r'\d+')
# print p.split('one1two2three3four4')

# import re
# p = re.compile(r'\d+')
# print p.findall('one1two2three3four4')

# import re
# p = re.compile(r'\d+')
# for m in p.finditer('one1two2three3four4'):
#     print m.group(),

# import re
# p = re.compile(r'(\w+) (\w+)')
# s = 'i say, hello world!'
# print p.sub(r'\2 \1', s)

# def func(m):
#     # print m.group(1)
#     print m.group(2)
#     return m.group(1).title() + ' ' + m.group(2).title()
# print p.sub(func, s)

# import re
# p = re.compile(r'(\w+) (\w+)')
# s = 'i say, hello world!'
# print p.subn(r'\2 \1', s)

# def func(m):
#     return m.group(1).title() + ' ' + m.group(2).title()
# print p.subn(func, s)