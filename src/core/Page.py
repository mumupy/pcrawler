#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/8/13 20:14
# @Author  : ganliang
# @File    : Page.py
# @Desc    : 页面内容信息
class Page:
    def __init__(self, url, base_url, filter_url, crawler):
        self.url = url
        self.base_url = base_url
        self.filter_url = filter_url
        self.content = None
        self.crawler = crawler
        self.field_dict = {}
        self.is_filter = False

    def setContent(self, content):
        self.content = content
        return self

    def getContent(self):
        return self.content

    def put_field(self, field_name, field_value):
        self.field_dict.setdefault(field_name, field_value)
        return self

    def put_fields(self, field_name, field_values):
        self.field_dict.setdefault(field_name, []).extend(field_values)
        return self

    def put_field_dict(self, field_dict):
        self.field_dict.update(field_dict)
        return self

    def put_url(self, url):
        self.crawler.schedular.put_url(url)
