#!/usr/bin/env python
# -*- coding: utf-8 -*-
########################################################################
# 
# Copyright (c) 2017 Qianbao.com, Inc. All Rights Reserved
# 
########################################################################
 
"""
File: re_test.py
Author: wangqj(wangqj@qianbao.com)
Date: 2017/03/27 10:04:59
"""

import re

body = 'jQuery17205445927260395554_1490579539681({resultCode:"0000",redirectURL:"http://www.10010.com"});'
body = 'jQuery17205445927260395554_1490579539681({resultsCode:"0000",redirectURL:"http://www.10010.com"});'

pat = re.compile(r'resultCode:"(?P<result_code>[\S]+?)"')
m = pat.search(body)
if m:
    print m.group('result_code')


reg = re.findall(re.compile(r'resultCode:\"([\S]+?)\"', re.I), body)

print reg
