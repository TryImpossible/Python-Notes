#coding=utf-8


# def printme( str ):
#     '打印傳入的字符串到標準顯示設備上'
#     print str;
#     return;
# printme(123);

# def changeInt (a):
#     a = 10;
# b = 2;
# changeInt(a = 10);
# print b;

# def changeMe(myList):
#     myList.append([1,2,3]);
#     print '函數內取值:', myList;
#     return;

# myList=[10, 20, 30];
# changeMe(myList);
# print '函數外取值:', myList;

# def printInfo( name, age = 35 ):
#     print 'Name:', name;
#     print 'Age:', age;
#     return;

# printInfo( age = 50, name = 'miki' );
# printInfo( name = 'miki' );

# def printInfo( arg1, *vartuple ):
#     print '輸出';
#     print arg1;
#     for var in vartuple:
#         print var;
#     return;

# printInfo( 10 );
# print('\n');
# printInfo( 70, 60, 50 );

# sum = lambda arg1, arg2: arg1 + arg2;
# print(sum(1, 2));

# total = 0;
# def sum( arg1, arg2 ):
#     total = arg1 + arg2;
#     print '函數內是局部變量:',total;
#     global total;
#     total = total;
#     return total;

# sum( 10, 20 );
# print '函數外是全局變量:', total;