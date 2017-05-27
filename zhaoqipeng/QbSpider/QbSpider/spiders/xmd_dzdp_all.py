#!/usr/bin/env python
# -*- coding: utf-8 -*-
########################################################################
# 
# Copyright (c) 2017 Qianbao.com, Inc. All Rights Reserved
# 
########################################################################
 
"""
File: xmd_dzdp_all.py
Author: wangqj(wangqj@qianbao.com)
Date: 2017/05/10 10:04:13
"""


import os

import logging
import json
import re


from scrapy.http import Request
from scrapy.spiders import CrawlSpider


import sys
sys.path.append(os.path.abspath("../../"))
from QbSpider.utils.hbcommon import HBClient


logger = logging.getLogger(__name__)


class XMDDZDPSpider(CrawlSpider):

    name = 'xmddzdpall'

    allowed_domains = ['dianping.com']

    tb = HBClient()

    #start_urls = ['https://www.dianping.com/search/category/2/10/']
    #start_urls = ['https://www.dianping.com/search/category/10/10/']
    #start_urls = ['https://www.dianping.com/search/category/3/10']

    pat_idx = re.compile('^http(s)?://www.dianping.com/search/category/\d+/\d+(/)?(g\d+)?([rc]\d+)?(p\d+)?$')

    #custom_settings = {
    #    'DOWNLOAD_DELAY': 0.2,
    #    'CONCURRENT_REQUESTS': 5,
    #    'DOWNLOAD_TIMEOUT': 35,
    #    'COOKIES_ENABLED': True,
    #    'REDIRECT_ENABLED': False,
    #    'REFERER_ENABLED': True,
    #    'USEPROXYHIGHLEVEL': False,
    #    'USELOCALIP': 1,
    #    'RETRY_ENABLED': False,
    #    'RETRY_TIMES': 0,
    #    'RETRY_HTTP_CODES': [],
    #    'HTTPERROR_ALLOWED_CODES':  [403, 404]
    #}

    def __init__(self, *args, **kwargs):
        self.start_urls = []
        std = 'https://www.dianping.com/search/category/%s/10/'
        citys = self.__loadurls()
        for num, city in citys:
            url = std % num
            self.start_urls.append(url)

    def __loadurls(self, fname='./citys-dzdp.json'):
        citys = []
        #maginc num
        with open('./citys-dzdp.json') as f:
            js = f.read()
            dic = json.loads(js)
            if dic:
                for line in dic['city']:
                    city, _, _, num, _ = line.split('|')
                    citys.append((int(num), city))
        citys.sort(key=lambda x:x[0])
        for city in citys:
            logging.info(msg='%s, %s' % city)
        return citys
    
    def parse(self, response):

        if response.status in [403, 404]:
            logging.warning('%s, %s' % (response.url, response.status))
            return

        if not self.pat_idx.match(response.url):
            logging.warn('invalid url: %s' % response.url)

        # extract dish
        x_dish = "//div[@id='classfy']/a"
        outlinks = self.__getoutlinks(response, x_dish)
        for outlink in outlinks:
            yield Request(outlink, callback=self.parse)

        # extract region
        x_region = "//div[@id='region-nav']/a"
        outlinks = self.__getoutlinks(response, x_region)
        for outlink in outlinks:
            yield Request(outlink, callback=self.parse)

        # extract region 2
        x_region2 = "//div[@id='region-nav-sub']/a"
        outlinks = self.__getoutlinks(response, x_region2)
        for outlink in outlinks:
            yield Request(outlink, callback=self.parse)

        # extract next page
        a_list = response.xpath("//div[@class='page']/a")
        for a in a_list:
            anchor = self.__gettxt(a, ".//text()")
            href = self.__gettxt(a, "./@href")
            if not href:
                continue
            href = href.split('?')[0]
            outlink = response.urljoin(href)
            if self.pat_idx.match(outlink):
                logging.info('%s,%s' % (anchor, outlink))
                yield Request(outlink, callback=self.parse)
            else:
                logging.warn('invalid outlink: %s' % outlink)

        self.__parse_pagelist(response)

    def __getoutlinks(self, response, x):
        outlinks = []
        a_list = response.xpath(x)
        for a in a_list:
            anchor = self.__gettxt(a, ".//text()")
            href = self.__gettxt(a, "./@href")
            if not href:
                continue
            outlink = response.urljoin(href)
            if self.pat_idx.match(outlink):
                logging.info('%s,%s' % (anchor, outlink))
                outlinks.append(outlink)
            else:
                # filter
                logging.warn('invalid outlink: %s' % outlink)
        return outlinks

    def __gettxt(self, e, x, r=None):
        if r:
            e_list = e.xpath(x).re(r)
        else:
            e_list = e.xpath(x).extract()
        e_list = [x.strip() for x in e_list]
        txt = ''.join(e_list)
        return txt

    def __parse_pagelist(self, response):

        def getpromo(e_li):
            a_promo_list = e_li.xpath("./div[@class='txt']/div[@class='tit']/div[@class='promo-icon']/a")
            dic_promo = {}
            for a_p in a_promo_list:
                promo = self.__gettxt(a_p, './@class')
                promo_url = self.__gettxt(a_p, './@href')
                if promo_url:
                    promo_url = response.urljoin(promo_url)
                dic_promo[promo] = promo_url
            if dic_promo:
                return dic_promo
            return ''

        x_li = "//div[@id='shop-all-list']/ul/li"
        list_li = response.xpath(x_li)

        records = []

        for e_li in list_li:
            metadata = {}
            href = self.__gettxt(e_li, "./div[@class='txt']/div[@class='tit']/a[1]/@href")
            if not href:
                continue
            outlink = response.urljoin(href)
            metadata['outlink'] = outlink
            anchor = self.__gettxt(e_li, "./div[@class='txt']/div[@class='tit']/a[1]//text()")
            metadata['anchor'] = anchor

            ## 支持所有优惠， 目前仅发现团购与外卖
            #dic_promo = getpromo(e_li)
            ## 这里的数据要抓取
            #metadata['promo'] = dic_promo

            istoptrade = self.__gettxt(e_li, "./div[@class='txt']/div[@class='tit']/span[@class='istopTrade']/text()", '\((.*?)\)')
            metadata['istoptrade'] = istoptrade

            branch_url = self.__gettxt(e_li, "./div[@class='txt']/div[@class='tit']/a[@class='shop-branch']/@href")
            if branch_url:
                branch_url = response.urljoin(branch_url)

            star = self.__gettxt(e_li, "./div[@class='txt']/div[@class='comment']/span/@class", '(\d+)')
            metadata['star'] = star
            num_comments = self.__gettxt(e_li, "./div[@class='txt']/div[@class='comment']/a[@class='review-num']/b/text()")
            metadata['numcomments'] = num_comments
            mean_price = self.__gettxt(e_li, "./div[@class='txt']/div[@class='comment']/a[@class='mean-price']/b/text()", '(\d+)')
            metadata['meanprice'] = mean_price
            tag_cate = self.__gettxt(e_li, "./div[@class='txt']/div[@class='tag-addr']/a[1]//text()")
            metadata['cate'] = tag_cate
            tag_cate_url = self.__gettxt(e_li, "./div[@class='txt']/div[@class='tag-addr']/a[1]/@href")
            if tag_cate_url:
                tag_cate_url = response.urljoin(tag_cate_url)
            metadata['cateurl'] = tag_cate_url
            tag_region = self.__gettxt(e_li, "./div[@class='txt']/div[@class='tag-addr']/a[2]//text()")
            metadata['region'] = tag_region
            tag_region_url = self.__gettxt(e_li, "./div[@class='txt']/div[@class='tag-addr']/a[2]/@href")
            if tag_region_url:
                tag_region_url = response.urljoin(tag_region_url)
            metadata['regionurl'] = tag_region_url
            addr = self.__gettxt(e_li, "./div[@class='txt']/div[@class='tag-addr']/span[@class='addr']//text()")
            metadata['addr'] = addr

            records.append((outlink, metadata))

        for outlink, meta in records:
            # 入库
            anchor = json.dumps(meta)
            try:
                self.tb.insertanchor(url=outlink, anchor=anchor)
            except Exception as e:
                logging.exception(e)
            
            logging.info(msg='insertanchor: %s' % outlink)
