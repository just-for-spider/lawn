#!/usr/bin/env python
# -*- coding: utf-8 -*-
########################################################################
# 
# Copyright (c) 2017 Qianbao.com, Inc. All Rights Reserved
# 
########################################################################
 
"""
File: shopnamematch.py
Author: wangqj(wangqj@qianbao.com)
Date: 2017/04/25 10:34:19
"""

import urllib
import urllib2
from six.moves.urllib.parse import urljoin
from lxml import etree
from operator import itemgetter

import sim


def getHtml(url):
    request = urllib2.Request(url)
    #request.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 6.1; rv:19.0) Gecko/20100101 Firefox/19.0')
    request.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:53.0) Gecko/20100101 Firefox/53.0')
    doc = urllib2.urlopen(request, timeout=45).read().decode('utf-8')
    return doc

def _urlencode(name):
    name = name.encode('utf-8')
    name = urllib.quote(name)
    return name

def getinfo(url):
    x_phone = "//p[@class='expand-info tel']/span[2]/text()"
    x_addr = "//div[@class='expand-info address']/span[2]/text()"
    html = getHtml(url)
    dom = etree.HTML(html)
    phone = None
    addr = None

    hour = dom.xpath(u"//p[@class='info info-indent']/span[text()='营业时间：']/following::span[1]/text()")[0]
    print hour

    try:
        phone = dom.xpath(x_phone)[0].strip()
        addr = dom.xpath(x_addr)[0].strip()
        return phone, addr
    except IndexError:
        print 'indexerror:', url
    return phone, addr


def getlist(sname, regionid, phones):
    shopname = _urlencode(sname)
    seed = u'http://www.dianping.com/search/keyword/%s/0_%s' % (regionid, shopname)
    
    html = getHtml(seed)
    dom = etree.HTML(html)
    xpath_sname = "//div[@id='shop-all-list']/ul/li/div[@class='txt']/div[@class='tit']"
    alist = dom.xpath(xpath_sname)
    records = []
    for a in alist:
        # 标准化：括号中文转英文
        # 解析是否分店
        # 如果是分店：解析评论数
        ru = a.xpath('./a[1]/@href')[0]
        shopid = int(ru.split('/')[-1])
        branchid = 0
        try:
            branchid = a.xpath('./a[@class="shop-branch"]/@href')[0].split('/')[-2].split('_')[1]
        except:
            pass

        branchid = int(branchid)
        uri = urljoin(seed, ru)
        phone, addr = getinfo(uri)
        hit = False
        if phone in phones:
            hit = True

        h = a.xpath('./a[1]/h4/text()')[0]
        sstr, size, prob = sim.lcsstr(h, sname)
        records.append((prob, hit, shopid, branchid, h, sname, sstr, size, phone, ''.join(phones), addr))
    records.sort(key=itemgetter(0, 1, 2, 3), reverse=True)
    return records


if __name__ == '__main__':
    url = 'http://www.dianping.com/shop/2833240'
    phone, addr = getinfo(url)
    print phone, addr

    #import sys
    #for line in sys.stdin:
    #    line = line.decode('utf-8')
    #    sname, region, phone = line.strip().split()
    #    phones = phone.split('|')
    #    rs =getlist(sname, region, phones)
    #    for r in rs:
    #        print r
    #    print '----------' * 20

    #sname = sys.argv[1].decode('utf-8')
    #region = sys.argv[2]
    #getlist(sname, region)
