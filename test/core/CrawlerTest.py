#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/8/13 22:41
# @Author  : ganliang
# @File    : CrawlerTest.py
# @Desc    : 爬虫核心类测试
from src.core.Crawler import Crawler
from src.processor.builtin.ImagePageProcess import ImagePageProcess
from src.processor.builtin.SinaNewsPageProcessor import SinaNewsPageProcessor
from src.processor.builtin.VedioPageProcess import VedioPageProcess
from src.storage.JsonStorage import JsonStorage
from src.storage.MediaStorage import MediaStorage


def hubei_news():
    """湖北新浪新闻"""
    Crawler("http://hb.sina.com.cn/news/", SinaNewsPageProcessor()) \
        .set_thread(100) \
        .set_storage(JsonStorage("D:/data/sina/hunews")) \
        .run()


def xiaohuar_images():
    """图片爬取"""
    Crawler("http://hb.sina.com.cn/news/", ImagePageProcess()) \
        .set_thread(10) \
        .set_storage(MediaStorage("D:/data/xiaohua/img")) \
        .run()


def xiaohuar_media():
    """视频爬取"""
    Crawler("http://www.xiaohuar.com/v/", VedioPageProcess(), filter_url="http://www.xiaohuar.com/") \
        .set_storage(MediaStorage("D:/data/xiaohua/video")) \
        .run()


if __name__ == "__main__":
    hubei_news()
