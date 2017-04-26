#!/usr/bin/env python
# -*- coding: utf-8 -*-
########################################################################
# 
# Copyright (c) 2017 Qianbao.com, Inc. All Rights Reserved
# 
########################################################################

"""
File: search_test.py
Author: wangqj(wangqj@qianbao.com)
Date: 2017/04/01 10:29:31
"""

import urllib2
from urllib import urlencode


def to_bytes(text, encoding=None, errors='strict'):
    """Return the binary representation of `text`. If `text`
    is already a bytes object, return it as-is."""
    if isinstance(text, bytes):
        return text
    if encoding is None:
        encoding = 'utf-8'
        return text.encode(encoding, errors)


def _urlencode(seq, enc):
    values = [(to_bytes(k, enc), to_bytes(v, enc)) for k, v in seq]
    print values
    return urlencode(values, doseq=1)


def doPost(url, dic):
    request = urllib2.Request(url=url, data=dic)
    request.add_header('Content-Type', 'application/x-www-form-urlencoded; charset=UTF-8')
    request.add_header('Host', 'wenshu.court.gov.cn')
    request.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:52.0) Gecko/20100101 Firefox/52.0')
    request.add_header('X-Requested-With', 'XMLHttpRequest')
    request.add_header('Accept-Encoding', 'gzip, deflate')
    request.add_header('Accept-Language', 'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3')
    resp = urllib2.urlopen(request)
    res = resp.read()
    return res

uri = 'http://wenshu.court.gov.cn/List/ListContent'

dic = {}
dic['Direction'] = 'asc'
dic['Index'] = '1'
dic['Order'] = '法院层级'
dic['Page'] = '5'
dic['Param'] = '案件类型:刑事案件,法院地域:上海市'


querystr = _urlencode(dic.items(), 'utf-8')

print querystr

doc = doPost(uri, querystr)

#print doc
