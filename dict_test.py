#!/usr/bin/env python
# -*- coding: utf-8 -*-
########################################################################
# 
# Copyright (c) 2017 Qianbao.com, Inc. All Rights Reserved
# 
########################################################################
 
"""
File: dict_test.py
Author: wangqj(wangqj@qianbao.com)
Date: 2017/03/21 14:38:51
"""

dic = {'c': 100}

dic1 = {'a': 'b', 'c': 10}
dic.update(dic1)

print dic


dic = {
        "vip_level": '',
        "packageName": "4G全国套餐-136元套餐",
        "rspCode": "00",
        "is_vip": '',
        "provinceCode": "076",
        "rspDesc": '',
        "cityCode": "760",
        "period": "2017-03-01 至 2017-03-22",
    "rspArgs": {
        "result": [
            {
                "content": [
                    [
                                                "专项款",
                                                "0.00"
                                            
                    ]
                                    
                ],
                                "title": "账户当前可用余额",
                                "fee": "102.45"
                            
            },
            {
                                "title": "欠费金额",
                                "fee": "0.00"
                            
            },
            {
                "content": [
                    [
                                                "联通在信-短信通信费",
                                                "0.10"
                                            
                    ],
                    [
                                                "一体化套餐月套餐费",
                                                "136.00"
                                            
                    ],
                    [
                                                "增值业务-绿色邮箱",
                                                "0.00"
                                            
                    ]
                                    
                ],
                                "title": "实时话费",
                                "fee": "136.10"
                            
            }
                    
        ],
                "isFix": "false",
                "totalfee": "0.00"
            
    },
    "netType": "11",
        "name": "左弦",
            "packageID": "99999828",
                "custlvl": "三星用户",
                    "payType": "2",
                        "queryDate": "2017年03月22日",
                            "mobile": "18537179815"

}


def get_value_dict(dic, where, *keys):
    print keys

    pass


keys = ['rspArgs', 'result', 'fee']
get_value_dict(dic, None, *keys)








