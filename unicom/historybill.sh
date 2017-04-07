#!/bin/bash


SPIDER_HOME=/home/app_bank/zhaoqipeng/QbSpider/QbSpider/spiders/

cat ${SPIDER_HOME}/spider.log | grep "historybill struct json" | awk -Fjson: '{print $2}' | python historybill.py

