#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/8/15 22:55
# @Author  : ganliang
# @File    : FileCacheScheduler.py
# @Desc    : 使用文件【shelve】缓存待爬取的url列表和已爬取的页面
import os
import shelve
import time

from src.config.Config import logging
from src.scheduler.Schedular import Schedular
from src.scheduler.duplicate.FileCacheDuplicate import FileCacheDuplicate


class FileCacheScheduler(Schedular):

    def __init__(self, base_url, file_dir):
        super(FileCacheScheduler, self).__init__(base_url)
        if not os.path.exists(file_dir):
            os.makedirs(file_dir)
        self.duplicate_remover = FileCacheDuplicate(file_dir)
        self.url_file = shelve.open(os.path.join(file_dir, "urls.txt"))

    def get_url(self):
        retry_counter = 0
        while True:
            try:
                page_url = self.url_file.popitem()[0]
                logging.info(page_url)
                return page_url
            except Exception as ex:
                if retry_counter < 3:
                    time.sleep(1)
                    retry_counter += 1
                else:
                    raise TypeError("页面无数据")

    def put_url(self, url):
        if not self.url_file.has_key(url) and not self.duplicate_remover.dump(url):
            self.url_file.setdefault(url, "")

    def count(self):
        return self.url_file.__len__()
