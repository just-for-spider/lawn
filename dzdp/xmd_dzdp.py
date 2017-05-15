#!/usr/bin/env python
# -*- coding: utf-8 -*-
########################################################################
# 
# Copyright (c) 2017 Qianbao.com, Inc. All Rights Reserved
# 
########################################################################
 
"""
File: xmd_dzdp.py
Author: wangqj(wangqj@qianbao.com)
Date: 2017/05/04 11:17:17
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

    name = 'xmddzdp'

    allowed_domains = ['dianping.com']

    start_urls = ['https://www.dianping.com/search/keyword/2/0_%E5%BA%B7%E4%BA%8C%E5%A7%90%E4%B8%B2%E4%B8%B2']
    #start_urls = ['https://www.dianping.com/search/keyword/2/0_%E8%82%AF%E5%BE%B7%E5%9F%BA']

    tb = HBClient()

    def __gettxt(self, e, x, r=None):
        if r:
            e_list = e.xpath(x).re(r)
        else:
            e_list = e.xpath(x).extract()
        e_list = [x.strip() for x in e_list]
        txt = ''.join(e_list)
        return txt
    
    def parse(self, response):

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
            anchorinfo = {}
            href = self.__gettxt(e_li, "./div[@class='txt']/div[@class='tit']/a[1]/@href")
            if not href:
                continue
            outlink = response.urljoin(href)
            # 外链
            anchorinfo['outlink'] = outlink
            # 锚点信息
            anchor = self.__gettxt(e_li, "./div[@class='txt']/div[@class='tit']/a[1]//text()")
            anchorinfo['anchor'] = anchor
            # 所有优惠， 1, 目前仅发现团购与外卖 2 这里的数据要抓取
            dic_promo = getpromo(e_li)
            anchorinfo['promo'] = dic_promo
            # 是否营业
            istoptrade = self.__gettxt(e_li, "./div[@class='txt']/div[@class='tit']/span[@class='istopTrade']/text()", '\((.*?)\)')
            anchorinfo['istoptrade'] = istoptrade
            # 分店url
            # 是否抓取全部分店信息
            # 详情页也有, 在详情页抓取吧
            branch_url = self.__gettxt(e_li, "./div[@class='txt']/div[@class='tit']/a[@class='shop-branch']/@href")
            if branch_url:
                branch_url = response.urljoin(branch_url)
            anchorinfo['branchurl'] = branch_url
            # 星级
            star = self.__gettxt(e_li, "./div[@class='txt']/div[@class='comment']/span/@class", '(\d+)')
            anchorinfo['star'] = star
            # 评论数
            num_comments = self.__gettxt(e_li, "./div[@class='txt']/div[@class='comment']/a[@class='review-num']/b/text()")
            anchorinfo['numcomments'] = num_comments
            # 均价
            mean_price = self.__gettxt(e_li, "./div[@class='txt']/div[@class='comment']/a[@class='mean-price']/b/text()", '(\d+)')
            anchorinfo['meanprice'] = mean_price
            # 分类
            tag_cate = self.__gettxt(e_li, "./div[@class='txt']/div[@class='tag-addr']/a[1]//text()")
            anchorinfo['cate'] = tag_cate
            # 分类url
            tag_cate_url = self.__gettxt(e_li, "./div[@class='txt']/div[@class='tag-addr']/a[1]/@href")
            if tag_cate_url:
                tag_cate_url = response.urljoin(tag_cate_url)
            anchorinfo['cateurl'] = tag_cate_url
            # 地区
            tag_region = self.__gettxt(e_li, "./div[@class='txt']/div[@class='tag-addr']/a[2]//text()")
            anchorinfo['region'] = tag_region
            # 地区url
            tag_region_url = self.__gettxt(e_li, "./div[@class='txt']/div[@class='tag-addr']/a[2]/@href")
            if tag_region_url:
                tag_region_url = response.urljoin(tag_region_url)
            anchorinfo['regionurl'] = tag_region_url
            # 地址
            addr = self.__gettxt(e_li, "./div[@class='txt']/div[@class='tag-addr']/span[@class='addr']//text()")
            anchorinfo['addr'] = addr

            records.append((outlink, anchorinfo))

        for outlink, anchor in records:
            logging.info(msg='extract outlink: %s' % outlink)
            yield Request(outlink, callback=self.parse_detail, meta={'anchor': anchor})
            # 先抓一个，测试
            break

    def parse_detail(self, response):

        def getscore(input, pat=re.compile(u'\|口味：([0-9\.]*)\|环境：([0-9\.]*)\|服务：([0-9\.]*)')):
            m = pat.search(input)
            if m:
                return m.group(1), m.group(2), m.group(3)
            return '', '', ''

        def getbranch(div_branch):
            dic = {}
            if not div_branch:
                return dic

            # 分店列表地址
            branch_url = self.__gettxt(div_branch, "//div[@id='shop-branchs']/a[@class='more-shop']/@href")
            if branch_url:
                branch_url = response.urljoin(branch_url)
            dic['branchurl'] = branch_url

            # 分店总数量
            branch_num = self.__gettxt(div_branch, "//div[@id='shop-branchs']/a[@class='more-shop']/text()", '(\d+)')
            dic['branchnum'] = branch_num

            div_list = div_branch.xpath('./div')
            branchlist = []
            for div in div_list:
                subdic = {}
                name = self.__gettxt(div, "./h3/a/text()")
                subdic['name'] = name
                href = self.__gettxt(div, "./h3/a/@href")
                if href:
                    href = response.urljoin(href)
                subdic['url'] = href
                addr = self.__gettxt(div, "./p/text()")
                subdic['addr'] = addr
                star = self.__gettxt(div, "./p/span/@class", '(\d+)')
                subdic['star'] = star
                branchlist.append(subdic)
            dic['branches'] = branchlist
            return dic

        def getshopconfig(txt, pat=re.compile("<script>[\S\s]+?window\.shop_config=([\s\S]*?)</script>"), pat_1=re.compile("(\w+?):\{(\w+?:.*?,\w+:.*?)\}")):
            try:
                m = pat.search(txt)
                if not m:
                    return None
                shop = m.group(1)
                shop = re.sub('\s+', '', shop)
                shop = shop.strip('{}')

                dic = {}

                # 移除一级二级键
                m_1 = pat_1.search(shop)
                if m_1:
                    old = m_1.group(0) + ','
                    shop = shop.replace(old, '')
                    key = m_1.group(1)
                    dic[key] = {}
                    k_2_arr = [e.split(':') for e in m_1.group(2).split(',')]
                    for k, v in k_2_arr:
                        dic[key][k] = eval(v)

                k_1_arr = [e.split(':', 1) for e in shop.split(',')]
                for k, v in k_1_arr:
                    dic[k] = eval(v)

                return dic
            except Exception as e:
                logging.exception(e)


        def getpromo(e_li):
            a_promo_list = e_li.xpath("//div[@class='promosearch-wrapper']//a")
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

        dic_json = {}
        dic_json['baseurl'] = response.url

        # 类别信息
        cates = self.__gettxt(response, "//div[@class='breadcrumb']//text()")
        dic_json['cates'] = cates
        logging.info(msg='cates: %s' % cates)

        # 店名
        shopname = self.__gettxt(response, "//h1[@class='shop-name']/text()")
        dic_json['shopname'] = shopname
        logging.info(msg='shopname: %s' % shopname)

        # 是否表V
        vshop = self.__gettxt(response, "//h1[@class='shop-name']/a[@class='icon v-shop']/@title")
        dic_json['vshop'] = vshop
        logging.info(msg='vshop: %s' % vshop)

        # 分店数量
        numbranch = self.__gettxt(response, "//h1[@class='shop-name']/a[@class='branch J-branch']/text()", '(\d+)')
        dic_json['numbranch'] = numbranch
        logging.info(msg='numbranch: %s' % numbranch)

        # 星级
        star = self.__gettxt(response, "//div[@class='brief-info']/span[1]/@class", '(\d+)')
        dic_json['star'] = star
        logging.info(msg='star: %s' % star)

        # 评论数
        numcomments = self.__gettxt(response, "//div[@class='brief-info']/span[@id='reviewCount']/text()", '(\d+)')
        dic_json['numcomments'] = numcomments
        logging.info(msg='numcomments: %s' % numcomments)

        # 平均价格
        meanprice = self.__gettxt(response, "//div[@class='brief-info']/span[@id='avgPriceTitle']/text()", '(\d+)')
        dic_json['meanprice'] = meanprice
        logging.info(msg='meanprice: %s' % meanprice)

        # 口味 环境 服务
        commentscore = self.__gettxt(response, "//div[@class='brief-info']/span[@id='comment_score']//text()")
        logging.info(msg='commentscore: %s' % commentscore)
        taste, env, service = getscore(commentscore)
        dic_json['taste'] = taste 
        dic_json['env'] = env 
        dic_json['service'] = service
        logging.info('taste: %s env: %s service: %s' % (taste, env, service))

        # 地址
        addr = self.__gettxt(response, "//div[@class='expand-info address']/span[@itemprop='street-address']//text()")
        dic_json['addr'] = addr
        logging.info(msg='address: %s' % addr)

        # 电话:可能是两个
        tel = self.__gettxt(response, "//span[@itemprop='tel']/text()")
        dic_json['tel'] = tel
        logging.info(msg='tel: %s' % tel)

        # 优惠信息:见parse_promo
        #promo = getpromo(response)
        #logging.info(msg='promo: %s' % promo)

        # 别名(不需要吧) 
        # 营业时间 
        # 停车信息(在评论里抓取)
        # 简洁
        shopinfo = self.__gettxt(response, "//p[@class='info info-indent']//text()")
        dic_json['shopinfo'] = shopinfo
        logging.info(msg='shophour: %s' % shopinfo)

        # 营业时间-hour
        busihour = self.__gettxt(response, u"//p[@class='info info-indent']/span[text()='营业时间：']/following::span[1]/text()")
        dic_json['busihour'] = busihour
        logging.info(msg='busihour: %s' % busihour)

        # 别名1
        alias = self.__gettxt(response, u"//p[@class='info info-indent']/span[starts-with(text(),'别')]/following::span[1]/text()")
        dic_json['alias'] = alias
        logging.info(msg='alias: %s' % alias)

        # 简介
        intro = self.__gettxt(response, u"//p[@class='info info-indent']/span[text()='餐厅简介：']/../text()")
        dic_json['intro'] = intro
        logging.info(msg='intro: %s' % intro)

        #branch 非全部(获取发起请求)
        # 暂时体统部分
        div_branch = response.xpath("//div[@id='shop-branchs']")
        branch = getbranch(div_branch)
        dic_json['branches'] = branch
        logging.debug(msg='branches: %s' % json.dumps(branch))

        # 图片数量
        piccount = self.__gettxt(response, "//*[@id='pic-count']/text()")
        dic_json['piccount'] = piccount
        logging.info(msg='piccount: %s' % piccount)

        # 隐藏字段, 如何使用这个字段（给不出实际意义)
        dic_base = getshopconfig(response.body)
        dic_json['basic'] = dic_base
        logging.debug(msg='shop config: %s' % json.dumps(dic_base))

        shopId = dic_base.get('shopId', '')

        url_comment = 'https://www.dianping.com/shop/%s/review_more' % shopId
        yield Request(url_comment, callback=self.parse_comments)


        #power = dic_base.get('power', '')
        #cityId = dic_base.get('cityId', '')
        #shopType = dic_base.get('shopType', '')

        ## ajax 优惠信息
        #if shopId and power and cityId and shopType:
        #    url_promo = 'https://www.dianping.com/ajax/json/shopDynamic/searchPromo?shopId=%s&power=%s&cityId=%s&shopType=%s' % (shopId, power, cityId, shopType)
        #    yield Request(url_promo, callback=self.parse_promo)

        #shopName = dic_base.get('shopName', '')
        #mainCategoryId = dic_base.get('mainCategoryId', '')
        #shopCityId = dic_base.get('shopCityId', '')

        #if shopId and power and cityId and shopType and shopName and mainCategoryId and shopCityId:
        #    url_dish = 'https://www.dianping.com/ajax/json/shopDynamic/shopTabs?shopId=%s&cityId=%s&shopName=%s&power=%s&mainCategoryId=%s&shopType=%s&shopCityId=%s' % (shopId, cityId, shopName, power, mainCategoryId, shopType,shopCityId)
        #    yield Request(url_dish, callback=self.parse_dish)

        #if shopId:
        #    url_houtai = 'https://www.dianping.com/ajax/json/shopfood/wizard/BasicHideInfoAjaxFP?_nr_force=1494238106490&shopId=%s' % shopId
        #    yield Request(url_houtai, callback=self.parse_houtai)

        #try:
        #    anchor = response.meta['anchor']
        #    print 'anchor anchor anchor'
        #    print json.dumps(anchor)
        #    self.tb.insertpage(response.url, anchor, response.body, struct_dic=dic_json)
        #    print response.url, 'insert success 000000000000000000000000000000000000000000000'
        #except Exception as e:
        #    logging.exception(e)

        ##yield Request(outlink, callback=self.parse_detail, meta={'anchor': anchor})
    
    def parse_promo(self, response):
        dic_promo = json.loads(response.body)
        # 这个整个入库即可
        print dic_promo


    def parse_dish(self, response):
        print response.url
        print response.body
        print 'dish: json 恐惧症， 转去抽取评论了'

    def parse_houtai(self, response):
        print response.body

    def parse_comments(self, response):

        def getstarnum(response):
            span_list = response.xpath("//div[@class='comment-star']/dl/dd/span")
            for span in span_list:
                print span
                name = self.__gettxt(span, "./a//text()")
                num  = self.__gettxt(span, "./em//text()", '(\d+)')
                print name, num



        # 先处理main
        getstarnum(response)









