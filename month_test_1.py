#!/usr/bin/env python
# -*- coding: utf-8 -*-
########################################################################
# 
# Copyright (c) 2017 Qianbao.com, Inc. All Rights Reserved
# 
########################################################################
 
"""
File: month_test_1.py
Author: wangqj(wangqj@qianbao.com)
Date: 2017/03/23 19:03:15
"""

import time
import datetime


def getnexthalfyearmonth():

    realdate = time.strftime('%Y-%m-%d', time.localtime(time.time()))
    realmonth = int(realdate[5:7])
    realyear = int(realdate[0:4])
    daycount_month = {"31": ["01", "03", "05", "07", "08", "10", "12"], "30": ["04", "06", "09", "11"], }
    if realyear%4 == 0:
        special_mon = {"29":["02"]}
        daycount_month.update(special_mon)
    else:
        special_mon = {"28":["02"]}
        daycount_month.update(special_mon)
    monthlist = []
    for x in xrange(1, 7):
        if realmonth > x:
            month = "0" + str(realmonth - x) if len(str(realmonth - x)) == 1 else str(realmonth - x)
            ym = str(realyear) + "-" + month
        else:
            y = str(x+6) if x+6 >=10 else "0"+str(x+6)
            ym = str(realyear - 1) + "-" + y
        if ym[5:7] == realdate[5:7]:
            day = {(realdate[:-2]+"01"): realdate}
        else:
            for k, v in daycount_month.iteritems():
                if ym[5:7] in v:
                    day = {(ym + "-01"):(ym + "-%s" % k)}
        monthlist.append(day)
    return monthlist

monlist = getnexthalfyearmonth()
for mon in monlist:
    for k, v in mon.iteritems():
        pay_load = {
            "pageNo": "1",
            "pageSize": "100",
            "beginDate": k.replace("-",""),
            "endDate": v.replace("-","")
        }
        print pay_load


print '#****************************************'

def getlast6month():
    months = []
    end = datetime.date.today()
    begin = end.replace(day=1)
    #months.append((begin, end))

    for i in range(6):
        end = begin - datetime.timedelta(days=1)
        begin = end.replace(day=1)
        months.append((begin, end))
        #months.append((str(begin), str(end)))
    return months

monlist = getlast6month()
for begin, end in monlist:
    begin = begin.strftime('%Y%m%d')
    end = end.strftime('%Y%m%d')
    pay_load = {
        "pageNo": "1",
        "pageSize": "100",
        "beginDate": begin,
        "endDate": end
    }
    print pay_load



{'beginDate': '20170201', 'endDate': '20170228', 'pageSize': '100', 'pageNo': '1'}
{'beginDate': '20170101', 'endDate': '20170131', 'pageSize': '100', 'pageNo': '1'}
{'beginDate': '20160901', 'endDate': '20160930', 'pageSize': '100', 'pageNo': '1'}
{'beginDate': '20161001', 'endDate': '20161031', 'pageSize': '100', 'pageNo': '1'}
{'beginDate': '20161101', 'endDate': '20161130', 'pageSize': '100', 'pageNo': '1'}
{'beginDate': '20161201', 'endDate': '20161231', 'pageSize': '100', 'pageNo': '1'}
#****************************************
{'beginDate': '20170201', 'endDate': '20170228', 'pageSize': '100', 'pageNo': '1'}
{'beginDate': '20170101', 'endDate': '20170131', 'pageSize': '100', 'pageNo': '1'}
{'beginDate': '20161201', 'endDate': '20161231', 'pageSize': '100', 'pageNo': '1'}
{'beginDate': '20161101', 'endDate': '20161130', 'pageSize': '100', 'pageNo': '1'}
{'beginDate': '20161001', 'endDate': '20161031', 'pageSize': '100', 'pageNo': '1'}
{'beginDate': '20160901', 'endDate': '20160930', 'pageSize': '100', 'pageNo': '1'}




#print '#*********************************************'
#
#monlist = getlast6month()
#for begin, end in monlist:
#    begin = str(begin)
#    end = str(end)
#    pay_load = {
#        "pageNo": "1",
#        "pageSize": "100",
#        "beginDate": begin,
#        "endDate": end
#    }
#    print pay_load
#
#
#
#{'beginDate': '2017-02-01', 'endDate': '2017-02-28', 'pageSize': '100', 'pageNo': '1'}
#{'beginDate': '2017-01-01', 'endDate': '2017-01-31', 'pageSize': '100', 'pageNo': '1'}
#{'beginDate': '2016-09-01', 'endDate': '2016-09-30', 'pageSize': '100', 'pageNo': '1'}
#{'beginDate': '2016-10-01', 'endDate': '2016-10-31', 'pageSize': '100', 'pageNo': '1'}
#{'beginDate': '2016-11-01', 'endDate': '2016-11-30', 'pageSize': '100', 'pageNo': '1'}
#{'beginDate': '2016-12-01', 'endDate': '2016-12-31', 'pageSize': '100', 'pageNo': '1'}
##*********************************************
#{'beginDate': '2017-02-01', 'endDate': '2017-02-28', 'pageSize': '100', 'pageNo': '1'}
#{'beginDate': '2017-01-01', 'endDate': '2017-01-31', 'pageSize': '100', 'pageNo': '1'}
#{'beginDate': '2016-12-01', 'endDate': '2016-12-31', 'pageSize': '100', 'pageNo': '1'}
#{'beginDate': '2016-11-01', 'endDate': '2016-11-30', 'pageSize': '100', 'pageNo': '1'}
#{'beginDate': '2016-10-01', 'endDate': '2016-10-31', 'pageSize': '100', 'pageNo': '1'}
#{'beginDate': '2016-09-01', 'endDate': '2016-09-30', 'pageSize': '100', 'pageNo': '1'}



#
##print getnexthalfyearmonth()
#monlist = getnexthalfyearmonth()
#for mon in monlist:
#    for k, v in mon.iteritems():
#        pay_load = {
#            'querytype': '0001',
#            'querycode': '0001',
#            'billdate': k.replace('-', '')[0:6],
#            'flag': '1',
#        }
#        print pay_load
#
#
#{'querycode': '0001', 'billdate': '201702', 'flag': '1', 'querytype': '0001'}
#{'querycode': '0001', 'billdate': '201701', 'flag': '1', 'querytype': '0001'}
#{'querycode': '0001', 'billdate': '201609', 'flag': '1', 'querytype': '0001'}
#{'querycode': '0001', 'billdate': '201610', 'flag': '1', 'querytype': '0001'}
#{'querycode': '0001', 'billdate': '201611', 'flag': '1', 'querytype': '0001'}
#{'querycode': '0001', 'billdate': '201612', 'flag': '1', 'querytype': '0001'}
#
#
#
#def getlast6month():
#    months = []
#    end = datetime.date.today()
#    begin = end.replace(day=1)
#    #months.append((begin, end))
#
#    for i in range(6):
#        end = begin - datetime.timedelta(days=1)
#        begin = end.replace(day=1)
#        months.append((begin, end))
#        #months.append((str(begin), str(end)))
#    return months
#
#
##print getlast6month()
#monlist = getlast6month()
#for begin, _ in monlist:
#    billdate = begin.strftime('%Y%m')
#    pay_load = {
#        'querytype': '0001',
#        'querycode': '0001',
#        'billdate': billdate,
#        'flag': '1',
#    }
#    print pay_load
#
#
#{'querycode': '0001', 'billdate': '201702', 'flag': '1', 'querytype': '0001'}
#{'querycode': '0001', 'billdate': '201701', 'flag': '1', 'querytype': '0001'}
#{'querycode': '0001', 'billdate': '201609', 'flag': '1', 'querytype': '0001'}
#{'querycode': '0001', 'billdate': '201610', 'flag': '1', 'querytype': '0001'}
#{'querycode': '0001', 'billdate': '201611', 'flag': '1', 'querytype': '0001'}
#{'querycode': '0001', 'billdate': '201612', 'flag': '1', 'querytype': '0001'}
#
#{'querycode': '0001', 'billdate': '201702', 'flag': '1', 'querytype': '0001'}
#{'querycode': '0001', 'billdate': '201701', 'flag': '1', 'querytype': '0001'}
#{'querycode': '0001', 'billdate': '201612', 'flag': '1', 'querytype': '0001'}
#{'querycode': '0001', 'billdate': '201611', 'flag': '1', 'querytype': '0001'}
#{'querycode': '0001', 'billdate': '201610', 'flag': '1', 'querytype': '0001'}
#{'querycode': '0001', 'billdate': '201609', 'flag': '1', 'querytype': '0001'}
#
#
#
#
#
#
#
#
##9, 10, 11, 12, 1, 2
#[{'2017-02-01': '2017-02-28'}, {'2017-01-01': '2017-01-31'}, {'2016-09-01': '2016-09-30'}, {'2016-10-01': '2016-10-31'}, {'2016-11-01': '2016-11-30'}, {'2016-12-01': '2016-12-31'}]
##10, 11, 12, 1, 2, 3
#[{'2017-03-01': '2017-03-23'}, {'2017-02-01': '2017-02-28'}, {'2017-01-01': '2017-01-31'}, {'2016-10-01': '2016-10-31'}, {'2016-11-01': '2016-11-30'}, {'2016-12-01': '2016-12-31'}]
#
#
#[{'2017-02-01': '2017-02-28'}, {'2017-01-01': '2017-01-31'}, {'2016-09-01': '2016-09-30'}, {'2016-10-01': '2016-10-31'}, {'2016-11-01': '2016-11-30'}, {'2016-12-01': '2016-12-31'}]
#[('2017-02-01', '2017-02-28'), ('2017-01-01', '2017-01-31'), ('2016-12-01', '2016-12-31'), ('2016-11-01', '2016-11-30'), ('2016-10-01', '2016-10-31'), ('2016-09-01', '2016-09-30')]
#






