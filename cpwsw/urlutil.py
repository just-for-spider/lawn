#!/usr/bin/env python
# -*- coding: utf-8 -*-
########################################################################
# 
# Copyright (c) 2017 Qianbao.com, Inc. All Rights Reserved
# 
########################################################################
 
"""
File: urlutil.py
Author: wangqj(wangqj@qianbao.com)
Date: 2017/04/01 16:21:03
"""
from urllib import urlencode
from scrapy.utils.python import is_listlike


def to_bytes(text, encoding=None, errors='strict'):
    """Return the binary representation of `text`. If `text`
    is already a bytes object, return it as-is."""
    if isinstance(text, bytes):
        return text
    if encoding is None:
        encoding = 'utf-8'
    return text.encode(encoding, errors)


def _urlencode(seq, enc):
    values = [(to_bytes(k, enc), to_bytes(v, enc))
                for k, vs in seq
                for v in (vs if is_listlike(vs) else [vs])]
    return urlencode(values, doseq=1)

