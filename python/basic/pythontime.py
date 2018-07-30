#!/usr/bin/python3
#coding=utf-8

# import time  
# import datetime  

# starttime = datetime.datetime.now()  

# time.sleep(5)  

# endtime = datetime.datetime.now()  
# print ((endtime - starttime).seconds )


# import datetime
# i = datetime.datetime.now()
# print ("当前的日期和时间是 %s" % i)
# print ("ISO格式的日期和时间是 %s" % i.isoformat() )
# print ("当前的年份是 %s" %i.year)
# print ("当前的月份是 %s" %i.month)
# print ("当前的日期是  %s" %i.day)
# print ("dd/mm/yyyy 格式是  %s/%s/%s" % (i.day, i.month, i.year) )
# print ("当前小时是 %s" %i.hour)
# print ("当前分钟是 %s" %i.minute)
# print ("当前秒是  %s" %i.second)


# import time;
# ticks = time.time();
# print '當前時間:', ticks;

# import time;
# localtime = time.localtime(time.time());
# localtime = time.asctime(time.localtime(time.time()));
# print '本地時間:', localtime;

# import time;
# print time.strftime("%Y-%m-%d %H:%M:%S", time.localtime());
# print time.strftime("%a %b %d %H:%M:%S %Y", time.localtime());
# a = "Sat Mar 28 22:24:24 2016";
# print time.mktime(time.strptime(a, "%a %b %d %H:%M:%S %Y"));

# import calendar;
# cal = calendar.month(2016, 1);
# print cal;
# print calendar.firstweekday();