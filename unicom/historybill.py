#!/usr/bin/env python
# -*- coding: utf-8 -*-
########################################################################
# 
# Copyright (c) 2017 Qianbao.com, Inc. All Rights Reserved
# 
########################################################################
 
"""
File: historybill.py
Author: wangqj(wangqj@qianbao.com)
Date: 2017/03/31 15:44:13
"""

import sys
import json

for line in sys.stdin:
    line = line.strip()
    dic = json.loads(line)

    for key in dic:
        print key, dic[key].encode('utf-8')

    #astr = dic['historyresultlist']
    #print astr

    #adic = json.loads(astr)
    #for key in adic:
    #    print key, adic[key]
    #print '---------------------------------'



