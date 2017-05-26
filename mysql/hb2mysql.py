#!/usr/bin/env python
# -*- coding: utf-8 -*-
########################################################################
# 
# Copyright (c) 2017 Qianbao.com, Inc. All Rights Reserved
# 
########################################################################
 
"""
File: hb2mysql.py
Author: wangqj(wangqj@qianbao.com)
Date: 2017/05/25 14:18:50
"""

import sys
import json
import logging
import time


def read():
    citys = {}
    with open('./citys-dzdp.json') as f:
        js = f.read()
        dic = json.loads(js)
        if dic:
            for line in dic['city']:
                city, _, _, num, _ = line.split('|')
                citys[num] = city
    return citys

city_map = read()



import db

shopids = db.readallshopid()

logging.info('num=%s, sleep 10 seconds' % len(shopids))
time.sleep(10)


for line in sys.stdin:
    line = line.strip()
    
    arr = line.split(' ', 1)
    url = arr[0].strip()
    dic1 = arr[1].strip()

    try:

        dic = json.loads(dic1)

        outlink = dic.get('outlink', '')
        if not outlink:
            logging.info(msg='not outlink')
            continue


        regionurl = dic['regionurl']
        if not regionurl:
            regionurl = dic['cateurl']

        if not regionurl:
            logging.info(msg='not region url or cate url')
            continue

        cityid = regionurl.split('/')[-3]

        if cityid in city_map:

            shopid = outlink.split('/')[-1]
            name = dic.get('anchor', '')
            city = city_map[cityid]
            region = dic.get('region', '')
            addr = dic.get('addr', '')

            info = {}
            info['city'] = city
            info['vendor_name'] = name
            info['district_name'] = region
            info['shopid'] = shopid
            info['address'] = addr

            if shopid not in shopids:
                db.insertanchor(info)
            else:
                logging.info(msg='exists')
            
    except Exception as e:
        logging.exception(e)
        break




