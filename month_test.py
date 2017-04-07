#!/usr/bin/env python
# -*- coding: utf-8 -*-
########################################################################
# 
# Copyright (c) 2017 Qianbao.com, Inc. All Rights Reserved
# 
########################################################################
 
"""
File: month_test.py
Author: wangqj(wangqj@qianbao.com)
Date: 2017/03/23 15:06:18
"""

import time


def gethalfyearmonth():
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
    for x in xrange(0, 6):
        if realmonth > x:
            month = "0" + str(realmonth - x) if len(str(realmonth - x)) == 1 else str(realmonth - x)
            ym = str(realyear) + "-" + month
        else:
            y = str(x+7) if x+7 >=10 else "0"+str(x+7)
            ym = str(realyear - 1) + "-" + y
        if ym[5:7] == realdate[5:7]:
            day = {(realdate[:-2]+"01"): realdate}
        else:
            for k, v in daycount_month.iteritems():
                if ym[5:7] in v:
                    day = {(ym + "-01"):(ym + "-%s" % k)}
        monthlist.append(day)
    return monthlist

import datetime

def getlast6month():
    months = []
    end = datetime.date.today()
    begin = end.replace(day=1)
    months.append((begin, end))

    for i in range(5):
        end = begin - datetime.timedelta(days=1)
        begin = end.replace(day=1)
        months.append((begin, end))
    return months
        
#{'beginDate': '2017-03-00', 'endDate': '2017-03-00', 'pageSize': '100', 'pageNo': '1'}
#{'beginDate': '2017-03-01', 'endDate': '2017-03-01', 'pageSize': '100', 'pageNo': '1'}

#monlist = gethalfyearmonth()
#monlist = getlast6month()
#for mon in monlist:
#    for k, v in mon.iteritems():
#        for xx in xrange((int(v[8:]) - int(k[8:])) + 1):
#            if xx < 10:
#                begdate = '0' + str(xx)
#            else:
#                begdate = str(xx)
#
#            pay_load = {
#                'pageNo': '1',
#                'pageSize': '100',
#                'beginDate': k[0:8]+begdate,
#                'endDate': k[0:8]+begdate
#            }
#            print pay_load

monlist = getlast6month()
for begin, end in monlist:
    for i in range((end-begin).days+1):
        day = begin + datetime.timedelta(days=i)
        day = str(day)
        pay_load = {
            'pageNo': '1',
            'pageSize': '100',
            'beginDate': day,
            'endDate': day
        }
        print pay_load
































