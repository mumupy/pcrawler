#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/8/1 21:08
# @Author  : ganliang
# @File    : Crawler.py
# @Desc    : 爬虫核心入口

import sys
import threading

from src.core.Page import Page
from src.downloader.SimpleDownloader import SimpleDownloader
from src.monitor.CrawlerMonitor import CrawlerMonitor
from src.monitor.MonitorModel import MonitorModel
from src.scheduler.HashSetScheduler import HashSetScheduler
from src.storage.ConsoleStorage import ConsoleStorage


class Crawler(threading.Thread):

    def __init__(self, base_url, pageProcess, thread_count=1, filter_url=None):
        super(Crawler, self).__init__()
        self.setName("crawler-thread")
        if not str(base_url).endswith("/"):
            base_url = base_url + "/"
        self.base_url = base_url
        self.filter_url = filter_url if filter_url else base_url
        self.pageProcess = pageProcess
        self.thread_count = thread_count
        self.schedular = HashSetScheduler(base_url)
        self.downloader = SimpleDownloader()
        self.storage = ConsoleStorage()
        self.monitorModel = MonitorModel(self)

    def set_thread(self, thread_count):
        self.thread_count = thread_count
        return self

    def set_pageprocess(self, pageprocess):
        self.pageProcess = pageprocess
        return self

    def set_schedular(self, schedular):
        self.schedular = schedular
        return self

    def set_duplicate_remover(self, duplicate_remover):
        self.schedular.set_duplicate_remover(duplicate_remover)
        return self

    def set_downloader(self, downloader):
        self.downloader = downloader
        return self

    def set_storage(self, storage):
        self.storage = storage
        return self

    def run(self):
        # 开启任务爬取线程
        for thread_index in range(self.thread_count):
            crawler = CrawlerExecution(self, thread_index)
            crawler.start()
        # 开启任务监控线程
        crawlerMonitor = CrawlerMonitor(self)
        crawlerMonitor.start()


class CrawlerExecution(threading.Thread):
    """执行爬虫业务逻辑"""

    def __init__(self, crawler, thread_index):
        super(CrawlerExecution, self).__init__()
        self.crawler = crawler
        self.setName("crawler-execution-{0}-thread".format(thread_index))

    def run(self):
        PAGE_NOTFOUND_COUNTER = 0
        while True:
            # 从页面管理器中获取页面
            url = self.crawler.schedular.get_url()
            if not url:
                PAGE_NOTFOUND_COUNTER += 1
                if (PAGE_NOTFOUND_COUNTER <= 10):
                    continue
                else:
                    sys.exit(-1)
            PAGE_NOTFOUND_COUNTER = 0
            # 下载该页面 获取页面内容
            content = self.crawler.downloader.download(url)
            # 将url添加到去重器中
            self.crawler.schedular.duplicate_remover.add(url)
            if not content:
                self.crawler.monitorModel.failure()
                continue
            self.crawler.monitorModel.success()
            page = Page(url, self.crawler.base_url, self.crawler.filter_url, self.crawler).setContent(content)
            # 页面逻辑处理
            self.crawler.pageProcess.process(page)
            if page.is_filter:
                self.crawler.monitorModel.filter(url)
                continue
            # 保存页面
            self.crawler.storage.storage(page.field_dict)


if __name__ == "__main__":
    pass
