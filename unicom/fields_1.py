#!/usr/bin/env python
# -*- coding: utf-8 -*-
########################################################################
# 
# Copyright (c) 2017 Qianbao.com, Inc. All Rights Reserved
# 
########################################################################
 
"""
File: fields_1.py
Author: wangqj(wangqj@qianbao.com)
Date: 2017/03/27 13:41:31
"""

a_json = """
{"login_records": [{"user_id": "15507312690", "login_from": "\u7f51\u4e0a\u8425\u4e1a\u5385", "login_location": "\u5317\u4eac \u5317\u4eac", "cust_id": "9116030787240538", "login_ip": "111.200.*.*", "brower": "Chrome 53.0.2785.143", "os": "Windows 7", "login_time": "2017-03-22 11:33:12"}, {"user_id": "15507312690", "login_from": "\u7f51\u4e0a\u8425\u4e1a\u5385", "login_location": "\u5317\u4eac \u5317\u4eac", "cust_id": "9116030787240538", "login_ip": "111.200.*.*", "brower": "Chrome 53.0.2785.143", "os": "Windows 7", "login_time": "2017-03-22 11:57:58"}, {"user_id": "15507312690", "login_from": "\u7f51\u4e0a\u8425\u4e1a\u5385", "login_location": "\u5317\u4eac \u5317\u4eac", "cust_id": "9116030787240538", "login_ip": "111.200.*.*", "brower": "Chrome 53.0.2785.143", "os": "Windows 7", "login_time": "2017-03-23 17:14:46"}, {"user_id": "15507312690", "login_from": "\u7f51\u4e0a\u8425\u4e1a\u5385", "login_location": "\u5317\u4eac \u5317\u4eac", "cust_id": "9116030787240538", "login_ip": "111.200.*.*", "brower": "Chrome 53.0.2785.143", "os": "Windows 7", "login_time": "2017-03-24 15:41:50"}, {"user_id": "15507312690", "login_from": "\u7f51\u4e0a\u8425\u4e1a\u5385", "login_location": "\u5317\u4eac \u5317\u4eac", "cust_id": "9116030787240538", "login_ip": "111.200.*.*", "brower": "Chrome 53.0.2785.143", "os": "Windows 7", "login_time": "2017-03-24 11:22:58"}, {"user_id": "15507312690", "login_from": "\u7f51\u4e0a\u8425\u4e1a\u5385", "login_location": "\u5317\u4eac \u5317\u4eac", "cust_id": "9116030787240538", "login_ip": "111.200.*.*", "brower": "Chrome 53.0.2785.143", "os": "Windows 7", "login_time": "2017-03-24 10:59:14"}, {"user_id": "15507312690", "login_from": "\u7f51\u4e0a\u8425\u4e1a\u5385", "login_location": "\u5317\u4eac \u5317\u4eac", "cust_id": "9116030787240538", "login_ip": "111.200.*.*", "brower": "Chrome 53.0.2785.143", "os": "Windows 7", "login_time": "2017-03-24 10:57:15"}, {"user_id": "15507312690", "login_from": "\u7f51\u4e0a\u8425\u4e1a\u5385", "login_location": "\u5317\u4eac \u5317\u4eac", "cust_id": "9116030787240538", "login_ip": "111.200.*.*", "brower": "Chrome 53.0.2785.143", "os": "Windows 7", "login_time": "2017-03-24 11:49:38"}, {"user_id": "15507312690", "login_from": "\u7f51\u4e0a\u8425\u4e1a\u5385", "login_location": "\u5317\u4eac \u5317\u4eac", "cust_id": "9116030787240538", "login_ip": "111.200.*.*", "brower": "Chrome 53.0.2785.143", "os": "Windows 7", "login_time": "2017-03-24 15:31:26"}, {"user_id": "15507312690", "login_from": "\u7f51\u4e0a\u8425\u4e1a\u5385", "login_location": "\u5317\u4eac \u5317\u4eac", "cust_id": "9116030787240538", "login_ip": "111.200.*.*", "brower": "Chrome 53.0.2785.143", "os": "Windows 7", "login_time": "2017-03-24 10:55:02"}, {"user_id": "15507312690", "login_from": "\u7f51\u4e0a\u8425\u4e1a\u5385", "login_location": "\u5317\u4eac \u5317\u4eac", "cust_id": "9116030787240538", "login_ip": "111.200.*.*", "brower": "Firefox 52.0", "os": "Windows 7", "login_time": "2017-03-27 09:38:25"}, {"user_id": "15507312690", "login_from": "\u7f51\u4e0a\u8425\u4e1a\u5385", "login_location": "\u5317\u4eac \u5317\u4eac", "cust_id": "9116030787240538", "login_ip": "111.200.*.*", "brower": "Firefox 52.0", "os": "Windows 7", "login_time": "2017-03-27 09:42:22"}, {"user_id": "15507312690", "login_from": "\u7f51\u4e0a\u8425\u4e1a\u5385", "login_location": "\u5317\u4eac \u5317\u4eac", "cust_id": "9116030787240538", "login_ip": "111.200.*.*", "brower": "Firefox 52.0", "os": "Windows 7", "login_time": "2017-03-27 09:55:06"}]}
"""
import json

dic = json.loads(a_json)
for key in dic:
    for e in dic[key]:
        for k1 in e:
            t = [key, k1, e[k1]]
            line = ':'.join(t)
            print line
        break



