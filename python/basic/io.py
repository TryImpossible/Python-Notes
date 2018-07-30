#coding=utf-8;
# str = raw_input('請輸入:');
# print '您輸入的內容是:', str;

# str = input('請輸入:');
# print '您輸入的內容是:', str;

# file = open('/Users/barry/Desktop/python.txt', 'r+');
# print '文件名', file.name;
# print '是否關閉', file.closed;
# print '訪問模式', file.mode;
# print '末尾是否強制加空格', file.softspace;
# file.close();

# file = open('/Users/barry/Desktop/python.txt', 'a+');
# file.writelines('其實吧');
# file.close();

# file = open('/Users/barry/Desktop/python.txt', 'r+');
# print file.read(30);
# file.close();

# file = open('/Users/barry/Desktop/python.txt', 'r+');
# str = file.read(10);
# print '讀取的字符串是:', str;
# position = file.tell();
# print '當前文件位置:', position;
# position = file.seek(0, 0);
# str = file.read(10);
# print '重新讀取字符串:', str;
# file.close();

# import os;
# print os.rename('/Users/barry/Desktop/python.txt', '/Users/barry/Desktop/python123.txt');
# os.remove('/Users/barry/Desktop/python123.txt');
# os.mkdir('/Users/barry/Desktop/python');
# os.chdir('/Users/barry/Desktop/python');
# print os.getcwd();
# os.rmdir('/Users/barry/Desktop/python');
