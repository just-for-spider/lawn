#!/usr/bin/env python
# -*- coding: utf-8 -*-
########################################################################
# 
# Copyright (c) 2017 Qianbao.com, Inc. All Rights Reserved
# 
########################################################################
 
"""
File: json_false.py
Author: wangqj(wangqj@qianbao.com)
Date: 2017/04/05 16:24:55
"""

dic = """{"errormessage":{"errcode":"ECS000000002","errmessage":"尊敬的客户您好，系统检测您的访问过于频繁，为保障您的账户安全请明天再试。【ECS000000002】"},"existexception":true,"isnotsuccess":true,"issuccess":true,"rspcode":"ECS000000002","rspdesc":"业务访问限制超出限制次数","totalpage":0,"userinfo":{"areacode":"","brand":"4G00","brand_name":"沃4G后付费","certnum":"41138119921128713X","citycode":"760","currentid":"18537179815","custname":"左弦","custlvl":"三星用户","customid":"5614051309427877","expiretime":"1491381092559","is_20":false,"is_36":false,"is_wo":"2","laststatdate":"","logintype":"01","menu_id":"2001","nettype":"11","nickname":"左弦","opendate":"20160611115002","packageid":"99999828","packagename":"4G全国套餐-136元套餐","paytype":"2","productid":"18537179815","producttype":"01","provincecode":"076","subscrbstat":"开通","usernumber":"18537179815"}}"""

import json

dic = json.loads(dic)

print dic['issuccess']





def fun1():
    yield 1
    yield 2
    yield 3



print type(fun1())


a = xrange(100)
print type(a)
print type(range(10))



