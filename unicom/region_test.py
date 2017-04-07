#!/usr/bin/env python
# -*- coding: utf-8 -*-
########################################################################
# 
# Copyright (c) 2017 Qianbao.com, Inc. All Rights Reserved
# 
########################################################################
 
"""
File: region_test.py
Author: wangqj(wangqj@qianbao.com)
Date: 2017/03/28 10:13:54
"""

import os


class RegionUnicom(object):

    data = u"""
    110 11 北京
    305 30 安徽
    831 83 重庆
    380 38 福建
    510 51 广东
    870 87 甘肃
    591 59 广西
    850 85 贵州
    710 71 湖北
    741 74 湖南
    188 18 河北
    760 76 河南
    501 50 海南
    971 97 黑龙江
    340 34 江苏
    901 90 吉林
    750 75 江西
    910 91 辽宁
    101 10 内蒙古
    880 88 宁夏
    700 70 青海
    170 17 山东
    310 31 上海
    190 19 山西
    841 84 陕西
    810 81 四川
    130 13 天津
    890 89 新疆
    790 79 西藏
    860 86 云南
    360 36 浙江
    HK HK 香港
    """

    fields = ['citycode', 'provcode', 'province']

    dic = {}

    @classmethod
    def code2region(cls, code):

        if not cls.dic:
            arr = cls.data.strip().split(os.linesep)
            for e in arr:
                obj = cls()
                line = e.strip()
                vals = line.split()
                for i in range(len(cls.fields)):
                    setattr(obj, cls.fields[i], vals[i])
                cls.dic[obj.provcode] = obj.province


        return cls.dic[code]



code = '88'
prov = RegionUnicom.code2region(code=code)
print prov

