#coding=utf-8
# for letter in 'Python':
#     print '當前字母：', letter;

# fruits = ['banana', 'apple', 'mango'];
# for fruit in fruits:
#     print '當前水果:', fruit;
# print 'Good bye';


# fruits = ['banana', 'apple', 'mango'];
# for index in range(len(fruits)):
#     print '當前水果：', fruits[index];
# print 'Good bye!';

# for num in range(10 ,20):
#     for i in range(2, num):
#         if num % i == 0:
#             j = num / i;
#             print '%d 等於 %d * %d' % (num, i, j);
#             break;
#     else :
#         print 'num';

# '''在python中，for循环后的in跟随一个序列的话，循环每次使用的序列元素，而不是序列
# 的下标'''
# s = 'qazxswedcvfr'
# for i in range(0,len(s),2):
#     print s[i]
# '''enumerate() :
#     在每次循环中，可以同时得到下标和元素
#     际上，enumerate(),在每次循环中返回的是包含每个元素的定值表，两个元素分别赋值
#  index，char'''
# for (index,char) in enumerate(s):
#     print "index=%s ,char=%s" % (index,char)


# for i in range(1,11):
#     for k in range(1,i):
#         print k,
#         k +=1
#     i +=1
#     print "\n"