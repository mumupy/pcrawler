#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/8/13 22:00
# @Author  : ganliang
# @File    : DuplicateRemover.py
# @Desc    : 数据去除重复
class DuplicateRemover(object):

    def __init__(self):
        pass

    def dump(self, url):
        """检查是否存在url 如果存在返回True 否则False"""
        pass

    def add(self, url):
        """将数据添加到已爬取页面容器中"""
        pass

    def url_hash(self, url):
        """计算url的唯一性"""
        return abs(hash(url))

    def count(self):
        """计算已爬取容器的url数量"""
        pass
