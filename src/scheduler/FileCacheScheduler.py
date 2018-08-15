#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/8/15 22:55
# @Author  : ganliang
# @File    : FileCacheScheduler.py
# @Desc    : 使用文件缓存待爬取的url列表和已爬取的页面
import os

from src.scheduler.Schedular import Schedular


class FileCacheScheduler(Schedular):

    def __init__(self, base_url, file_dir):
        super(FileCacheScheduler, self).__init__(base_url)
        if not os.path.exists(file_dir):
            os.makedirs(file_dir)
        self.url_file = open(os.path.join(file_dir, "urls.txt"), "w")
        self.duplicat_file = open(os.path.join(file_dir, "duplicates.txt"), "w")

    def get_url(self):
        super(FileCacheScheduler, self).get_url()

    def put_url(self, url):
        super(FileCacheScheduler, self).put_url(url)

    def count(self):
        super(FileCacheScheduler, self).count()
