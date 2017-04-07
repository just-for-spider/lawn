#!/bin/bash


SPIDER_HOME=/home/app_bank/zhaoqipeng/QbSpider/QbSpider/spiders/

cat ${SPIDER_HOME}/spider.log | python log_stat.py "$1"

