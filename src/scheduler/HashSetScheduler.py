#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/8/13 20:06
# @Author  : ganliang
# @File    : HashSetScheduler.py
# @Desc    : 随机列表url控制器
import threading
import time

from src.config.Config import logging
from src.scheduler.Schedular import Schedular


class HashSetScheduler(Schedular):

    def __init__(self, base_url):
        super(HashSetScheduler, self).__init__(base_url)
        self.urls = list()  # set 不是线程安全的
        self.urls.append(self.base_url)
        self.scheduler_lock = threading.Lock()

    def set_duplicate_remover(self, duplicate_remover):
        self.duplicate_remover = duplicate_remover

    def get_url(self):
        retry_counter = 0
        try:
            self.scheduler_lock.acquire()
            while True:
                if len(self.urls) == 0:
                    if retry_counter < 3:
                        time.sleep(1)
                        retry_counter += 1
                    else:
                        raise TypeError("页面无数据")
                else:
                    page_url = self.urls.pop(0)
                    logging.info(page_url)
                    return page_url
        except Exception as ex:
            logging.error(ex)
        finally:
            self.scheduler_lock.release()

    def put_url(self, url):
        if url not in self.urls and not self.duplicate_remover.dump(url):
            self.urls.append(url)

    def put_urls(self, urls):
        for url in urls:
            self.put_url(url)

    def count(self):
        return len(self.urls)
