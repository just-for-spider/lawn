#!/usr/bin/env python
# -*- coding: utf-8 -*-
########################################################################
# 
# Copyright (c) 2017 Qianbao.com, Inc. All Rights Reserved
# 
########################################################################
 
"""
File: key_func.py
Author: wangqj(wangqj@qianbao.com)
Date: 2017/04/26 14:57:27
"""

input = 'This is a test string from Andrew'

output1 = sorted(input.split())
output2 = sorted(input.split(), key=str.lower)

print output1
print output2


student_tuples = [('john', 'A', 15), ('jane', 'B', 12), ('dave', 'B', 10)]
output = sorted(student_tuples, key=lambda student: student[2])
print output

from operator import itemgetter, attrgetter, methodcaller

class Student:

    def __init__(self, name, grade, age):
        self.name = name
        self.grade = grade
        self.age = age

    def __repr__(self):
        return repr((self.name, self.grade, self.age))

    def weighted_grade(self):
        return 'CBA'.index(self.grade) / float(self.age)


student_objects = [
    Student('john', 'A', 15),
    Student('jane', 'B', 12),
    Student('dave', 'B', 10),
]

output = sorted(student_objects, key=lambda student: student.age)
print output


print sorted(student_tuples, key=itemgetter(2))
print sorted(student_objects, key=attrgetter('age'))


# 对字典
# sorted(teamitems ,key = lambda x:(x['P'],x['GD'],x['GS'],x['GA']),reverse=True)
# sorted(teamitems ,key = itemgetter('P','GD','GS','GA'),reverse=True)
# sorted(student_tuples, key=itemgetter(1,2))


output = [(student.name, student.weighted_grade()) for student in student_objects]
print output
print sorted(student_objects, key=methodcaller('weighted_grade'))


