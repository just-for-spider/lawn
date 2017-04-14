#!/usr/bin/env python
# -*- coding: utf-8 -*-
########################################################################
# 
# Copyright (c) 2017 Qianbao.com, Inc. All Rights Reserved
# 
########################################################################
 
"""
File: uuid_test.py
Author: wangqj(wangqj@qianbao.com)
Date: 2017/04/10 16:51:26
"""

import uuid


std = 'YYS_LT_%s'

token = uuid.uuid1().get_hex()
print type(token)

print std % (token, )





<type 'str'>
YYS_LT_22b3a8641dcb11e7b1a7964791d484c0


