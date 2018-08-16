#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/8/13 19:56
# @Author  : ganliang
# @File    : PageProcess.py
# @Desc    : 页面数据抽取器
import os

from lxml import etree


class PageProcess:
    def process(self, page):
        pass

    def handler(self, page):
        res_html = etree.HTML(page.getContent())
        a_elements = res_html.xpath("//a/@href")

        # 爬去新的页面添加到url理器中
        for a_element in a_elements:
            a_element = str(a_element)
            if a_element.find("javascript") >= 0 or a_element.find("#") >= 0:
                continue
            # 如果链接只包含后缀 需要将前缀添加进去
            base_url = os.path.dirname(page.url)
            if a_element.find("www") == -1 and a_element.find("http") == -1 and a_element.find(base_url) == -1:
                if a_element.startswith("/"):
                    a_element = a_element[1:]
                a_element = os.path.join(base_url, a_element).replace("\\", "/")
                relative_index = a_element.find("/../")
                if relative_index > -1:
                    a_element = a_element[:relative_index] + a_element[relative_index + 3:]
            filter = True
            for filter_url in page.filter_url:
                if a_element.find(filter_url) > -1:
                    filter = False
            if filter:
                continue
            page.put_url(a_element)
        return res_html
