#!/usr/bin/env python
# -*- coding: utf-8 -*-
########################################################################
# 
# Copyright (c) 2017 Qianbao.com, Inc. All Rights Reserved
# 
########################################################################
 
"""
File: eval_test.py
Author: wangqj(wangqj@qianbao.com)
Date: 2017/04/26 16:28:42
"""

"""
功能: 将字符串str当成有效的表达式来求值并返回计算结果
语法: eval(source [, globals [, locals]]) -> value
参数：
    source：一个python表达式或函数compile()返回的代码对象
    globals: 可选必须为dictionary
    locals: 可选， 任意map对象
"""

a = "[[1,2], [3,4], [5,6], [7,8], [9,0]]"
b = eval(a)
print type(b)



a = "{1: 'a', 2: 'b'}"
b = eval(a)
print type(b)


#<type 'list'>
#<type 'dict'>


# 当前域执行
exec('a=2')
print a

# 自动生成一段python代码， 并执行
exec("print 'hello world'")



scope_1 = {'a': 100}
scope = {}
print 'what is this?',  scope.keys()

exec("a=4", scope)
print 'value=2 not 4', a

print 'in scope a is 4', scope['a']

print 'what is this, __builtins__',  scope.keys()
print 'what is this',  scope_1.keys()


# eval 命名空间
result = eval('2+3')
print 'result = 2+3', result

scope = {}
scope['a'] = 3
scope['b'] = 4 

result = eval('a+b', scope)
print result


