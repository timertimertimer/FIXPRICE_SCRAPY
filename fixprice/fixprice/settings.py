# Scrapy settings for fixprice project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = "fixprice"

SPIDER_MODULES = ["fixprice.spiders"]
NEWSPIDER_MODULE = "fixprice.spiders"

FEEDS = {
   'data.json': {'format': 'json', 'overwrite': True}
}
# Crawl responsibly by identifying yourself (and your website) on the user-agent
# USER_AGENT = "fixprice (+http://www.yourdomain.com)"

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
# CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://docs.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
# DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
# CONCURRENT_REQUESTS_PER_DOMAIN = 16
# CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
# COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
# TELNETCONSOLE_ENABLED = False

# Override the default request headers:
# DEFAULT_REQUEST_HEADERS = {
#     "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
#     "Accept-Language": "ru,en-US;q=0.9,en;q=0e.8,hi;q=0.7,ja;q=0.6,zh-CN;q=0.5,zh;q=0.4",
#     "Cache-Control": "max-age=0",
#     "Cookie": f"i18n_redirected=ru; _cfuvid=gUURHWx2WDA7YDcPYDhs6BXozPe3maD1oIVi708Syqs-1727179961845-0.0.1.1-604800000; token=52c54bb8453b6757e96b224baa984ce6; is-logged=; visited=true; _ym_uid=1727179967584942354; _ym_d=1727179967; tmr_lvid=8e388bb3e5e6f13012585f5bf8cb2988; tmr_lvidTS=1727179967151; _ymab_param=wtLZgVhefZKXHidhaV6WMA5ir-pTEILpg8NTerSPgHRXc3rIgX4gHIs1OK5iDYQtufqFtMsP_gLLz23OBTfcP6-RSE8; _ym_isad=2; domain_sid=-UiHVnul2iy9gBoRMJD37%3A1727179967717; skip-city=true; cf_clearance=.Y0aCRDHHR4JOfhN1LXt_XFuJFFBjAHSOUbiWH4EA5Y-1727185767-1.2.1.1-Axxspv7IgVk7Dx8vaj8hSyI1PEvDqR_2R.EFkmFnKzEk4ZbJVlDGDieQnYHt0wHdHtxQcr7cJzi6Uk.TD4Yz3bO_lAOIllt0CSJHRo1.bSL3U56ie1BHl_6auhBotOwFRrxZh34x0Ph_KXN0EiJFCL_YUWpha4w8MyHnV4W5ssZd9w1mD4LNzqcOYwhBXoRhUemJbNcKN2jeBLRlrk7jE34yGmi8RQq4o3EHGEJltFzn3dhRaTGyXI8EVrwo0PZ12hsgtdaX1RaYEQmiiLA8nQpB5bLCe9lirJ04SSOAwdZ7Pvjl61BvCYpYDmz58Z.opeaqXnfRam6ZFW2k09fB1tD7ksiVeJ3wAGK9lljDhfsTkncqS78kIGiej38Dlfq.; _ym_visorc=b; tmr_detect=0%7C1727185771945; locality=%7B%22city%22%3A%22%D0%95%D0%BA%D0%B0%D1%82%D0%B5%D1%80%D0%B8%D0%BD%D0%B1%D1%83%D1%80%D0%B3%22%2C%22cityId%22%3A55%2C%22longitude%22%3A60.597474%2C%22latitude%22%3A56.838011%2C%22prefix%22%3A%22%D0%B3%22%7D",
#     "priority": "u=0, i",
#     "referer": "https://fix-price.com/",
#     "sec-ch-ua": '"Chromium";v="128", "Not;A=Brand";v="24", "Google Chrome";v="128"',
#     "sec-ch-ua-mobile": "?0",
#     "sec-ch-ua-platform": '"Windows"',
#     "sec-fetch-dest": "empty",
#     "sec-fetch-mode": "navigate",
#     "sec-fetch-site": "same-origin",
#     "upgrade-insecure-requests": "1",
#     "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36"
# }
DOWNLOADER_MIDDLEWARES = {"fixprice.middlewares.FixpriceDownloaderMiddleware": 1000}

# Enable or disable spider middlewares
# See https://docs.scrapy.org/en/latest/topics/spider-middleware.html

# Enable or disable downloader middlewares
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html

# Enable or disable extensions
# See https://docs.scrapy.org/en/latest/topics/extensions.html
# EXTENSIONS = {
#    "scrapy.extensions.telnet.TelnetConsole": None,
# }

# Configure item pipelines
# See https://docs.scrapy.org/en/latest/topics/item-pipeline.html
# ITEM_PIPELINES = {
#    "fixprice.pipelines.FixpricePipeline": 300,
# }

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/autothrottle.html
# AUTOTHROTTLE_ENABLED = True
# The initial download delay
# AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
# AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
# AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
# AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
# HTTPCACHE_ENABLED = True
# HTTPCACHE_EXPIRATION_SECS = 0
# HTTPCACHE_DIR = "httpcache"
# HTTPCACHE_IGNORE_HTTP_CODES = []
# HTTPCACHE_STORAGE = "scrapy.extensions.httpcache.FilesystemCacheStorage"

# Set settings whose default value is deprecated to a future-proof value
REQUEST_FINGERPRINTER_IMPLEMENTATION = "2.7"
TWISTED_REACTOR = "twisted.internet.asyncioreactor.AsyncioSelectorReactor"
FEED_EXPORT_ENCODING = "utf-8"
