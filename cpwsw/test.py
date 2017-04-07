#!/usr/bin/env python
# -*- coding: utf-8 -*-
########################################################################
# 
# Copyright (c) 2017 Qianbao.com, Inc. All Rights Reserved
# 
########################################################################
 
"""
File: test.py
Author: wangqj(wangqj@qianbao.com)
Date: 2017/04/01 17:31:10
"""


class Stu(object):

    def __init__(self):
        self.qq = _encode('xxs')
        print self.qq




def _encode(astr):
    return 'hello ' + astr




s = Stu()

