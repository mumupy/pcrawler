#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/8/31 21:34
# @Author  : ganliang
# @File    : FileCacheDuplicate.py
# @Desc    : 基于文件内存的去重器
import os
import shelve

from src.scheduler.duplicate.DuplicateRemover import DuplicateRemover


class FileCacheDuplicate(DuplicateRemover):

    def __init__(self, file_dir):
        super(FileCacheDuplicate, self).__init__()
        self.duplicat_file = shelve.open(os.path.join(file_dir, "duplicates.txt"))

    def dump(self, url):
        url_hash = self.url_hash(url)
        return self.duplicat_file.has_key(url_hash)

    def add(self, url):
        url_hash = self.url_hash(url)
        self.duplicat_file.setdefault(url_hash, "")

    def count(self):
        return self.duplicat_file.__len__()
