#!/usr/bin/env python
# -*- coding: utf-8 -*-
########################################################################
# 
# Copyright (c) 2017 Qianbao.com, Inc. All Rights Reserved
# 
########################################################################
 
"""
File: cookie_test.py
Author: wangqj(wangqj@qianbao.com)
Date: 2017/03/28 09:11:23
"""

cookie = '_n3fa_cid=4a026a70317c4ac2ff30196c415964dd; _n3fa_ext=ft=1486953681; _n3fa_lvt_a9e72dfe4a54a20c3d6e671b3bad01d9=1490578615,1490606994,1490609311,1490662600; WT_FPC=id=2919c2e6e638094c24d1486953683738:lv=1490662622568:ss=1490662622559; Hm_lvt_9208c8c641bfb0560ce7884c36938d9d=1490234330,1490578709,1490607013,1490662623; _ga=GA1.2.1305084953.1486953684; piw=%7B%22login_name%22%3A%22155****2690%22%2C%22nickName%22%3A%22%E5%94%90%E8%B4%A4%22%2C%22rme%22%3A%7B%22ac%22%3A%22%22%2C%22at%22%3A%22%22%2C%22pt%22%3A%2201%22%2C%22u%22%3A%2215507312690%22%7D%2C%22verifyState%22%3A%22%22%7D; guide=true; _ga=GA1.3.1305084953.1486953684; mallcity=11|110; _n3fa_lpvt_a9e72dfe4a54a20c3d6e671b3bad01d9=1490662620; JUT=730ljwFD7sBs0kP6hwyyHoy9RCRCBO1pU9iiOPscjTxjOHQSGFLvjlL4UznAat0i3kOCUqZC11MgXk2jPWlUfFyEKeORsIUeKKknwOvhv+oXcUkunItNY7fAg9T16IPaxOrGGRVp2iZt6190DfSRBinaHR/3AuGUI2JIjrH0tcn0GPB287AmE+5gYAjxagVBgJjGrwiRgvKPUBjEagaoWMkNh2Ij64d9EtjdWDPzxa4j6QGkyaIYEZlzC1dXIB++EYgscCcEFMc4npqGxQv2E2iQx19jhUsibcPWjGeZyEglCntNxlTo1IPI4RiwF88sq60xatqLi2YnbzwvMipwApO8WwYXLK6jmMHGJdKBJ1lzq3oqmix8DvwY+mkO7q83tfPL1jdkT2fGK1wnWWTbnxG8kkE30SjREKXcXL/imD64AhXMy3ikzVwrpX6oOHR3ciU+OOBJh516w1eJwRdZDYJoaYM7ejZ2JvBJZrlrpSzbkUUTpzFUBvv8IMvr89uSkjj51B04jYTwE0sCGt4/anw33TvUD60CEHVtqNIwTxS9olVv70q8mYiSVrOqdk+AYO6WEUPEJS+gl4wpp0QkCA==; _uop_id=1e44c234da32556792903095bb79e993; SHOP_PROV_CITY=; Hm_lpvt_9208c8c641bfb0560ce7884c36938d9d=1490662623; route=f8deee16bbc431370c3a29ba1fdea1eb; e3=87JhYZ0c0hbLfyrw8TX7LX9yYg6jP49krr7qqMPrn17GJ1GhLJPP!1842057208; ang_sessionid=647016245002641427; ang_seqid=4; ang_catchyou=1; _dc_gtm_UA-27681312-1=1'


def str2cookie(cook):
    dic = {}
    arr = cook.split(';')
    for item in arr:

        key, val = item.strip().split('=', 1)
        print key, val
        dic[key] = val
    return dic


str2cookie(cookie)
