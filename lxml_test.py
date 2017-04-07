#!/usr/bin/env python
# -*- coding: utf-8 -*-
########################################################################
# 
# Copyright (c) 2017 Qianbao.com, Inc. All Rights Reserved
# 
########################################################################
 
"""
File: lxml_test.py
Author: wangqj(wangqj@qianbao.com)
Date: 2017/03/28 10:03:51
"""
from lxml import etree

html = u'<div id="province_div" class="myCity topCity" style="display: none;"><ul><li><span>A-G</span><a citycode="110" provincecode="11" href="javascript:void(0)">北京</a><a citycode="305" provincecode="30" href="javascript:void(0)">安徽</a><a citycode="831" provincecode="83" href="javascript:void(0)">重庆</a><a citycode="380" provincecode="38" href="javascript:void(0)">福建</a><a citycode="510" provincecode="51" href="javascript:void(0)">广东</a><a citycode="870" provincecode="87" href="javascript:void(0)">甘肃</a><a citycode="591" provincecode="59" href="javascript:void(0)">广西</a><a citycode="850" provincecode="85" href="javascript:void(0)">贵州</a></li><li><span>H-J</span><a citycode="710" provincecode="71" href="javascript:void(0)">湖北</a><a citycode="741" provincecode="74" href="javascript:void(0)">湖南</a><a citycode="188" provincecode="18" href="javascript:void(0)">河北</a><a citycode="760" provincecode="76" href="javascript:void(0)">河南</a><a citycode="501" provincecode="50" href="javascript:void(0)">海南</a><a citycode="971" provincecode="97" href="javascript:void(0)">黑龙江</a><a citycode="340" provincecode="34" href="javascript:void(0)">江苏</a><a citycode="901" provincecode="90" href="javascript:void(0)">吉林</a><a citycode="750" provincecode="75" href="javascript:void(0)">江西</a></li><li><span>L-S</span><a citycode="910" provincecode="91" href="javascript:void(0)">辽宁</a><a citycode="101" provincecode="10" href="javascript:void(0)">内蒙古</a><a citycode="880" provincecode="88" href="javascript:void(0)">宁夏</a><a citycode="700" provincecode="70" href="javascript:void(0)">青海</a><a citycode="170" provincecode="17" href="javascript:void(0)">山东</a><a citycode="310" provincecode="31" href="javascript:void(0)">上海</a><a citycode="190" provincecode="19" href="javascript:void(0)">山西</a><a citycode="841" provincecode="84" href="javascript:void(0)">陕西</a><a citycode="810" provincecode="81" href="javascript:void(0)">四川</a></li><li><span>T-Z</span><a citycode="130" provincecode="13" href="javascript:void(0)">天津</a><a citycode="890" provincecode="89" href="javascript:void(0)">新疆</a><a citycode="790" provincecode="79" href="javascript:void(0)">西藏</a><a citycode="860" provincecode="86" href="javascript:void(0)">云南</a><a citycode="360" provincecode="36" href="javascript:void(0)">浙江</a><a citycode="HK" provincecode="HK" href="javascript:void(0)">香港</a></li></ul></div>'


dom = etree.HTML(html)

alist = dom.xpath("//div[@id='province_div']/ul/li/a")
for a in alist:
    city = a.xpath('./@citycode')[0]
    province = a.xpath('./@provincecode')[0]
    name = a.xpath('./text()')[0]
    print city, province, name
