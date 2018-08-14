#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/8/14 22:31
# @Author  : ganliang
# @File    : ImagePageProcess.py
# @Desc    : 图片抓取器

from src.config.Config import logging
from src.processor.PageProcess import PageProcess


class ImagePageProcess(PageProcess):

    def process(self, page):
        res_html = self.handler(page)

        img_urls = res_html.xpath("//img/@src")

        imgs = []
        for img_url in img_urls:
            if str(img_url).find("/skin/") > -1:
                continue
            if str(img_url).startswith("/"):
                img_url = page.base_url + img_url[1:]
                imgs.append(img_url)
        page.put_fields("img", imgs)
        logging.info(imgs)
