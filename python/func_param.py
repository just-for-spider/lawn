#!/usr/bin/env python
# -*- coding: utf-8 -*-



def fun(t):
    print id(t)
    t.sort()
    print id(t)
    print t


def fun1(q):
    print id(q)
    q = 100
    print id(q)
    print q


m = [1, 3, 2, 100, -19]

print 'origin: ', id(m), m


fun(m)

print 'modify: ', id(m), m



n = 19000000000000000
print 'origin: ', id(n), n
fun1(n)
print 'modify: ', id(n), n





