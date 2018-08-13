#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/8/1 21:08
# @Author  : ganliang
# @File    : Crawler.py
# @Desc    : 爬虫核心入口

import threading

from src.core.Page import Page
from src.downloader.SimpleDownloader import SimpleDownloader
from src.scheduler.HashSetScheduler import HashSetScheduler
from src.storage.ConsoleStorage import ConsoleStorage


class Crawler(threading.Thread):

    def __init__(self, base_url, pageProcess, thread_count=1):
        super(Crawler, self).__init__()
        self.setName("crawler-thread")
        self.base_url = base_url
        self.pageProcess = pageProcess
        self.thread_count = thread_count
        self.schedular = HashSetScheduler(base_url)
        self.downloader = SimpleDownloader()
        self.storage = ConsoleStorage()

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
        for thread_index in range(self.thread_count):
            crawler = CrawlerExecution(self, thread_index)
            crawler.start()


class CrawlerExecution(threading.Thread):
    """执行爬虫业务逻辑"""

    def __init__(self, crawler, thread_index):
        super(CrawlerExecution, self).__init__()
        self.crawler = crawler
        self.setName("crawler-execution-{0}-thread".format(thread_index))

    def run(self):
        while True:
            # 从页面管理器中获取页面
            url = self.crawler.schedular.get_url()
            # 下载该页面 获取页面内容
            content = self.crawler.downloader.download(url)
            if not content:
                continue
            page = Page(url, self.crawler.base_url, self.crawler).setContent(content)
            # 页面逻辑处理
            self.crawler.pageProcess.process(page)
            # 保存页面
            self.crawler.storage.storage(page.field_dict)


if __name__ == "__main__":
    pass
