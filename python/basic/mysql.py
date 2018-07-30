#!/usr/bin/python
# -*- coding: UTF-8 -*-

# import MySQLdb;
# db = MySQLdb.connect('localhost', 'root', 'root', 'test_db');
# cursor = db.cursor();
# cursor.execute('select version()');
# data = cursor.fetchone();
# print 'Database version : %s' % data;
# db.close();

# import MySQLdb;
# db = MySQLdb.connect('localhost', 'root', 'root', 'test_db');
# cursor = db.cursor();
# cursor.execute('drop table if exists employee');
# sql = '''create table employee (
#     first_name char(20) not null,
#     last_name char(20),
#     age int,
#     sex char(1),
#     income float)''';
# cursor.execute(sql);
# db.close();

# import MySQLdb;
# db = MySQLdb.connect('localhost', 'root', 'root', 'test_db');
# cursor = db.cursor();
# sql = '''insert into employee(first_name, last_name, age, sex, income) values('Mac', 'Mohan', 20, 'M', 2000)''';
# try:
#     cursor.execute(sql);
#     db.commit();
# except:
#     db.rollback();
# db.close();

# import MySQLdb;
# db = MySQLdb.connect('localhost', 'root', 'root', 'test_db');
# cursor = db.cursor();
# sql = "select * from employee where income > '%d'" % (1000);
# try:
#     cursor.execute(sql);
#     results = cursor.fetchall();
#     for row in results:
#         fname = row[0];
#         lname = row[1];
#         age = row[2];
#         sex = row[3];
#         income = row[4];
#         print "fname=%s,lanme=%s,age=%d,sex=%s,income=%d" % (fname, lname, age, sex, income);
# except:
#     print 'Error: Unable to fecth data';
# db.close();