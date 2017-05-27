#!/usr/bin/env python
# -*- coding: utf-8 -*-
########################################################################
# 
# Copyright (c) 2017 Qianbao.com, Inc. All Rights Reserved
# 
########################################################################
 
"""
File: injecttools.py
Author: wangqj(wangqj@qianbao.com)
Date: 2017/05/22 11:47:38
"""
import redis
import sys


if __name__ == '__main__':
    host ='172.28.40.23'
    port = 6379
    password = 'Qbbigdata'

    for line in sys.stdin:
            line = line.strip()
            r = redis.Redis(host=host, port=port, password=password)
            r.lpush('xmddzdp:start_urls', line)

