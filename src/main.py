#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/8/1 21:08
# @Author  : ganliang
# @File    : Crawler.py
# @Desc    : 爬虫核心入口

from src.core.Crawler import Crawler
from src.processor.SinaNewsPageProcessor import SinaNewsPageProcessor

if __name__ == "__main__":
    crawler = Crawler("http://hb.sina.com.cn/news/", SinaNewsPageProcessor()).run()