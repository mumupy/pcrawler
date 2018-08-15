#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/8/14 21:58
# @Author  : ganliang
# @File    : MonitorModel.py
# @Desc    : 监控模型
class MonitorModel(object):

    def __init__(self, crawler):
        self.crawler = crawler
        self.success_count = 0
        self.fail_count = 0
        self.start_time = None
        self.crawler_count = 0
        self.duplicate_count = 0
        self.filter_count = 0
        self.filter_urls = set()

    def success(self):
        self.success_count += 1
        return self

    def failure(self):
        self.fail_count += 1
        return self

    def statistical(self):
        self.crawler_count = self.crawler.schedular.count()
        self.duplicate_count = self.crawler.schedular.duplicate_remover.count()
        return self

    def filter(self, url):
        self.filter_count += 1
        self.filter_urls.add(url)
