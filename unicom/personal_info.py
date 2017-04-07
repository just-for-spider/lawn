#!/usr/bin/env python
# -*- coding: utf-8 -*-
########################################################################
# 
# Copyright (c) 2017 Qianbao.com, Inc. All Rights Reserved
# 
########################################################################
 
"""
File: personal_info.py
Author: wangqj(wangqj@qianbao.com)
Date: 2017/03/28 16:08:18
"""

import json


ajsos = """
 {"personal_info": [{"custsex": "1", "province": "\u6cb3\u5357", "citycode": "760", "producttype": "01", "subscrbstat": "\u5f00\u901a", "opendate": "2016-06-11 11:50:02", "paytype": "2", "certtype": "02", "brandcode": "4G00", "custname": "\u5de6\u5f26", "serial_numbers": "037106283659|18537179815", "certaddr": "\u6cb3\u5357\u7701\u9093\u5dde\u5e02\u5218\u96c6\u9547\u5317\u4f55\u51b2\u6751\u4f55\u5c972\u53f7", "paytypename": "\u540e\u4ed8\u8d39", "provincecode": "76", "custsexname": "\u7537", "brandname": "\u6c834G\u540e\u4ed8\u8d39", "certnum": "41138119921128713X", "custlvl": "\u4e09\u661f\u7528\u6237", "productname": "4G\u5168\u56fd\u5957\u9910-136\u5143\u5957\u9910", "usernumber": "18537179815", "productid": "99999828"}]}
"""

dic = json.loads(ajsos)

for k1 in dic:
    for k2 in dic[k1][0]:
        line = '%s\t%s\t%s' % (k1, k2, dic[k1][0][k2])
        print line.encode('utf-8')
