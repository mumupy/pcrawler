#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/8/13 19:56
# @Author  : ganliang
# @File    : PageProcess.py
# @Desc    : 页面数据抽取器
from lxml import etree


class PageProcess:
    def process(self, page):
        pass

    def handler(self, page):
        res_html = etree.HTML(page.getContent())
        a_elements = res_html.xpath("//a/@href")

        # 爬去新的页面添加到url理器中
        for a_element in a_elements:
            if a_element.find("javascript") >= 0 or a_element.find("#") >= 0:
                continue
            if a_element.find(page.filter_url) == -1:
                continue
            page.put_url(a_element)
        return res_html
