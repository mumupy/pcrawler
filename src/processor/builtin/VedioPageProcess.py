#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/8/14 23:17
# @Author  : ganliang
# @File    : VedioPageProcess.py
# @Desc    : video视频下载器
from src.processor.PageProcess import PageProcess


class VedioPageProcess(PageProcess):
    """直接下载页面的video视频文件"""

    def process(self, page):
        res_html = self.handler(page)

        video_urls = res_html.xpath("//video/source/@src")
        if video_urls:
            page.put_fields("video", video_urls)
