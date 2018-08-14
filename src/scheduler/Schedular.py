#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/8/13 19:57
# @Author  : ganliang
# @File    : Schedular.py
# @Desc    : 页面调度器
from src.scheduler.duplicate.HashSetDuplicateRemover import HashSetDuplicateRemover


class Schedular(object):

    def __init__(self, base_url):
        self.duplicate_remover = HashSetDuplicateRemover()
        self.base_url = base_url

    def get_url(self):
        """从url管理器中取出一个url 进行数据爬取"""
        pass

    def put_url(self, url):
        """将待爬取的页面添加到控制器中"""
        pass

    def count(self):
        """计算待爬取的页面数量"""
        pass
