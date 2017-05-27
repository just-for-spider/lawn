#!/usr/bin/env python
# -*- coding: utf-8 -*-
########################################################################
# 
# Copyright (c) 2017 Qianbao.com, Inc. All Rights Reserved
# 
########################################################################
 
"""
File: hbcommon.py
Author: wangqj(wangqj@qianbao.com)
Date: 2017/05/10 15:07:21
"""

import os
import sys
from urlparse import urlsplit

from thrift.transport import TSocket
from thrift.protocol import TBinaryProtocol
#sys.path.append(os.path.abspath("../"))
sys.path.append(os.path.abspath("../../"))
from QbSpider.hbases import Hbase
from QbSpider.hbases.ttypes import *
from scrapy.utils.project import get_project_settings


def reverseUrl(url):
    reverse_url = ''
    url = urlsplit(url)

    # reverse host
    reverse_host = '.'.join(url.hostname.split('.')[::-1])
    reverse_url += reverse_host

    # add protocol
    reverse_url += ':'
    reverse_url += url.scheme

    # add port if necessary
    if url.port:
        reverse_url += ':'
        reverse_url += str(url.port)

    # add path
    if url.path:
        reverse_url += url.path

    if url.query:
        reverse_url += '?'
        reverse_url += url.query

    if url.fragment:
        reverse_url += '#'
        reverse_url += url.fragment

    return reverse_url



class HBClient(object):
    def __init__(self, tabname='webpage'):

        settings = get_project_settings().getdict('PARAMS_CONNECT_HBASE')

        self.host = settings['host']
        self.port = settings['port']
        self.buf = settings['buf']

        self.TabName = tabname

    def __open(self):
        self.transport = TTransport.TBufferedTransport(TSocket.TSocket(self.host, self.port), rbuf_size=self.buf)
        self.protocol = TBinaryProtocol.TBinaryProtocol(self.transport)
        self.client = Hbase.Client(self.protocol)
        self.transport.open()

    def insertanchor(self, url, anchor):
        self.__open()
        rowkey = reverseUrl(url)
        mutations = [Mutation(column="f:bas", value=url),
                     Mutation(column="f:anc", value=anchor)]
        self.client.mutateRow(self.TabName, rowkey, mutations, None)

    def getanchor(self, url):
        self.__open()
        rowkey = reverseUrl(url)
        ajson = self.client.get(self.TabName, rowkey, 'f:anc', None)
        print ajson[0].value

    def getallanchor(self):
        self.__open()

        scan = TScan()
        id = self.client.scannerOpenWithScan(self.TabName, scan, None)
        reslist = self.client.scannerGetList(id, 10000)
        while reslist:
            for res in reslist:
                print res.columns['f:bas'].value, res.columns['f:anc'].value
            reslist = self.client.scannerGetList(id, 10000)



if __name__ == '__main__':
    url = 'https://www.dianping.com/shop/67056533'
    url = 'https://www.dianping.com/shop/9811536'
    url = 'https://www.dianping.com/shop/15859122'
    url = 'https://www.dianping.com/shop/23426548'
    url = 'https://www.dianping.com/shop/8757578'
    url = 'https://www.dianping.com/shop/9913405'
    #url = reverseUrl(url)
    #print url

    hb = HBClient()
    #hb.insertanchor(url, 'anchor')
    #hb.getanchor(url)

    hb.getallanchor()
