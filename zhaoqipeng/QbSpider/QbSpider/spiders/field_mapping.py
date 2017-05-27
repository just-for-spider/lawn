#!/usr/bin/env python
# -*- coding: utf-8 -*-
########################################################################
# 
# Copyright (c) 2017 Qianbao.com, Inc. All Rights Reserved
# 
########################################################################
 
"""
File: field_mapping.py
Author: wangqj(wangqj@qianbao.com)
Date: 2017/04/14 15:44:36
"""

import urllib2
from lxml import etree


def getHtml(url):
    request = urllib2.Request(url)
    request.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 6.1; rv:19.0) Gecko/20100101 Firefox/19.0')
    request.add_header('Cookie', 'doc-sidebar=300px; seraph.confluence=16023862%3A0414080c294673e335a68d5ebdb19dd63a4a0dc7; JSESSIONID=0E5B0508BC6E3D26C28B560634D916A7')
    doc = urllib2.urlopen(request, timeout=45).read()
    return doc


uri = 'http://wiki.qianbaoqm.com/pages/viewpage.action?pageId=15766812'

html = getHtml(uri)

dom = etree.HTML(html)
rows = dom.xpath("//table[@class='confluenceTable']/tbody/tr")
print len(rows)
