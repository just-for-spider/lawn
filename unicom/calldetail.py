#!/usr/bin/env python
# -*- coding: utf-8 -*-
########################################################################
# 
# Copyright (c) 2017 Qianbao.com, Inc. All Rights Reserved
# 
########################################################################
 
"""
File: calldetail.py
Author: wangqj(wangqj@qianbao.com)
Date: 2017/03/29 20:36:45
"""

dic = {
    "calldetail": [
        {
                        "calltype": "2",
                        "calltypename": "被叫",
                        "homeareaname": "长沙",
                        "calledhome": "岳阳",
                        "calllonghourunitsecond": 14,
                        "otherareaName": "",
                        "othernum": "18973009609",
                        "landtype": "国内通话",
                        "calllonghour": "14秒",
                        "starttime": "2017-02-22 08:11:40",
                        "totalfee": "0.00"
                    
        },
        {
                        "calltype": "2",
                        "calltypename": "被叫",
                        "homeareaname": "长沙",
                        "calledhome": "岳阳",
                        "calllonghourunitsecond": 21,
                        "otherareaName": "",
                        "othernum": "18973009609",
                        "landtype": "国内通话",
                        "calllonghour": "21秒",
                        "starttime": "2017-02-22 08:03:12",
                        "totalfee": "0.00"
                    
        }
            
    ]

}


for k1 in dic:
    for k2 in dic[k1][0]:
        print '%s\t\t%s\t\t%s' % (k1, k2, dic[k1][0][k2])
