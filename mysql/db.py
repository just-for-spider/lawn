#!/usr/bin/env python
# -*- coding: utf-8 -*-
########################################################################
# 
# Copyright (c) 2017 Qianbao.com, Inc. All Rights Reserved
# 
########################################################################
 
"""
File: db.py
Author: wangqj(wangqj@qianbao.com)
Date: 2017/05/25 15:50:10
"""

import MySQLdb
import logging


conn= MySQLdb.connect(host='172.28.40.21', port = 3306, user='crawler', passwd='crawler', db ='crawl')
conn.set_character_set('utf8')

cur = conn.cursor()
cur.execute('SET NAMES utf8;')
cur.execute('SET CHARACTER SET utf8;')
cur.execute('SET character_set_connection=utf8;')


def readallshopid():
    """
    支持字典读
    """
    r = set()

    sql = 'SELECT shopid FROM dianping_all_3'
    num = cur.execute(sql)
    t = cur.fetchmany(num)
    for x in t:
        r.add(x[0])
    return r

readallshopid()


def insertanchor(dic):
    sql = "INSERT INTO dianping_all_3 (city, vendor_name, district_name, shopid, address) VALUES(%(city)s, %(vendor_name)s, %(district_name)s, %(shopid)s, %(address)s)"
    n = cur.execute(sql, dic)
    conn.commit()
    logging.info(msg='num=%s' % n)



def close():
    cur.close()
    conn.close()

#close()
