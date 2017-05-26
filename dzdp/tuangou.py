#!/usr/bin/env python
# -*- coding: utf-8 -*-
########################################################################
# 
# Copyright (c) 2017 Qianbao.com, Inc. All Rights Reserved
# 
########################################################################
 
"""
File: tuangou.py
Author: wangqj(wangqj@qianbao.com)
Date: 2017/05/25 10:40:17
"""

import urllib2


def getHtml(url):
    request = urllib2.Request(url)
    #request.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 6.1; rv:19.0) Gecko/20100101 Firefox/19.0')
    request.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:53.0) Gecko/20100101 Firefox/53.0')
    doc = urllib2.urlopen(request, timeout=45).read().decode('utf-8')
    return doc



url_price = 'http://t.dianping.com/ajax/detail_ajax_check_user?dealGroupId=22654077'
#url_price = 'http://t.dianping.com/ajax/getaids?ids=22654077&needDeal=1'

doc = getHtml(url_price)
print doc

url_promo = 'http://t.dianping.com/jsonp/dealPromo?ids=22654077&templateId=18'
doc = getHtml(url_promo)
print doc

url_command = 'http://t.dianping.com/ajax/recommend?action=alsoview&dealGroupId=22654077&limit=10&reqId=undefined'
doc = getHtml(url_command)
print doc

url = 'http://t.dianping.com/ajax/messagebar?position=detail&dealGroupId=22654077&action=showbar'
doc = getHtml(url)
print doc

#url = 'http://t.dianping.com/ajax/dealGroupShopDetail?dealGroupId=22654077&cityId=2&action=shops&page=1&regionId=0'
#doc = getHtml(url)
#print doc


