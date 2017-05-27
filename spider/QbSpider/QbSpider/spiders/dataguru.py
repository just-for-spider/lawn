#!/usr/bin/env python
# -*- coding: utf-8 -*-
########################################################################
# 
# Copyright (c) 2017 Qianbao.com, Inc. All Rights Reserved
# 
########################################################################
 
"""
File: dataguru.py
Author: wangqj(wangqj@qianbao.com)
Date: 2017/05/12 11:57:00
"""
from scrapy.http import Request

from scrapy_redis.spiders import RedisSpider


class DATAGURUSpider(RedisSpider):

    name = 'dataguru'

    redis_key = 'dataguru:start_urls'

    allowed_domains = ['dataguru.cn']

    def __gettxt(self, e, x, r=None):
        if r:
            e_list = e.xpath(x).re(r)
        else:
            e_list = e.xpath(x).extract()
        e_list = [x.strip() for x in e_list]
        txt = ''.join(e_list)
        return txt

    def parse(self, response):
        #a_list = response.xpath("//div[@class='bm_c xld']/dl/dt/a")
        #for a in a_list:
        #    href = self.__gettxt(a, './@href')
        #    outlink = response.urljoin(href)
        #    #print outlink
        #    yield Request(outlink, callback=self.parse)


        a_list = response.xpath("//div[@class='pg']/a")
        for a in a_list:
            href = self.__gettxt(a, './@href')
            outlink = response.urljoin(href)
            #print outlink
            yield Request(outlink)

