#!/usr/bin/env python
# -*- coding: utf-8 -*-
########################################################################
# 
# Copyright (c) 2017 Qianbao.com, Inc. All Rights Reserved
# 
########################################################################
 
"""
File: class_inherit.py
Author: wangqj(wangqj@qianbao.com)
Date: 2017/05/03 10:20:28
"""

class SchoolMember:

    def __init__(self, name, age):
        self.name = name
        self.age = age
        print 'initialized SchoolMember: %s' % self.name


    def tell(self):
        print 'Name:%s, Age:%s' % (self.name, self.age)


class Teacher(SchoolMember):

    def __init__(self, name, age, salary):
        SchoolMember.__init__(self, name, age)
        self.salary = salary
        print 'initialized Teacher: %s' % self.name

    def tell(self):
        SchoolMember.tell(self)
        print 'salary:%s' % self.salary


class Student(SchoolMember):

    def __init__(self, name, age, marks):
        SchoolMember.__init__(self, name, age)
        self.marks = marks
        print 'initialized Student: %s' % self.name

    def tell(self):
        SchoolMember.tell(self)
        print 'marks:%s' % self.marks


t = Teacher('Mrs. shrividya', 40, 30000)
s = Student('Swaroop', 22, 75)

members = [t, s]
for m in members:
    m.tell()



