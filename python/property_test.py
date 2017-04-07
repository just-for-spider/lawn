#!/usr/bin/env python
# -*- coding: utf-8 -*-
########################################################################
# 
# Copyright (c) 2017 Qianbao.com, Inc. All Rights Reserved
# 
########################################################################
 
"""
File: property_test.py
Author: wangqj(wangqj@qianbao.com)
Date: 2017/04/01 11:56:16
"""


class Student(object):

    #def get_score(self):
    #    return self._score

    #def set_score(self, value):
    #    if not isinstance(value, int):
    #        raise ValueError('score must be an integer')
    #    if value < 0 or value > 100:
    #        raise ValueError('score must between 0~100!')
    #    self._score = value

    #@property
    #def score(self):
    #    return self._score

    #@score.setter
    def score(self, value):
        if not isinstance(value, int):
            raise ValueError('score must be an integer')
        if value < 0 or value > 100:
            raise ValueError('score must between 0~100!')
        self._score = value


s = Student()
s.score = 80

print s.score


class Person(object):

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    @property
    def full_name(self):
        return '%s %s' % (self.first_name, self.last_name)


person = Person('Mike', 'Driscoll')
print person.full_name

#person.full_name = 'jackalope'


from decimal import Decimal


class Fees(object):

    def __init__(self):
        self._fee = None

    def get_fee(self):
        return self._fee

    def set_fee(self, value):
        if isinstance(value, str):
            self._fee = Decimal(value)
        elif isinstance(value, Decimal):
            self._fee = value

    fee = property(get_fee, set_fee)


f = Fees()
#f.set_fee('1')
#print f.get_fee()

f.fee = '2'

print f.fee

'''当我们以这种方式使用属性时，它允许fee属性设置并获取值本身而不需要破坏原有代码。'''
'''让我们用属性装饰器来重写这段代码， 看看我们能否得到 一个允许设置属性的值'''



80
Mike Driscoll
2

