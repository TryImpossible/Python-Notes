#coding=utf-8

# count = 0;
# while (count < 9) :
#     print 'The count is:', count;
#     count += 1;
# print 'Good bye';

# i = 1;
# while i < 10:
#     i += 1;
#     if i % 2 > 0:
#         continue;
#     print i;

# i = 1;
# while 1:
#     print i;
#     i += 1;
#     if i > 10:
#         break;

# var = 1;
# while var == 1 :
#     num = raw_input('Enter a number:');
#     print 'You entered:', num;
# print 'Good bye!';

# count = 0;
# while count < 5:
#     print count, 'is less than 5';
#     count += 1;
# else :
#     print count, 'is not less than 5';

# flag = 1;
# while (flag) : print 'Given flag is really true!';
# print 'Good bye!';


import random;
import sys;
import time;

result = [];
while True:
    result.append(int(random.uniform(1, 7)));
    result.append(int(random.uniform(1, 7)));
    result.append(int(random.uniform(1, 7)));
    print result;
    count = 0;
    index = 2;
    pointStr = '';
    while index >= 0:
        currPoint = result[index];
        count += currPoint;
        index -= 1;
        pointStr += '';
        pointStr += str(currPoint);
    if count <= 11 :
        sys.stdout.write(pointStr + '->' + '小' + '\n');
        time.sleep(1);
    else:
        sys.stdout.write(pointStr + '->' + '大' + '\n');
        time.sleep(1);
    result = [];