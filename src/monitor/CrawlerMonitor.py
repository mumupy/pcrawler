#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/8/13 22:52
# @Author  : ganliang
# @File    : CrawlerMonitor.py
# @Desc    : 监控线程
import threading
import time

from src.config.Config import logging


class CrawlerMonitor(threading.Thread):

    def __init__(self, crawler, sleep_time=60):
        super(CrawlerMonitor, self).__init__()
        self.crawler = crawler
        self.sleep_time = sleep_time
        self.setName("crawler-monitor-thread")

    def monitor(self):
        while True:
            # 待爬取的url数量
            time.sleep(self.sleep_time)
            monitorModel = self.crawler.monitorModel.statistical()
            logging.info("statistical: success[{0}] failure [{1}] schedular[{2}] duplicate [{3}] filter [ {4} ]".format(
                monitorModel.success_count, monitorModel.fail_count, monitorModel.crawler_count,
                monitorModel.duplicate_count, monitorModel.filter_count))
            logging.info("filter url {0}".format("\n".join(monitorModel.filter_urls)))

    def run(self):
        self.monitor()
