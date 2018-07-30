#!/usr/bin/python
#coding=utf-8;
# import re;
# print (re.match('www', 'www.runoob.com').span());
# print (re.match('com', 'www.runoob.com'));

# import re;
# line = 'Cats are smarter than dogs';
# matchObj = re.match(r'(.*) are (.*?) .*', line, re.M|re.I);
# if matchObj:
#     print 'matchObj.group():', matchObj.group();
#     print 'matchObj.group(1):', matchObj.group(1);
#     print 'matchObj.group(2):', matchObj.group(2);
# else:
#     print 'No match!!';

# import re;
# print (re.search('www', 'www.runoob.com').span());
# print (re.search('com', 'www.runoob.com').span());

# import re
# line = "Cats are smarter than dogs";
# searchObj = re.search( r'(.*) are (.*?) .*', line, re.M|re.I)
# if searchObj:
#    print "searchObj.group() : ", searchObj.group()
#    print "searchObj.group(1) : ", searchObj.group(1)
#    print "searchObj.group(2) : ", searchObj.group(2)
# else:
#    print "Nothing found!!"

# import re;
# phone = '2004-959-559 # 這是一個國外電話號碼';
# num = re.sub(r'#.*$', '', phone);
# print '電話號碼是:', num;
# num = re.sub(r'\D', '', phone);
# print '電話號碼是:', num;

# import re;
# def double(matched):
#     value = int(matched.group('value'));
#     return str(value * 2);
# s = 'A23G4HFD567';
# print(re.sub('(?P<value>\d+)', double, s));

# import re;
# str = '1strzz. . .23';
# searchObj = re.search(r'.*$', str, re.M|re.I);
# searchObj = re.search(r'[tr]', str, re.M|re.I);
# searchObj = re.search(r'[^str].*$', str, re.M|re.I);
# searchObj = re.search(r'\w.*$', str, re.M|re.I);
# searchObj = re.search(r'\W.*$', str, re.M|re.I);
# searchObj = re.search(r'\s.*$', str, re.M|re.I);
# searchObj = re.search(r'\S.*$', str, re.M|re.I);
# searchObj = re.search(r'\d.$', str, re.M|re.I);
# searchObj = re.search(r'\D', str, re.M|re.I);
# print(searchObj.group());

# import re;
# str = 'ruby123';
# searchObj = re.search(r'[Pp]ython', str, re.M|re.I);
# searchObj = re.search(r'rub[ye]', str, re.M|re.I);
# searchObj = re.search(r'[aeiou]', str, re.M|re.I);
# searchObj = re.search(r'[0-9].*$', str, re.M|re.I);
# searchObj = re.search(r'\d', str, re.M|re.I);
# print(searchObj.group());





import re

key = r"<html><body><h1>hello world<h1></body></html>"#这段是你要匹配的文本
p1 = r"(?<=<h1>).+?(?=<h1>)"#这是我们写的正则表达式规则，你现在可以不理解啥意思
pattern1 = re.compile(p1)#我们在编译这段正则表达式
matcher1 = re.search(pattern1,key)#在源文本中搜索符合正则表达式的部分
print matcher1.group(0)#打印出来