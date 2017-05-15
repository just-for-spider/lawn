#!/usr/bin/env python
# -*- coding: utf-8 -*-
########################################################################
# 
# Copyright (c) 2017 Qianbao.com, Inc. All Rights Reserved
# 
########################################################################
 
"""
File: javascript_dict_transfer.py
Author: wangqj(wangqj@qianbao.com)
Date: 2017/05/08 17:12:28
"""

astr = """
{userId:0,shopId:67344977,shopCityId:2,shopName:"康二姐串串香",address:"中关村大街19号新中关购物中心B1楼",publicTransit:"",cityId:2,cityCnName:"北京",cityName:"北京",cityEnName:"beijing",isOverseasCity:0,fullName:"康二姐串串香(新中关购物中心店)",shopGlat:"39.978386",shopGlng:"116.31563",cityGlat:"39.904667",cityGlng:"116.408198",power:5,shopPower:30,voteTotal:0,district:0,shopType:10,mainRegionId:1488,mainCategoryName:"串串香",categoryURLName:"food",shopGroupId:67478771,categoryName:"美食",loadUserDomain:"http://www.dianping.com",map:{power:5,manaScore:0},mainCategoryId:3017,defaultPic:"http://p0.meituan.net/dpmerchantalbum/43ed4b2d23a95fa74327aba8af1172ff74155.jpg%40120w_90h_1e_1c_1l_80q%7Cwatermark%3D1%26%26r%3D1%26p%3D9%26x%3D2%26y%3D2%26relative%3D1%26o%3D20"}
"""

import re

pat = re.compile("(\w+?):")

m = pat.findall(astr)
print m
