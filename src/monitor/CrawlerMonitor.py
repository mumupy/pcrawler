#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/8/13 22:52
# @Author  : ganliang
# @File    : CrawlerMonitor.py
# @Desc    : 监控线程
import threading


class CrawlerMonitor(threading.Thread):

    def __init__(self, crawler):
        super(CrawlerMonitor, self).__init__()
        self.crawler = crawler
        self.setName("crawler-monitor-thread")

    def monitor(self):
        # 待爬取的url数量
        self.crawler.schedular.waiting_count()
