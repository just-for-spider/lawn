#!/usr/bin/env python
# -*- coding: utf-8 -*-

import urllib
import urllib2
from lxml import etree

import artextract


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


def getart(uri):
    doc = getHtml(uri)
    art = artextract.extract(doc)
    return art



key = u'钱包金服'

key = _urlencode(key)

url_std = 'http://news.baidu.com/ns?word=%s' % key

html = getHtml(url_std)

dom = etree.HTML(html)

divc = dom.xpath("//div[@class='result']")
if divc:
    for div in divc:
        title = ''.join(div.xpath('./h3/a/text()'))
        print 'title:', title
        outlink = ''.join(div.xpath('./h3/a/@href'))
        print outlink
        art = getart(outlink)
        print art
        author = ''.join(div.xpath(".//p[@class='c-author']/text()"))
        print 'author:', author
        content = ''.join(div.xpath("./div//text()"))
        print content
    print '-------------' * 10



