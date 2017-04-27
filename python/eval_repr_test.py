#!/usr/bin/env python
# -*- coding: utf-8 -*-
########################################################################
# 
# Copyright (c) 2017 Qianbao.com, Inc. All Rights Reserved
# 
########################################################################
 
"""
File: eval_repr_test.py
Author: wangqj(wangqj@qianbao.com)
Date: 2017/04/26 17:01:47
"""

exec 'print "hello wordl"'
print '------------'


exec('a=1')
print a

print eval('3+4*7+2**-2')
print eval('a==1')

# repr 函数用来规范对象的规范字符串标识， 反引号（也成转换符）可以完成相同的功能。注意； 大多数时候 eval(repe(obj)) = obj
# 基本上repr 与 反引号 用来获取对象的可打印的表示形式。 你可以通过定义 __repr__ 方法来控制你的对象在被repr函数调用的时候返回的内容1

i = []
i.append('item')
print i

print repr(i)


dic = {1: 'a', 10: 'b', 20: 'c'}
print repr(dic)
print `dic`


hello wordl
------------
1
31.25
True
['item']
['item']
{1: 'a', 10: 'b', 20: 'c'}
{1: 'a', 10: 'b', 20: 'c'}
