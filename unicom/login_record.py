#!/usr/bin/env python
# -*- coding: utf-8 -*-
########################################################################
# 
# Copyright (c) 2017 Qianbao.com, Inc. All Rights Reserved
# 
########################################################################
 
"""
File: login_record.py
Author: wangqj(wangqj@qianbao.com)
Date: 2017/03/27 10:59:55
"""

import re

body = """
getLoginInfo({"result":"1","content":{"took":113,"timed_out":false,"_shards":{"total":140,"successful":140,"failed":0},"hits":{"total":13,"max_score":12.858888,"hits":[{"_index":"20170322","_type":"login_log","_id":"17032211331119100047994","_score":12.858888,"_source":{"os":"Windows 7","login_time":"2017-03-22 11:33:12","login_location":"北京 北京","login_from":"网上营业厅","brower":"Chrome 53.0.2785.143","user_id":"15507312690","login_ip":"111.200.*.*","cust_id":"9116030787240538"}},{"_index":"20170322","_type":"login_log","_id":"17032211575819100887172","_score":12.858531,"_source":{"os":"Windows 7","login_time":"2017-03-22 11:57:58","login_location":"北京 北京","login_from":"网上营业厅","brower":"Chrome 53.0.2785.143","user_id":"15507312690","login_ip":"111.200.*.*","cust_id":"9116030787240538"}},{"_index":"20170323","_type":"login_log","_id":"17032317144319149821349","_score":12.854559,"_source":{"os":"Windows 7","login_time":"2017-03-23 17:14:46","login_location":"北京 北京","login_from":"网上营业厅","brower":"Chrome 53.0.2785.143","user_id":"15507312690","login_ip":"111.200.*.*","cust_id":"9116030787240538"}},{"_index":"20170324","_type":"login_log","_id":"17032415415019192424192","_score":12.830641,"_source":{"os":"Windows 7","login_time":"2017-03-24 15:41:50","login_location":"北京 北京","login_from":"网上营业厅","brower":"Chrome 53.0.2785.143","user_id":"15507312690","login_ip":"111.200.*.*","cust_id":"9116030787240538"}},{"_index":"20170324","_type":"login_log","_id":"17032411225819182211244","_score":12.830051,"_source":{"os":"Windows 7","login_time":"2017-03-24 11:22:58","login_location":"北京 北京","login_from":"网上营业厅","brower":"Chrome 53.0.2785.143","user_id":"15507312690","login_ip":"111.200.*.*","cust_id":"9116030787240538"}},{"_index":"20170324","_type":"login_log","_id":"17032410591419180765437","_score":12.829714,"_source":{"os":"Windows 7","login_time":"2017-03-24 10:59:14","login_location":"北京 北京","login_from":"网上营业厅","brower":"Chrome 53.0.2785.143","user_id":"15507312690","login_ip":"111.200.*.*","cust_id":"9116030787240538"}},{"_index":"20170324","_type":"login_log","_id":"17032410571519180624669","_score":12.8296795,"_source":{"os":"Windows 7","login_time":"2017-03-24 10:57:15","login_location":"北京 北京","login_from":"网上营业厅","brower":"Chrome 53.0.2785.143","user_id":"15507312690","login_ip":"111.200.*.*","cust_id":"9116030787240538"}},{"_index":"20170324","_type":"login_log","_id":"17032411493819183971755","_score":12.829548,"_source":{"os":"Windows 7","login_time":"2017-03-24 11:49:38","login_location":"北京 北京","login_from":"网上营业厅","brower":"Chrome 53.0.2785.143","user_id":"15507312690","login_ip":"111.200.*.*","cust_id":"9116030787240538"}},{"_index":"20170324","_type":"login_log","_id":"17032415312419192075191","_score":12.82806,"_source":{"os":"Windows 7","login_time":"2017-03-24 15:31:26","login_location":"北京 北京","login_from":"网上营业厅","brower":"Chrome 53.0.2785.143","user_id":"15507312690","login_ip":"111.200.*.*","cust_id":"9116030787240538"}},{"_index":"20170324","_type":"login_log","_id":"17032410550019180480723","_score":12.826586,"_source":{"os":"Windows 7","login_time":"2017-03-24 10:55:02","login_location":"北京 北京","login_from":"网上营业厅","brower":"Chrome 53.0.2785.143","user_id":"15507312690","login_ip":"111.200.*.*","cust_id":"9116030787240538"}},{"_index":"20170327","_type":"login_log","_id":"17032709382419290679672","_score":11.656377,"_source":{"os":"Windows 7","login_time":"2017-03-27 09:38:25","login_location":"北京 北京","login_from":"网上营业厅","brower":"Firefox 52.0","user_id":"15507312690","login_ip":"111.200.*.*","cust_id":"9116030787240538"}},{"_index":"20170327","_type":"login_log","_id":"17032709422219290832581","_score":11.653157,"_source":{"os":"Windows 7","login_time":"2017-03-27 09:42:22","login_location":"北京 北京","login_from":"网上营业厅","brower":"Firefox 52.0","user_id":"15507312690","login_ip":"111.200.*.*","cust_id":"9116030787240538"}},{"_index":"20170327","_type":"login_log","_id":"17032709550619291335033","_score":11.648468,"_source":{"os":"Windows 7","login_time":"2017-03-27 09:55:06","login_location":"北京 北京","login_from":"网上营业厅","brower":"Firefox 52.0","user_id":"15507312690","login_ip":"111.200.*.*","cust_id":"9116030787240538"}}]}}});
"""

pat = re.compile(r'getLoginInfo\(([\s\S]*?)\);')
m = pat.search(body)
if m:
    print m.group(1)
    import json
    dic = json.loads(m.group(1))

    if 'content' in dic and 'hits' in dic['content'] and 'hits' in dic['content']['hits']:
        print 'True'
    










