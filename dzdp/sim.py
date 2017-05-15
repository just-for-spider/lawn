#!/usr/bin/env python
# -*- coding: utf-8 -*-
########################################################################
# 
# Copyright (c) 2017 Qianbao.com, Inc. All Rights Reserved
# 
########################################################################
 
"""
File: sim.py
Author: wangqj(wangqj@qianbao.com)
Date: 2017/04/25 11:22:30
"""

from __future__ import division, unicode_literals

import hashlib
import collections
from itertools import groupby


def _hashfunc(x):
    return int(hashlib.md5(x).hexdigest(), 16)


class Simhash(object):

    def __init__(self, value, f=64, reg=r'[\w\u4e00-\u9fcc]+', hashfunc=None):
        self.f = f
        self.reg = reg
        self.value = None

        if isinstance(value, basestring):
            pass
        else:
            raise Exception('Bad parameter with type {}'.format(type(value)))

    def _tokenize(self, content):
        """分词"""
        return None


    def build_by_text(self, content):
        features = self._tokenize(content)
        # 统计词频
        features = {k:sum(1 for _ in g) for k, g in groupby(sorted(features))}
        return self.build_by_features(features)

    def build_by_features(self, features):
        pass





def lcsstr(s1, s2):
    m = [[0 for i in range(len(s2) + 1)]  for j in range(len(s1) + 1)]
    mmax = 0
    p = 0

    for i in range(len(s1)):
        for j in range(len(s2)):
            if s1[i]==s2[j]:
                m[i+1][j+1] = m[i][j] + 1
                if m[i+1][j+1] > mmax:
                    mmax = m[i+1][j+1]
                    p = i + 1
    prob = float(mmax) / len(s2)
    return s1[p-mmax:p],mmax, prob


def lcsseq(s1, s2):
    m = [[0 for x in range(len(s2)+1)] for y in range(len(s1)+1)] 
    d = [[None for x in range(len(s2)+1)] for y in range(len(s1)+1)]
    for p1 in range(len(s1)):
        for p2 in range(len(s2)):
            if s1[p1] == s2[p2]:
                m[p1+1][p2+1] = m[p1][p2]+1
                d[p1+1][p2+1] = 'ok'
            elif m[p1+1][p2] > m[p1][p2+1]:
                m[p1+1][p2+1] = m[p1+1][p2]
                d[p1+1][p2+1] = 'left'
            else:
                m[p1+1][p2+1] = m[p1][p2+1]
                d[p1+1][p2+1] = 'up'
    (p1, p2) = (len(s1), len(s2))
    s = []
    while m[p1][p2]:
        c = d[p1][p2]
        if c == 'ok':
            s.append(s1[p1-1])
            p1-=1
            p2-=1
        if c =='left':
            p2 -= 1
        if c == 'up':
            p1 -= 1
    s.reverse()
    return ''.join(s)



if __name__ == '__main__':

    s1 = 'abcdfg'
    s2 = 'abdfg'
    print lcsstr(s1, s2)


    s1 = 'abdfg'
    s2 = 'abcdfg'
    print lcsseq(s1, s2)
