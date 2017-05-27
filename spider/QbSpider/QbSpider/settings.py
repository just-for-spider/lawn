# -*- coding: utf-8 -*-

# Scrapy settings for QbSpider project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#     http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
#     http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html
import sys, os
sys.path.append(os.path.abspath("../"))
BOT_NAME = 'QbSpider'

SPIDER_MODULES = ['QbSpider.spiders']
NEWSPIDER_MODULE = 'QbSpider.spiders'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'QbSpider (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See http://scrapy.readthedocs.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
#DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
#COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
#DEFAULT_REQUEST_HEADERS = {
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#   'Accept-Language': 'en',
#}

# Enable or disable spider middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'QbSpider.middlewares.MyCustomSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
#DOWNLOADER_MIDDLEWARES = {
#    'QbSpider.middlewares.MyCustomDownloaderMiddleware': 543,
#}

# Enable or disable extensions
# See http://scrapy.readthedocs.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See http://scrapy.readthedocs.org/en/latest/topics/item-pipeline.html
# ITEM_PIPELINES = {
#    'QbSpider.pipelines.dzdppipelines.QbspiderPipeline': 300,
# }

# Enable and configure the AutoThrottle extension (disabled by default)
# See http://doc.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'



#Max Reuests
CONCURRENT_REQUESTS = 50

CONCURRENT_REQUESTS_PER_DOMAIN = 50

#Enable cookie
COOKIES_ENABLED = False

#Enable download delay
DOWNLOAD_DELAY = 0.2

#Download timeout
DOWNLOAD_TIMEOUT = 45 

#Enable downloadmiddleware
DOWNLOADER_MIDDLEWARES = {
    'scrapy.downloadermiddlewares.useragent.UserAgentMiddleware': None,
    'scrapy.contrib.downloadermiddleware.httpproxy.HttpProxyMiddleware': None,
    'QbSpider.middleware.RandomUserAgentMiddleware.RotateUserAgentMiddleware':500,
    'QbSpider.middleware.RandomProxyMiddleware.ProxyMiddleware':750,
}

#Enable dupefilter can change
DUPEFILTER_CLASS = 'scrapy.dupefilters.RFPDupeFilter'

#Enable pipeline
#ITEM_PIPELINES = {
#    'QbSpider.dzdppipelines.QbspiderPipeline': 300,
#}

#Enable log
LOG_ENABLED = True
LOG_ENCODING = 'utf-8'
LOG_FORMATTER = 'scrapy.logformatter.LogFormatter'
LOG_FORMAT = '%(asctime)s [%(name)s] %(levelname)s: %(message)s'
LOG_DATEFORMAT = '%Y-%m-%d %H:%M:%S'
#Enable print anything in py
LOG_STDOUT = False
LOG_LEVEL = 'DEBUG'
LOG_FILE = None

#max thread pool size
# REACTOR_THREADPOOL_MAXSIZE = 150
REACTOR_THREADPOOL_MAXSIZE = 50

# Enable url referer avoid web count your visit urls
REFERER_ENABLED = False

#Enable redisrect
REDIRECT_ENABLED = False
#max retry times for failed url
REDIRECT_MAX_TIMES = 20  # uses Firefox default setting
REDIRECT_PRIORITY_ADJUST = +2
#if 1 Enable TelnetConsole
TELNETCONSOLE_ENABLED = 0

#SCHEDULER = "QbSpider.scrapy_redis.scheduler.Scheduler"

#SCHEDULER_QUEUE_CLASS = "QbSpider.scrapy_redis.queue.SpiderPriorityQueue",

#Enable retry
RETRY_ENABLED = False # not retry
#xRETRY_TIMES = 40 # initial response + 2 retries = 3 requests
RETRY_TIMES = 1 # initial response + 2 retries = 3 requests
RETRY_TIMES_VPS = 3
RETRY_HTTP_CODES = [511, 500, 502, 503, 504, 408, 404, 403, 400, 405, 407, 437, 307, 0, 429, 401, 402]
PROXY_MIN_NUM = 40
PROXY_MIN_NUM_VPS = 2
#RETRY_PRIORITY_ADJUST = -1

# default disobey site robotstxt
#ROBOTSTXT_OBEY = False


# default use  chrome user-agent
USER_AGENT = "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36"

REDIS_PARAMSS = {
#'REDIS_HOST':'172.28.40.21',
'REDIS_HOST':'172.28.40.23',
#'REDIS_HOST':'61.164.149.156',
#'REDIS_HOST':'192.168.0.16',
'REDIS_PORT':6379,
'REDIS_PASSWORD':"Qbbigdata"
#'REDIS_PASSWORD':'qianbao'
}

REDIS_URL = "redis://:Qbbigdata@172.28.40.23:6379"
# Enables scheduling storing requests queue in redis.
SCHEDULER = 'scrapy_redis.scheduler.Scheduler'
# Ensure all spiders share same duplicates filter through redis.
DUPEFILTER_CLASS = 'scrapy_redis.dupefilter.RFPDupeFilter'
# Don't cleanup redis queues, allows to pause/resume crawls.
SCHEDULER_PERSIST = True
# Schedule requests using a priority queue. (default)
SCHEDULER_QUEUE_CLASS = 'scrapy_redis.queue.SpiderPriorityQueue'

# REDIS_START_URLS_BATCH_SIZE = 1
#REDIS_START_URLS_BATCH_SIZE = 150

#COMMANDS_MODULE = 'QbSpider.scrapyd.crawl'

PROXY_MYSQL={ 'Host':'172.28.40.21', 'User':'crawler','Passwd':'crawler', 'Db':'crawl', 'Charset':'utf8'}

PROXY_MYSQL_VPS={ 'Host':'172.28.40.47', 'User':'root','Passwd':'Qbbigdata', 'Db':'proxys', 'port':3306, 'Charset':'utf8'}

# PROXY_SQL = "SELECT `ip` FROM `new_ip` WHERE `speed` <= '1500' LIMIT 0, 1000"
PROXY_SQL = "SELECT `ip` from new_ip WHERE `status` = 1 and `speed` <= '5000' Order By update_time Desc LIMIT 0, 1000"

PROXY_SQL_VPS = "SELECT ip,update_time FROM new_ip WHERE UPDATE_TIME IN (SELECT MAX(update_time) FROM `new_ip` WHERE `site1` = 1) LIMIT 1"

EXTENSIONS ={'scrapy.extensions.telnet.TelnetConsole': None}

USELOCALIP = 0

LOGIN_TYPE = False

PARAMS_CONNECT_HBASE = {'host': '172.28.40.45', 'port': 9090, 'buf': 512}

LOGIN_URL = [
            "http://login.189.cn/login",
            "http://www.xzgjj.com:7001/wscx/index.jsp",
        ]

