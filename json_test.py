#!/usr/bin/env python
# -*- coding: utf-8 -*-
########################################################################
# 
# Copyright (c) 2017 Qianbao.com, Inc. All Rights Reserved
# 
########################################################################
 
"""
File: json_test.py
Author: wangqj(wangqj@qianbao.com)
Date: 2017/03/21 14:14:11
"""
import re
import json


resp_texts = 'jQuery_1490075239788({"resultCode":"false"});'

regex = "[\S\s]+?{([\S\s]+)}"
resp_text = re.findall(re.compile(r'%s'%regex,re.I),resp_texts)
print resp_text
if resp_text:
    strs = "{"+resp_text[0]+"}"
    re_item = re.compile(r'(?<=[{,])\w+')
    after = re_item.sub("\"\g<0>\"", strs)
    print json.loads(after)
else:
    print json.loads("{"+resp_text[0]+"}")

