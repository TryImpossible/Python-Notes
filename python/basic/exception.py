#coding=utf-8;

# try:
#     file = open('testfile', 'w');
#     file.write('這是一個測試文件');
# except IOError:
#     print 'Error:沒有找到文件或讀取文件失敗';
# else:
#     print '內容寫入文件成功';
#     file.close();

# def temp_convert(var):
#     try:
#         return int(var);
#     except ValueError, Argument:
#         print '參數沒有包含數字\n', Argument;
# print temp_convert('123');

# def mye(level):
#     if level < 1:
#         raise Exception('Invalid level', level);
# try:
#     mye(0);
# except 'Invalid level!':
#     print 1;
# else: 
#     print 2;

class NetWorkerror(RuntimeError):
    def __init__(self, arg):
        self.args = arg;
try:
    raise NetWorkerror('Bad hostname');
except NetWorkerror, e:
    print e.args;