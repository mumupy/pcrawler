#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/8/1 21:08
# @Author  : ganliang
# @File    : Crawler.py
# @Desc    : 爬虫核心入口

from src.core.Crawler import Crawler
from src.processor.builtin.VedioPageProcess import VedioPageProcess

if __name__ == "__main__":
    # 湖北新浪新闻
    # crawler = Crawler("http://hb.sina.com.cn/news/", SinaNewsPageProcessor()) \
    #     .set_thread(20) \
    #     .run()
    # Crawler("http://www.xiaohuar.com/", ImagePageProcess()).run()
    Crawler("http://www.xiaohuar.com/v/", VedioPageProcess(), filter_url="http://www.xiaohuar.com/").run()
