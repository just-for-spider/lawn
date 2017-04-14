#!/usr/bin/env python
# -*- coding: utf-8 -*-
########################################################################
# 
# Copyright (c) 2017 Qianbao.com, Inc. All Rights Reserved
# 
########################################################################
 
"""
File: poi86_stat.py
Author: wangqj(wangqj@qianbao.com)
Date: 2017/04/10 18:03:39
"""

import urllib2
from lxml import etree


def getHtml(url):
    request = urllib2.Request(url)
    request.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 6.1; rv:19.0) Gecko/20100101 Firefox/19.0')
    doc = urllib2.urlopen(request, timeout=45).read()
    return doc

url = 'http://www.poi86.com/'
doc = getHtml(url)
dom = etree.HTML(doc)

numlist = dom.xpath("//ul[@class='list-group']/li/div/div[1]/a/small/text()")
numsum = 0
for num in numlist:
    numsum += int(num)

print 'sum:', numsum
