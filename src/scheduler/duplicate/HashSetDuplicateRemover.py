#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/8/13 19:23
# @Author  : ganliang
# @File    : HashSetDuplicateRemover.py
# @Desc    : 基于内存set去重

from src.scheduler.duplicate.DuplicateRemover import DuplicateRemover


class HashSetDuplicateRemover(DuplicateRemover):
    """基于内存的去除重复业务逻辑，将页面的hash(URL)全部保存到集合中"""

    def __init__(self):
        self.DUMP_URLS = list()  # 保存所有的页面 页面去除重复

    def dump(self, url):
        """判断数据是否有重复 如果没有重复则保存到集合中 否则直接返回"""
        url_hash = self.url_hash(url)
        return url_hash in self.DUMP_URLS

    def add(self, url):
        url_hash = self.url_hash(url)
        self.DUMP_URLS.append(url_hash)

    def count(self):
        return len(self.DUMP_URLS)
