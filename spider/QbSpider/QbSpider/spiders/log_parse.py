#!/usr/bin/env python
# -*- coding: utf-8 -*-
########################################################################
# 
# Copyright (c) 2017 Qianbao.com, Inc. All Rights Reserved
# 
########################################################################
 
"""
File: log_parse.py
Author: wangqj(wangqj@qianbao.com)
Date: 2017/05/22 10:53:10
"""

import sys
import re


# 抽取invalid url
#pat = re.compile('invalid outlink: (.*)')
#
#urls = set()
#
#if __name__ == '__mian__':
#    for line in sys.stdin:
#        line = line.strip()
#    
#        m = pat.search(line)
#        if m:
#            url = m.group(1)
#            urls.add(url)
#    
#    for uri in urls:
#        print uri


if __name__ == '__main__':
    pat = re.compile('response\.status\<(\d+)\> request.url\<(.*)\>')

    urls = set()
    
    for line in sys.stdin:
        m = pat.search(line)
        if m:
            status, url = m.group(1), m.group(2)
            if status != '200':
                #print status, url
                #urls.add(status + ' ' + url)
                urls.add(url)

    for uri in urls:
        print uri
