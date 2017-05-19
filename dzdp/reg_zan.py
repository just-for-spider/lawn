#!/usr/bin/env python
# -*- coding: utf-8 -*-
########################################################################
# 
# Copyright (c) 2017 Qianbao.com, Inc. All Rights Reserved
# 
########################################################################
 
"""
File: reg_zan.py
Author: wangqj(wangqj@qianbao.com)
Date: 2017/05/16 11:02:28
"""

import re
import json

input = """赞|回应(1)|收藏|不当内容
赞(2)|回应|收藏|不当内容
赞(4)|回应(3)|收藏|不当内容
赞|回应|收藏|不当内容"""


pat = re.compile('(.*?)(\d+)')
lines = input.split('\n')
for line in lines:
    line = line.strip()
    arr = line.split('|')
    dic = {}
    for e in arr:
        e = e.replace('(', '').replace(')', '')
        m = pat.search(e)
        if m:
            key = m.group(1)
            val = m.group(2)
            dic[key] = val
        else:
            dic[e] = ''
    print json.dumps(dic)
    print '-----------------'

        


    

