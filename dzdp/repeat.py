#!/usr/bin/env python
# -*- coding: utf-8 -*-
########################################################################
# 
# Copyright (c) 2017 Qianbao.com, Inc. All Rights Reserved
# 
########################################################################
 
"""
File: repeat.py
Author: wangqj(wangqj@qianbao.com)
Date: 2017/05/18 14:44:32
"""

a = """currurl
cates
shopname
vshop
numbranch
star
numcomments
meanprice
taste
env
service
addr
tel
busihour
alias
intro
istoptrade
piccount
--
todayhits
monthlyhits
weeklyhits
prevweeklyhit
glng
glat
shoptype
newshoptype
clienttype
cityid
phoneno
phoneno2
adduser
addusername
lastuser
lastusername
adddate
lastdate
address
crossroad
publictransit
shoppower
power
district
newdistrict
businesshours
shopgroupid
shopname
branchname
shopid"""


lines = a.split('\n')
lines = [line.strip() for line in lines]
s = set()
for line in lines:
    if line in s:
        print line 
    else:
        s.add(line)

