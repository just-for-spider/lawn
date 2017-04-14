#!/usr/bin/env python
# -*- coding: utf-8 -*-
########################################################################
# 
# Copyright (c) 2017 Qianbao.com, Inc. All Rights Reserved
# 
########################################################################
 
"""
File: private_fun.py
Author: wangqj(wangqj@qianbao.com)
Date: 2017/04/10 15:31:08
"""


class Stu(object):

    def __init__(self):
        pass

    def __open(self):
        print 'can access'

    def ok(self):
        self.__open()



u = Stu()

u.ok()
u.__open()





can access
Traceback (most recent call last):
  File "private_fun.py", line 32, in <module>
    u.__open()
AttributeError: 'Stu' object has no attribute '__open'

